import time

import streamlit as st
from PIL import Image

st.title('주차 예시')

image = Image.open('images/parking.png')
st.image(image, width=270)

# put a button in the app
col1, col2 = st.columns(2)
with col1:
    picture_button = st.button('사진 촬영')
    if picture_button:
        # send api request to AI model
        st.write('Sending to AI model...')
        time.sleep(3)
        st.write('AI model response: 사진 전송 완료')

with col2:
    back_button = st.button('뒤로 가기')
    if back_button:
        st.switch_page("main_page.py")
