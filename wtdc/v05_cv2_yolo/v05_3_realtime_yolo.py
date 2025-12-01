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
    
    # 3-3. 윈도우 창 설정
    cv2.imshow("HTTPS", annotated_frame)
    
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