from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("wtdc/v09_advanced_yolo/input.mp4")
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# 2. 특정 좌표 설정
# 클릭한 좌표는 => 612, 96
# 클릭한 좌표는 => 615, 425
# 클릭한 좌표는 => 1231, 398
# 클릭한 좌표는 => 1249, 114
region_points = {
    "region-01" : [(612, 96),(615, 425),(1231, 398),(1249, 114)]
    # 왼쪽상단, 왼쪽하단, 오른쪽하단, 오른쪽상단
}

# 3. 구역 객체 설정
region = solutions.RegionCounter(
    model="yolo11n.pt",
    show=True,
    conf=0.5,
    region=region_points
)

# 4. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    region_frame = region(frame)

# 5. 자원 해제
cap.release()
cv2.destroyAllWindows()