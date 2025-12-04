from ultralytics import solutions

inf = solutions.Inference(
    model="yolo11n.pt"
)

inf.inference()

