import pytesseract
from PIL import Image
from PIL import ImageEnhance

"""
unset DYLD_LIBRARY_PATH
"""
# 打开图片
img = Image.open("img_1.png")

# 进行文字识别
text = pytesseract.image_to_string(img, lang='chi_sim')

# 打印识别结果
print("识别结果：", text)


# 增强图片对比度
enhancer = ImageEnhance.Contrast(img)
img_contrast = enhancer.enhance(2.0)

# 进行文字识别
text_contrast = pytesseract.image_to_string(img_contrast)

# 打印识别结果
print("增强对比度后的识别结果：", text_contrast)
