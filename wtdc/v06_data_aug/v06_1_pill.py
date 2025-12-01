from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# 1. 이미지 로드
img = Image.open("v06_data_aug/input.jpg")

# 2. 이미지 조정(회전)
img_rotated = img.rotate(90)

# 2-1. 이미지 조정(밝기)
enhancer = ImageEnhance.Brightness(img)
img_brightness = enhancer.enhance(0.5)

# 3. 시각화 틀 만들어주기
fig, ax = plt.subplots(2, 3, figsize=(20, 10))

# 3-1. 원본 이미지 시각화
ax[0,0].imshow(img)
ax[0,0].axis('off')
ax[0,0].set_title("ORG")

# 3-2. 회전 이미지 시각화
ax[0,1].imshow(img_rotated)
ax[0,1].axis('on')
ax[0,1].set_title("ROTATE")

# 3-3. 밝기 이미지 시각화
ax[0,2].imshow(img_brightness)
ax[0,2].axis('off')
ax[0,2].set_title("BRIGHT")

# 3-3. 결과 시각화
plt.show()

# 4. 결과 이미지 저장
img_brightness.save("./img_rotated.jpg")
print("이미지 저장 완료!!!")