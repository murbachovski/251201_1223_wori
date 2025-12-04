from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("wtdc/v09_advanced_yolo/inout.mp4")

# 2. 라인 설정
lines = [(22, 366), (1251, 200)]

# 3. inout 객체 생성
count_lines = solutions.ObjectCounter(
    model="yolo11n.pt",
    show=True,
    region=lines
)

# 4. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    count_frame = count_lines(frame)

# 5. 자원 해제
cap.release()
cv2.destroyAllWindows()