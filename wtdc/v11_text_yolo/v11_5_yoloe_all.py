from ultralytics import YOLOE

# 모델 로드
model = YOLOE("yoloe-11l-seg-pf.pt")

# 모델 추론
results = model.predict("wtdc/v11_text_yolo/tomato.jpg")

# 결과 확인
results[0].save("./output_YOLOE_tomato.jpg")