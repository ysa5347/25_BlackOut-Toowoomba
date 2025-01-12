import time

import streamlit as st
from PIL import Image

st.title('선행 예시')

if 'image_path' not in st.session_state:
    st.session_state['image_path'] = 'images/good_behavior1.png'

image = Image.open(st.session_state['image_path'])
st.image(image, width=270)

# put a button in the app
col1, col2, col3 = st.columns(3)
with col1:
    getup_button = st.button('일으켜 세우기')
    if getup_button:
        st.session_state['image_path'] = 'images/good_behavior2.png'
        st.rerun()

with col2:
    picture_button = st.button('사진 촬영')
    if picture_button:
        # send api request to AI model
        st.write('Sending to Server...')
        time.sleep(3)
        st.write('선행 완료!\n쿠폰함을 확인하세요~')

with col3:
    back_button = st.button('뒤로 가기')
    if back_button:
        st.switch_page("main_page.py")