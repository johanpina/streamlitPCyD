import streamlit as st
from PIL import Image

# Subir una imagen
uploaded_image = st.file_uploader("Sube una imagen", type=["png", "jpg", "jpeg"])

if uploaded_image:
    # Abrir la imagen con PIL
    image = Image.open(uploaded_image)
    # Mostrar la imagen en Streamlit
    st.image(image, caption="Imagen cargada", use_column_width=True)


st.write("### Video")

# Subir un video
uploaded_video = st.file_uploader("Sube un video", type=["mp4", "mov", "avi"])

if uploaded_video is not None:
    # Mostrar el video en Streamlit
    st.video(uploaded_video)


st.write("### Audio")
# Subir un audio
uploaded_audio = st.file_uploader("Sube un archivo de audio", type=["mp3", "wav", "ogg"])

if uploaded_audio is not None:
    # Mostrar el audio en Streamlit
    st.audio(uploaded_audio)