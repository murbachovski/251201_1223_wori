from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolo11n-cls.pt")

# 2. 모델 예측
results = model(
    "251201_1223_wori-main/wtdc/v09_advanced_yolo/image.png",
    save=True
)