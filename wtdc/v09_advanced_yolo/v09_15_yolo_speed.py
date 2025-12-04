from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("wtdc/v09_advanced_yolo/speed.mp4")

# 2. 속도 객체 생성
speed = solutions.SpeedEstimator(
    model="yolo11n.pt",
    show=True,
    max_speed=200, # 최대 속도 제한
    max_hist=5, # 최소 추적 프레임 수
    meter_per_pixel=0.5, # 1픽셀당 실제 이동 거리 설정
    # 실제 이동 거리 = 픽셀 이동량 x meter_per_pixel
    line_width=5 # 박스 선 두께 조절
)

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    results = speed(frame)

# 4. 자원해제
cap.release()
cv2.destroyAllWindows()