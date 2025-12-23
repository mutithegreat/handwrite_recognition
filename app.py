import os
import streamlit as st
import pandas as pd
from main import recognize_text , file_name , get_texts_from_images
import cv2
from pathlib import Path
cap = cv2.VideoCapture(0)
enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)
    save_path = Path.cwd() / "data" / "captured_image.jpeg"
    with open(save_path, "wb") as f:
        f.write(picture.getvalue())


header = st.container()
image = st.container()
texts = st.container()

st.write("**Resimden Tanınan Metinler**")
tarih, saat, firma, plaka, aciklama, aciklama2, aciklama3, dosya_no, telefon = get_texts_from_images("data", file_name)

col1, col2 , col3= st.columns(3)
with col1:
    st.write(file_name)
    st.image(os.path.join("data", file_name), use_container_width=True)
    
with col2:
    st.write("Data from Image")
    tarih_text = st.text_area("Tarih", value=tarih, height=68)
    firma_text = st.text_area("Firma", value=firma, height=68)
    aciklama_text = st.text_area("Açıklama", value=aciklama, height=68)
    aciklama3_text = st.text_area("Açıklama 3", value=aciklama3, height=68)
    telefon_text = st.text_area("Telefon", value=telefon, height=68)
    
with col3:
    st.write("Data from Image")
    saat_text = st.text_area("Saat", value=saat, height=68)
    plaka_text = st.text_area("Plaka", value=plaka, height=68)
    aciklama2_text = st.text_area("Açıklama 2", value=aciklama2, height=68)
    dosya_no_text = st.text_area("Dosya No", value=dosya_no, height=68)
    