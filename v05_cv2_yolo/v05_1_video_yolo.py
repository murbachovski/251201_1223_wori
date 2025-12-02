from ultralytics import YOLO
import cv2

# 1. 비디오 경로 설정
video_path = "v05_cv2_yolo/input.mp4"
cap = cv2.VideoCapture(video_path)

# 2. 모델 로드
model = YOLO("yolo11n.pt")

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        print("비디오를 못 읽습니다.")
        break
    
    # 4. YOLO 객체 탐지 수행
    results = model(frame)
    
    # 5. 탐지 결과 표시
    annotated_frame = results[0].plot()

    # 6. 영상 결과 출력
    cv2.namedWindow("YOLO", cv2.WINDOW_NORMAL)
    cv2.imshow("YOLO", annotated_frame)
    
    # 7. 'q'키를 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q키를 눌러서 종료합니다.")
        break
    
# 8. 자원 해제
cap.release()
cv2.destroyAllWindows()