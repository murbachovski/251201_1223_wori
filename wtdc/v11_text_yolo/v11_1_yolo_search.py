from ultralytics import solutions

app = solutions.SearchApp(
    # data="" # 커스텀 폴더 경로
    device="cpu"
)

app.run(debug=True)

# pip install flask
# git clone clip github
# pip install tqdm
# pip install ftfy
# pip install regex
# pip install faiss-cpu
# pip install flask tqdm ftfy regex faiss-cpu