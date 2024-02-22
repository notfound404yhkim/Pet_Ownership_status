# 🐶 2021년 전국 반려동물 보유현황 

## 📌 Project Explanation
* 2021년 전국 애완동물 보유가구 현황 데이터를 제공
* 가구별 통계 데이터를 seaborn , matplotlib 을 이용해 시각화
* csv 파일내 위도,경도 data를 입력받아 수도권 애견놀이터 맵 표시
* 애견의 사람 나이 계산 공식을 포함하여, 반려동물의 종과 나이를 입력하면 사람나이로 계산
* AWS EC2를 이용하여 서버를 관리하였습니다.
* 유지보수작업을 수월하게 하기 위해서 다른 파일에서 함수를 만들고 그 함수를 import해서 작업을 하였습니다.


## 📌Code block

# 선택한 컬럼의 상관계수
```
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
```



  

## 📌 URL
  - http://ec2-43-201-154-87.ap-northeast-2.compute.amazonaws.com:8502/
