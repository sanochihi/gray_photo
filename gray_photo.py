import streamlit as st
from PIL import Image

with st.expander("白黒写真の撮影"):

    # Start the camera
    camera_image = st.camera_input("Take Photo を押してね。撮った写真を白黒にするよ。")

if camera_image:

    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_img)