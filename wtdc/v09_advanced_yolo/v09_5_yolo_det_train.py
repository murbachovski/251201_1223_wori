from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolo11n.pt")

# 2. 모델 훈련
model.train(
    data="coco8.yaml", # 훈련 데이터셋 경로
    epochs=10, # 훈련 횟수
    batch=16, # 훈련 횟수 안의 이미지 수
    imgsz=320, # 이미지 사이즈
)

# train | val | test
# 학습  | 검증 | 시험
    # 최소 클래스 별 총 100장 이상
        # 학습 60
        # 검증 30
        # 시험 10

# 