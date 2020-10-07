import pandas as pd#.loc[] 을 활용한 데이터 추출

# 코로나 데이터를 불러옵니다.
data_path = '#'
corona_data = pd.read_excel(data_path)

# .loc을 활용하여 7월 30일('2020-07-30')의 사망자 데이터를 추출해봅니다.
#데이터의 특정 부분을 가져올 때 : .loc[행 지정, 열 지정]
death_0730 = corona_data.loc[corona_data['날짜']=='2020-07-30', '사망자']
print(death_0730)