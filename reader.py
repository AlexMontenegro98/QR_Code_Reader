import streamlit as st
import cv2
import numpy as np

def decode(im) : 
    # Find QR code
    decodedObjects = cv2.QRCodeDetector().detectAndDecode(im)
    
    # If there's a QR code in the image, display the decoded message
    if decodedObjects[0] :
        print("QR code detected, data:", decodedObjects[1])
        st.write("QR code detected, data:", decodedObjects[1])
    else:
        print("QR code not detected")
        st.write("QR code not detected")

# Load image
#im = cv2.imread(r"C:\Python\Ready_Codes\nota_fiscal\notafis.jpg")
picture = st.camera_input("Take a picture")
if picture:
    bytes_data = picture.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

# Decode QR code
decode(cv2_img)
