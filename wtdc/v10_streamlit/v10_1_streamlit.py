from ultralytics import YOLO
import cv2
import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(layout="wide")
st.title("WEB YOLO")

# 2. 영상 공간 설정
frame_placeholder = st.empty()

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

    frame_placeholder.image(annotated_frame, channels="BGR")

# 6. 자원 해제
cap.release()
cv2.destroyAllWindows()
# pip install streamlit