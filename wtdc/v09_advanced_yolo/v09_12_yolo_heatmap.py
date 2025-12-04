from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("wtdc/v09_advanced_yolo/input.mp4")

# 2. Heatmap 설정
heatmap = solutions.Heatmap(
    model="yolo11n.pt",
    show=True,
    conf=0.3,
    # colormap=cv2.COLORMAP_PARULA
    colormap=cv2.COLORMAP_PINK
)

# 3. 비디오 프레임 설정
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임을 못 읽었습니다.")
        break

    heat_frame = heatmap(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()