from ultralytics import YOLO
import cv2
import streamlit as st
import pandas as pd
import plotly.express as px
import time

# 1. 페이지 기본 설정
st.set_page_config(layout="wide")
st.title("WEB YOLO")

# 2. 화면 설정
col1, col2 = st.columns(2) # 화면 좌우를 두 개의 컬럼으로 분리

with col1:
    frame_placeholder = st.empty()

with col2:
    chart_placeholder = st.empty()

# 3. 비디오 경로 설정
cap = cv2.VideoCapture(0)

# 4. 모델 로드
model = YOLO("yolo11n.pt")

# 5. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("FRAME ERROR")
        st.warning("FRAME ERROR")
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    # 탐지된 객체의 클래스 이름 추출
    labels = [model.names[int(c)] for c in results[0].boxes.cls]

    # labels 리스트가 비어 있지 않은 경우 (탐지된 객체가 있을 때)
    if labels:
        # labels 리스트를 DataFrame으로 변환 후 객체별 개수 집계
        df_count = pd.DataFrame({"Object": labels})
        df_count = df_count.value_counts().reset_index(name="Count")

        # plotly로 막대 그래프 생성
        fig = px.bar(
            df_count,
            x="Object",
            y="Count",
            title="탐지 객체 수",
            color="Object",
            text="Count"
        )
        fig.update_layout(showlegend=False) # 범례 제거
        fig.update_traces(textposition="outside") # 막대 위에 숫자 표시
    else:
        # 탐지된 객체가 없을 때 빈 그래프 생성
        df_count = pd.DataFrame({"Object": [], "Count": []})
        fig = px.bar(
            df_count,
            x="Object",
            y="Count",
            title="탐지 객체 수"
        )

    # 왼쪽 화면에 YOLO 분석 프레임 표시
    frame_placeholder.image(annotated_frame, channels="RGB")

    # 오른쪽 화면에 그래프 표시
    chart_placeholder.plotly_chart(fig,
                                   use_container_width=True,
                                   key=f"chart_{time.time()}"
                                   )

# 6. 자원 해제
cap.release()
cv2.destroyAllWindows()