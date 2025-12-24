#from google.cloud import vision
import io
import os
from google.cloud import vision
from pathlib import Path

base_path = Path().cwd()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(base_path / "versatile-brace-473413-r9-42c643e702d2.json")
dir_data = Path("data")
client = vision.ImageAnnotatorClient()
credantials_path = base_path / "versatile-brace-473413-r9-42c643e702d2.json"
file_name = "captured_image.jpeg"

def get_image(dir_data,file_name):
    file_path = Path(dir_data) / file_name
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()
    return content

def recognize_text(content):
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts
    
def get_texts_from_images(dir_data,file_name):
    content = get_image(dir_data, file_name)
    texts = recognize_text(content)
    
    if texts and len(texts) > 0:
        lines = texts[0].description.split('\n')
        tarih = lines[0] if len(lines) > 0 else ""
        saat = lines[1] if len(lines) > 1 else ""
        firma = lines[2] if len(lines) > 2 else ""
        plaka = lines[3] if len(lines) > 3 else ""
        aciklama = lines[4] if len(lines) > 4 else ""
        aciklama2 = lines[5] if len(lines) > 5 else ""
        aciklama3 = lines[6] if len(lines) > 6 else ""
        dosya_no = lines[7] if len(lines) > 7 else ""
        telefon = lines[8] if len(lines) > 8 else ""
    
    return tarih, saat, firma, plaka, aciklama, aciklama2, aciklama3, dosya_no, telefon

liste = get_texts_from_images(dir_data,file_name)
