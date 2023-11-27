import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb 

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


def run_eda_app():
    img_url = 'https://d2k6w3n3qf94c4.cloudfront.net/media/test/main_image/blind-dog-2-1024x683.jpg'
    st.image(img_url)
    
    st.subheader('데이터 분석')

    st.subheader('전체 데이터 프레임 확인하기')
    df = pd.read_csv('./data/2021_Owning_Pets.csv',encoding = 'euc-kr')
    df2 = df[(df['거처의 종류별'] == '계' ) & (df['행정구역별(시도)'] != '전국' )] #전국 데이터 제외
    df3 =df2.set_index('행정구역별(시도)') #지역을 인덱스화 
    
    st.dataframe(df)
    
    st.subheader('기초 통계 데이터 확인')
    if st.checkbox('통계 데이터보기'):
        st.dataframe(df.describe())
    else :
        st.text('')

    st.subheader('최다 / 최소 데이터 확인')
    column_list = df2.columns[5 : -1]
    selected_column = st.selectbox('애완동물을 선택하세요.',column_list)

    st.text(selected_column + '를 키우는 가구가 제일 적은 지역')
    st.dataframe(df2.loc[ df2[selected_column] == df2[selected_column].min(),['행정구역별(시도)',selected_column ]])
    st.text(selected_column + '를 키우는 가구가 제일 많은 지역')
    st.dataframe(df2.loc[ df2[selected_column] == df2[selected_column].max(),['행정구역별(시도)',selected_column ]])


##############
    st.subheader('애완동물 별 데이터 확인하기')
    selected_column2 = st.selectbox('애완동물을 선택하세요',column_list)
    ylabel = selected_column2

    fig = plt.figure(figsize=(8,5))
    plt.title( '지역별 애완동물 보유 가구 데이터' )
    plt.xticks(rotation = 45)
    plt.xlabel('지역' )
    plt.ylabel('가구')
    plt.plot( df3[ylabel] )
    st.pyplot(fig)

##############

    st.subheader('파이 형태로 비율 확인')
    selected =  st.radio('정렬을 선택하세요',options=['반려동물 비율보기','반려동물 보유율보기'])
    
    # df의 petal_length 컬럼을 정렬하도록한다.
    if selected == '반려동물 비율보기':
        d_location = df2['행정구역별(시도)'].unique()
        st.subheader('반려동물 비율')
        selected_pet = str(st.selectbox('지역선택 선택', d_location))
        df3= df3.loc[selected_pet,['개','고양이','기타']]
        fig = plt.figure()
        plt.pie(df3, labels = df3.index, autopct='%.1f',startangle=90,wedgeprops={'width':0.8})
        plt.legend()
        plt.title( selected_pet +' 애완동물 비율 ')
        st.pyplot(fig)

    elif selected =='반려동물 보유율보기':
        d_location = df2['행정구역별(시도)'].unique()
        st.subheader('반려동물보유가구 비율')
        selected_pet = str(st.selectbox('지역선택 선택', d_location))
        df3= df3.loc[selected_pet,['반려동물보유가구-계','반려동물미보유가구-계']]
        fig = plt.figure()
        plt.pie(df3, labels = df3.index, autopct='%.1f',startangle=90,wedgeprops={'width':0.8})
        plt.legend()
        plt.title( selected_pet +'반려동물보유가구 비율 ')
        st.pyplot(fig)


###############################

    st.subheader('상관 관계 보기')

    if st.checkbox('상관 관계 데이터 보기'):
            
            selected_list = st.multiselect('두개의 컬럼을 선택하세요.' ,df.columns[:], max_selections=2)  

            #두개일때만 차트 그리기 
            if len(selected_list) == 2:
                fig = plt.figure()
                plt.scatter(data = df2, x= selected_list[0], y= selected_list[1])
                plt.title( selected_list[0] + ' VS ' + selected_list[1])
                plt.xlabel(selected_list[0])
                plt.ylabel(selected_list[1])
                st.pyplot(fig)

                fig = plt.figure()
                st.text('상관 계수')
                st.dataframe(df2[selected_list].corr())
                st.pyplot(fig)

            else:
                st.text('')
        
   


    



    
 