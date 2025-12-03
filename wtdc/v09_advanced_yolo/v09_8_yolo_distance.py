from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture(0)

# 2. 거리 계산 객체 생성
distance_calculator = solutions.DistanceCalculation(
    model="yolo11n.pt",
    show=True,
    conf=0.3,
    iou=0.2
)

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 못 읽음!")
        break

    results = distance_calculator(frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()

# 거리에 따른 조건 정의 작성
