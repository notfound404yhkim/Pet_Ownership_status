import streamlit as st

def run_home_app():
    st.subheader('Welcome~~')

    st.text('이 앱은 전국 애완동물 보유가구 현황에 대한 내용입니다.')
    
    st.text('AWS에 배포까지 된 앱 입니다.')

    img_url = 'https://www.nhis.or.kr/magazin/174/html/style/images/sub7_img2.jpg'
    st.image(img_url)