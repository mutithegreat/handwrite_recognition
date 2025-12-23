from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests
import cv2
import os   

file_path = os.path.join("data", "1.jpeg")
# Örnek: OpenCV ile okuma
image = cv2.imread(file_path)
# veya Google Vision için:
with open(file_path, "rb") as image_file:
    content = image_file.read()
# load image from the IAM database
image = Image.open(file_path).convert("RGB")

processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')
pixel_values = processor(images=image, return_tensors="pt").pixel_values

generated_ids = model.generate(pixel_values)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]