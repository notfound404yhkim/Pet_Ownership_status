# 🐶 2021년 전국 반려동물 보유현황 

## 📌 Project Explanation
* 2021년 전국 애완동물 보유가구 현황 데이터를 제공
* 가구별 통계 데이터를 seaborn , matplotlib 을 이용해 시각화
* csv 파일내 위도,경도 data를 입력받아 수도권 애견놀이터 맵 표시
* 애견의 사람 나이 계산 공식을 포함하여, 반려동물의 종과 나이를 입력하면 사람나이로 계산
* AWS EC2를 이용하여 서버를 관리하였습니다.
* 유지보수작업을 수월하게 하기 위해서 다른 파일에서 함수를 만들고 그 함수를 import해서 작업을 하였습니다.


## 📌Code block

# 파이 형태로 표시
```
selected_pet = str(st.selectbox('지역선택 선택', d_location))
df3= df3.loc[selected_pet,['개','고양이','기타']]
fig = plt.figure()
plt.pie(df3, labels = df3.index, autopct='%.1f',startangle=90,wedgeprops={'width':0.8})
plt.legend()
plt.title( selected_pet +' 애완동물 비율 ')
st.pyplot(fig)
```

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

# 위도 경도 지도표시
```
data = pd.read_csv('./data/mapinfo.csv')
st.map(data)
```

# 애견 나이 사람나이로 계산
```
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
```

## 📌 Screen Shot
# 데이터 분석 
![1](https://github.com/notfound404yhkim/Pet_Ownership_status/assets/151480575/47b98586-fba1-45e2-9321-a72df20ef428)
![2](https://github.com/notfound404yhkim/Pet_Ownership_status/assets/151480575/3e7abfe4-087b-4d10-a4dc-1be296f738ba)
# 상관 계수 
![3](https://github.com/notfound404yhkim/Pet_Ownership_status/assets/151480575/9551170c-2270-4834-a4ff-e06e66cf039e)
# st.map 구현
![4](https://github.com/notfound404yhkim/Pet_Ownership_status/assets/151480575/67f23790-4125-430a-9a00-218a5eac33f9)
![5](https://github.com/notfound404yhkim/Pet_Ownership_status/assets/151480575/24b77da5-364c-4f02-9d2a-960401239174)



## 📌 URL
  - http://ec2-43-201-154-87.ap-northeast-2.compute.amazonaws.com:8502/
