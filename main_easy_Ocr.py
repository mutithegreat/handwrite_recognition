#from google.cloud import vision
import io
from google.cloud import vision
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/yets/Documents/handwrite_recognition/versatile-brace-473413-r9-42c643e702d2.json"

# Google Cloud Vision istemcisi başlat
client = vision.ImageAnnotatorClient()
credantials_path = "/home/yets/Documents/handwrite_recognition/versatile-brace-473413-r9-42c643e702d2.json"


image_path = '/home/yets/Documents/handwrite_recognition/neka_1.jpeg'
with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# OCR ile metin çıkar
response = client.text_detection(image=image)
texts = response.text_annotations

# İlk metni yazdır (en kapsamlı metin)
print("Tanınan metin: ", texts[0].description)
