import pytesseract
from PIL import Image
import streamlit as st

import numpy as np
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

# img_file_buffer = st.file_uploader(
#     "Upload an image", type=["png", "jpg", "jpeg"])


# # image = Image.open('image.jpg')
# # img_array = np.array(image)

# if image is not None:
#     image = Image.open(img_file_buffer)
#     st.image(
#         image,

#         use_column_width=True,
#     )


img_file_buffer = st.file_uploader("Upload an image")
if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    img_array = np.array(image)  # if you want to pass it to OpenCV
    st.image(image, caption="The caption", use_column_width=True)
    text = pytesseract.image_to_string(image, config=r' — oem 3 — psm 6')
    st.write(text)

# im = Image.open('image.jpg')

# print(text)
