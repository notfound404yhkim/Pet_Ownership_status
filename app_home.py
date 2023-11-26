import streamlit as st

def run_home_app():
    st.subheader('Welcome~~')
    st.text('이 앱은 고객 데이터 와 자동차 구매 데이터에 대한 내용입니다.')
    st.text('고객 정보를 넣으면, 차 구매 금액도 예측해 줍니다.')

    st.text('AWS에 배포까지 된 앱 입니다.')

    img_url = 'https://m.kbchachacha.com/images/cm/theme-hybrid.png'
    st.image(img_url)