from sahi.predict import get_prediction
from sahi import AutoDetectionModel

# 1. 모델 경로 설정 및 로드
model_path = "wtdc/v09_advanced_yolo/yolo11n.pt"
detection_model = AutoDetectionModel.from_pretrained(
    model_path=model_path,
    model_type="ultralytics"
)

# 2. 모델 예측
results = get_prediction(
    "demo_data/small-vehicles1.jpeg",
    detection_model
)

# 3. 모델 결과 저장
results.export_visuals(export_dir="sahi/default")
print("모델 예측 후 저장 완료")