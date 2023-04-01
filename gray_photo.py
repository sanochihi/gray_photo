import streamlit as st
from PIL import Image

st.title("写真を白黒にするページ")

uploaded_image = st.file_uploader("写真をアップロードする", type=['png','jpg'])

if uploaded_image:

    # Create a pillow image instance
    img_upl = Image.open(uploaded_image)

    # Convert the pillow image to grayscale
    gray_img_upl = img_upl.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_img_upl)

with st.expander("Webカメラで撮影した写真を白黒にする"):

    # Start the camera
    camera_image = st.camera_input("Take Photo を押してね。撮った写真を白黒にするよ。")

if camera_image:

    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_img)