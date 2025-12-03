from sahi.predict import get_sliced_prediction
from sahi import AutoDetectionModel

# 1. 모델 경로 설정 및 로드
model_path = "wtdc/v09_advanced_yolo/yolo11n.pt"
detection_model = AutoDetectionModel.from_pretrained(
    model_path=model_path,
    model_type="ultralytics",
    confidence_threshold=0.4
)

# 2. 모델 예측
results = get_sliced_prediction(
    "demo_data/small-vehicles1.jpeg",
    detection_model,
    slice_height=200,
    slice_width=200,
    overlap_height_ratio=0.1,
    overlap_width_ratio=0.1
)

# 3. 모델 결과 저장
results.export_visuals(export_dir="sahi/slice")
print("모델 예측 후 결과 저장 완료!!!")