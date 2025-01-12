import time

import streamlit as st
from PIL import Image

st.title('안전 측정 예시')

# 상세 보기 버튼 안보이게 초기화
if 'show_more_button' not in st.session_state:
    st.session_state.show_more_button = False

if 'image_path' not in st.session_state:
    st.session_state['image_path'] = 'images/safety.png'

image = Image.open(st.session_state['image_path'])
st.image(image, width=270)

# put a button in the app
col1, col2, col3 = st.columns(3)
with col1:
    picture_button = st.button('반납하기')
    if picture_button:
        st.write('반납 중...')
        time.sleep(3)
        st.write('반납 완료.')
        st.session_state.show_more_button = True

        # feedback
        st.session_state['image_path'] = 'images/feedback.png'
        st.rerun()

with col2:
    if st.session_state.show_more_button:
        show_more_button = st.button('상세 보기')
        if show_more_button:
            st.session_state['image_path'] = 'images/analysis.png'
            st.rerun()

with col3:
    back_button = st.button('뒤로 가기')
    if back_button:
        st.switch_page("main_page.py")
