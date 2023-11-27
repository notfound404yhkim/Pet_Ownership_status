import streamlit as st
from app_home import run_home_app
from streamlit_option_menu import option_menu
from app_eda import run_eda_app
from app_ml import run_ml_app
from PIL import Image


def main():
    st.title('2021년 애완동물 보유가구 현황')

    menu = [ '홈','분석','with pet']
    with st.sidebar:

        img = Image.open('./data/image1.PNG')
        st.image(img)

        #choice = st.sidebar.selectbox('메뉴',menu)
        choice = option_menu("메뉴", menu,
                            icons=['house', 'bar-chart', 'camera-fill'],
                            menu_icon="bi bi-menu-up", default_index=0,
                            styles={
                            # default_index = 처음에 보여줄 페이지 인덱스 번호
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }) # css 설정

    if choice == menu[0]:
        run_home_app()
    elif choice == menu[1]:
        run_eda_app()
    elif choice == menu[2]:
        run_ml_app()


if __name__ == '__main__':
    main()


