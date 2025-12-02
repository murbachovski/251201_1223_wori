import cv2
import matplotlib.pyplot as plt

# 1. 이미지 로드
img = cv2.imread("v06_data_aug/input.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 2. 이미지 조정
img_flipped = cv2.flip(img, 1) # 1은 수평, 0은 수직, -1은 둘 다

# 3. 이미지 시각화
fig, ax = plt.subplots(2, 2, figsize=(10, 5))

ax[0,0].imshow(img)
ax[0,0].axis("off")
ax[0,0].set_title("ORG")

ax[0,1].imshow(img_flipped)
ax[0,1].axis("off")
ax[0,1].set_title("FLIP")

# plt.show()

# 4. 이미지 저장
cv2.imwrite("./img_flipped.jpg", img_flipped)
print("이미지 저장 성공!!!")
# 이미지 저장 성공!!!