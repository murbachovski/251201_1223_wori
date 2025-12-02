from ultralytics import YOLO
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture(0)

# 2. 모델 로드
model = YOLO("yolo11x.pt")

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    # 3-1. 모델 예측
    results = model(frame)
    
    # 3-2. 결과 값 표시
    annotated_frame = results[0].plot()
    
    # 탐지된 바운딩 박스
    boxes = results[0].boxes
    
    # 탐지된 객체 수 계산
    count = 0
    for i in boxes.cls:
        count += 1
    
    # 조건문으로 상태 메시지 결정
    if count >= 10:
        status = "Danger"
        color = (255, 0, 0)
    elif count >= 7:
        status = "warning"
        color = (0, 255, 0)
    elif count >= 3:
        status = "Normal"
        color = (0, 0, 255)
    else:
        status = "Safe"
        color = (0, 0, 0)
    
    cv2.putText(
        annotated_frame, # 표시 프레임
        f"Detected : {count}, {status}", # 표시 내용
        (10, 30), # 표시 위치
        cv2.FONT_HERSHEY_SIMPLEX, # 폰트 스타일
        1, # 폰트 크기
        color, # 색상
        2 # 두께
    )
    
    # 3-3. 윈도우 창 설정
    cv2.imshow("PUTTEXT_YOLO", annotated_frame)
    
    # 3-4. q키를 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('q키를 눌러서 종료합니다.')
        break
    
# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()

# 1. https://www.utic.go.kr/map/map.do?menu=incident
# 2. CCTV 주소 복사
# 3. https://strm2.spatic.go.kr/live/131.stream/playlist.m3u8