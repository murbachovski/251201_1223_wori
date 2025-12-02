from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolo11n.pt")

# 2. 모델 예측
results = model(
    "251201_1223_wori-main/wtdc/v09_advanced_yolo/class.jpg",
    save=True,
    save_txt=True,
    save_conf=True,
    save_crop=True,
    classes=[56, 74],
)

# clock, chair만 탐지되도록!