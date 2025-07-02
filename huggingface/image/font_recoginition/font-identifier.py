# Use a pipeline as a high-level helper
# 识别字体类型，不包含大小
from transformers import pipeline

pipe = pipeline("image-classification", model="gaborcselle/font-identifier")

result = pipe("test.png")
print(result)
