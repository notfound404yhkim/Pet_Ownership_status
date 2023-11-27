import streamlit as st
import numpy as np
from PIL import Image
import pandas as pd 


def run_ml_app():
    st.subheader('반려동물과 함께 추천여행지')
    img = Image.open('./data/travel.PNG')
    st.image(img)

    ## 위도와 경도 값을 가진 샘플 DataFrame 생성
    # data = pd.DataFrame({
    #     'latitude': [37.4559],
    #     'longitude': [126.752]
    # })
    st.subheader('수도권 놀이터 맵')
    data = pd.read_csv('./data/mapinfo.csv')
    
    
    ## 데이터를 사용하여 지도 생성
    st.map(data)
    img_url2 = 'https://preview.clipartkorea.co.kr/2014/01/31/yaytg269370.jpg'
    st.image(img_url2)
    
    st.subheader('애견 사람 나이 계산기')
    
    type = ['소형견','중형견','대형견']
    my_choice = st.selectbox('강아지가 어디에 속하나요?', type)
    birth_year = st.number_input( '강아지가 몇살인가요?', 1, 20 ) #레이블, 최소값,최대값
    
    if st.button('사람 나이 계산'):
        if birth_year <= 2:
            st.text('2살전 까지는 동일합니다.') 
            st.subheader(' 1살 : 16살 ')
            st.subheader(' 2년 : 24살 ')

        else :
            if my_choice == '소형견':
                diff = (birth_year-2)*5
                result = 24 + diff
                print(result)
            elif my_choice == '중형견':
                diff = (birth_year-2)*6
                result = 24 + diff
                print(result)
            elif my_choice == '대형견':
                diff = (birth_year-2)*7
                result = 24 + diff
                print(result)

            st.subheader(' 사람 나이로 계산하면 ' + str(result) + '살 입니다.')