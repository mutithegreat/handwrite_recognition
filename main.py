#from google.cloud import vision
import io
from google.cloud import vision
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "YOUR GOOGLE APPLICATION CREDENTIALS .json FILE"

# Google Cloud Vision istemcisi başlat
client = vision.ImageAnnotatorClient()
credantials_path = "YOUR GOOGLE APPLICATION CREDENTIALS .json FILE"


image_path = '/home/yets/Documents/handwrite_recognition/neka_1.jpeg'
with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# OCR ile metin çıkar
response = client.text_detection(image=image)
texts = response.text_annotations

# İlk metni yazdır (en kapsamlı metin)
print("Tanınan metin: ", texts[0].description)

