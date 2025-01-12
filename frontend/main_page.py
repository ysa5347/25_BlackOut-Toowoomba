import streamlit as st
from PIL import Image

st.title('GCOO Main Page')

image = Image.open('images/main_screen.png')
st.image(image, width=270)

col1, col2, col3, col4 = st.columns(4)
with col1:
    screen1_button = st.button('주차')
    if screen1_button:
        st.switch_page("pages/parking.py")

with col2:
    screen2_button = st.button('선행')
    if screen2_button:
        st.switch_page("pages/good_behavior.py")

with col3:
    screen3_button = st.button('안전')
    if screen3_button:
        st.switch_page("pages/safety.py")

with col4:
    screen4_button = st.button('동반 운전')
    if screen4_button:
        st.switch_page("pages/together.py")