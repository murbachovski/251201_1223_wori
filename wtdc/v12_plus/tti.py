# 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
import os
from huggingface_hub import InferenceClient

print("TTI START")


client = InferenceClient(
    provider="auto",
    api_key="",
)

answer = input("생성할 이미지를 설명해주세요. : ")

# output is a PIL.Image object
image = client.text_to_image(
    answer,
    model="black-forest-labs/FLUX.1-dev",
)

image.save("tti_image.jpg")
print("전체 코드가 잘 실행되었음!!")

# pip install huggingface_hub