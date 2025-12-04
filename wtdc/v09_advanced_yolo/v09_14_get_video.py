import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("wtdc/v09_advanced_yolo/inout.mp4")
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# 2. 마우스 이벤트 처리 콜백 함수 정의
points = []
def mouse_callback(event, x, y, flags, param):
    """
    마우스 이벤트 발생 시 호출되는 함수

    매개변수 :
    - event : 발생한 마우스 이벤트 종류
    - x, y : 이벤트 발생 위치의 좌표(픽셀 기준)
    - flags : 이벤트 관련 추가 플래그
    - param : 콜백 함수에 추가 전달된 파라미터
    """

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"클릭한 좌표는 => {x}, {y}")

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    cv2.imshow("GET_VIDEO_X_Y", frame)
    cv2.setMouseCallback("GET_VIDEO_X_Y", mouse_callback)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()