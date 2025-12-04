from ultralytics import FastSAM
import cv2

# 이미지 경로 설정
source = "wtdc/v11_text_yolo/fastsam3.jpg"

# FastSAM 모델 로드
model = FastSAM("FastSAM-s.pt")

# 모델 추론
results = model(source, texts="yllow car")

# 시각화 이미지
output_image = results[0].plot()

# 결과 이미지 저장
cv2.imwrite("output_result.jpg", output_image)
print("결과가 잘 저장됐습니다.")
