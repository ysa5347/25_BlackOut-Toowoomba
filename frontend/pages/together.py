import streamlit as st
from PIL import Image

st.title('동반 탑승 예시')

image = Image.open('images/together.png')
st.image(image, width=450)

col1, col2 = st.columns(2)
with col1:
    coupon_button = st.button('할인 받기')
    if coupon_button:
        # send api request to AI model
        st.write('50% 할인 쿠폰이 발급되었습니다!')

with col2:
    back_button = st.button('뒤로 가기')
    if back_button:
        st.switch_page("main_page.py")
