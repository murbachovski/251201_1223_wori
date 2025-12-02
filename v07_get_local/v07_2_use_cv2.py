import cv2
import os
from datetime import datetime


def capture_image():
    # 1. 저장 디렉토리 설정
    save_dir  = "./captured_images"
    os.makedirs(save_dir, exist_ok=True)

    # 2. 카메라 연결
    cap = cv2.VideoCapture(0)

    # 3. 프레임 처리
    if cap.isOpened():
        success, frame = cap.read()
        if success:
            print("성공적으로 프레임 읽음")
            
            # 3-1. 이미지 수집
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = os.path.join(save_dir, f"capture_{timestamp}.jpg")
            cv2.imwrite(file_path, frame)
            print("사진 저장 성공!")

    # 4. 자원 해제
    cap.release()
    cv2.destroyAllWindows()

# 위 코드를 함수화해서 사용해보기
capture_image()