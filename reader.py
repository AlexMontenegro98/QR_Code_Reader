!pip3 install cv2
!pip install pyzbar
!pip install numpy

import cv2
import streamlit as st
from pyzbar.pyzbar import decode
import numpy as np

picture = st.camera_input("Take a picture")

if picture:
    bytes_data = picture.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    for i in decode(cv2_img):
        a = i.data.decode('utf-8')
        st.write(a)
