"""
文本识别

brew install tesseract

tesseract官网：https://tesseract-ocr.github.io/tessdoc/

安装：https://tesseract-ocr.github.io/tessdoc/Installation.html

python安装：pip install pytesseract

unset DYLD_LIBRARY_PATH

tesseract --version

"""

# 导入一些需要的包
import cv2
import pytesseract

# 设置Tesseract OCR引擎路径
# pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'/opt/local/bin/tesseract'

# 加载一张图片
img = cv2.imread(r'img_2.png')


# 识别文字
# text = pytesseract.image_to_string(img, lang="chi_sim")  # 指定语言
text = pytesseract.image_to_string(img, lang='eng')

print(text)