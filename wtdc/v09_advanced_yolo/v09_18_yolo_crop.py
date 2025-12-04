from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("wtdc/v09_advanced_yolo/crop.mp4")

# 2. crop 객체 생성
cropper = solutions.ObjectCropper(
    model="yolo11n.pt",
    show=False,
    conf=0.7
)

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    crop_frame = cropper(frame)

# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()