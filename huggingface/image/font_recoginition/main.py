# method 1
# Use a pipeline as a high-level helper
# from transformers import pipeline
#
# pipe = pipeline("image-classification", model="microsoft/resnet-50")


# method 2
# Load model directly
from transformers import AutoImageProcessor, AutoModelForImageClassification

processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
model = AutoModelForImageClassification.from_pretrained("microsoft/resnet-50")