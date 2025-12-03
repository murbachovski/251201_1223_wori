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

# 탐지 모델 학습
# 1. 기획 => 눈, 코, 입 중 한 가지
# 2. 데이터 수집 => 총 100장
# 3. 데이터 전처리 => YOLO 내장 전처리 사용 가능
# 4. 데이터 라벨링 => Labelimg 또는 Roboflow 이용
# 5. 모델 학습
# 6. 모델 배포