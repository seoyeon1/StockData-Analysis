import pandas as pd#.loc[] 을 활용한 조건 데이터 추출

# 코로나 데이터를 불러옵니다.
data_path = '#'
corona_data = pd.read_excel(data_path)

# 확진자가 10000명 이상인 시점부터의 모든 데이터를 추출합니다.
confirmed_10000 = corona_data.loc[ corona_data["확진자"]>= 10000]#[ corona_data["확진자"]>= 10000, :] 같은 의미.
# 행 조건 : 가격 열의 값이 100 이상인 조건을 지정, 해당 조건에 맞는 행들만 가져옴. 열 조건에 있는 :(콜론)은 모든 값을 가져온다는 뜻

print(confirmed_10000)