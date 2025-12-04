from ultralytics import YOLOWorld

# 1. 모델로드
model = YOLOWorld("yolov8s-world.pt")

# 2. 탐지 클래스 설정
model.set_classes(["pink"])

# 3. 모델 예측
results = model.predict("wtdc/v11_text_yolo/fastsam2.jpg")

# 4. 시각화
results[0].save("./output.jpg")

# results[0].show()
# for result in results:
#     result.show()  # Display all results