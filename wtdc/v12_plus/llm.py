import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    api_key="",
)

answer = input("질문 :")

stream = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3.2:novita",
    messages=[
        {
            "role": "user",
            "content": answer
        }
    ],
    stream=True,
)

for chunk in stream:
    print(chunk.choices[0].delta.content, end="")

    