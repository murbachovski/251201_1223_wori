from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolo11n.pt")

# 2. 모델 예측
results = model(
    "251201_1223_wori-main/wtdc/v09_advanced_yolo/people.jpg",
    save=True,
    # save_txt=True,
    # save_conf=True,
    # save_crop=True,
    # classes=[56, 74],
)

# 상황 : 사람이 많이 탐지가 되고 있는데 5명만 탐지하겠다.