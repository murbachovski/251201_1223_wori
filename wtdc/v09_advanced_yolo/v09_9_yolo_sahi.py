# conda create -n sahi_py39 python=3.9
# conda activate sahi_py39
# pip install sahi

from sahi.utils.file import download_from_url
# from sahi.utils.ultralytics import download_yolo11n_model

# Download YOLO11 model
# model_path = "models/yolo11n.pt"
# download_yolo11n_model(model_path)

# Download test images
download_from_url(
    "https://raw.githubusercontent.com/obss/sahi/main/demo/demo_data/small-vehicles1.jpeg",
    "demo_data/small-vehicles1.jpeg",
)
download_from_url(
    "https://raw.githubusercontent.com/obss/sahi/main/demo/demo_data/terrain2.png",
    "demo_data/terrain2.png",
)

print("이미지 다운로드 성공!!")