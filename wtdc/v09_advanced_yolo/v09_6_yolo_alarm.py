from ultralytics import solutions
import cv2
# from v08_openapi.v08_3_cctv_its import its_cctv

# 1. 비디오 경로 설정(its cctv 사용)
# cctv_url = its_cctv(cctv_number=90)
# print(cctv_url)
# cap = cv2.VideoCapture(cctv_url)

# 1. 비디오 경로 설정(경찰청 cctv 사용)
cap = cv2.VideoCapture("https://strm1.spatic.go.kr/live/28.stream/playlist.m3u8")

# 2. 이메일 인증 정보
from_email = "ai.murbachovski@gmail.com"
passwoard = "gfbf ovvy fjgg came"
to_email = "ai.murbachovski@gmail.com"

# 3. 보안 알림 시스템 객체 생성
security = solutions.SecurityAlarm(
    model="yolo11n.pt",
    show=True,
    records=1 # 탐지된 객체 수가 reocrds 수 이상일때 이메일 전송함!!
)

# 4. 이메일 인증
security.authenticate(from_email, passwoard, to_email)

# 5. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("비디오 못 읽었어요.")
        break

    # 5-1. 객체탐지 수행
    results_frame = security(frame)

    # 5-2. q 키를 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 6. 자원 해제
cap.release()
cv2.destroyAllWindows()

# 이메일 알람 문구 변경 => 탐지된 객체 수 작성
# 예) 객체가 3명 탐지됐습니다.