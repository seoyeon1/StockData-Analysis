from datetime import datetime #날짜와 시간을 쉽게 조작할 수 있게 하는 클래스 제공
import pandas as pd
import matplotlib.pyplot as plt
from elice_utils import EliceUtils
elice_utils = EliceUtils()



# 주식 데이터 불러오기
df = pd.read_csv('stock.csv') 
print('초기 데이터 확인')
print(df)


# 주식 데이터 전처리하기(이전 문제에서 실행했던 코드)
df['tomorrow Adj Close']= df['Adj Close'].shift(-1) # 당일 종가가 아니라 다음 날 종가를 새로운 컬럼으로 추가하기
df['Fluctuation']= df['tomorrow Adj Close'] - df['Adj Close'] # 주가 변동 데이터(다음날 종가 - 오늘 종가)
df['Fluctuation Rate']= df['Fluctuation']/df['Adj Close'] # 주가 변동률 데이터(변동 / 오늘 종가)


# 히스토그램을 이용해 분포 살펴보기
#해당 계급에 값이 얼마나 많은지 파악 가능
df['Fluctuation Rate'].plot.hist()
plt.title('Fluctuation Rate Histogram')


# 현재까지 그려진 그래프를 보여줌
plt.savefig("hist1.png")
elice_utils.send_image("hist1.png")
plt.cla() #그래프를 그린 후 초기화


# 커널 밀도함수를 이용해 분포 살펴보기
df['Fluctuation Rate'].plot.kde()
plt.title('Fluctuation Rate KDE plot')


# 현재까지 그려진 그래프를 보여줌
plt.savefig("hist1.png")
elice_utils.send_image("hist1.png")#주가 데이터가 0에 가장 가까운 것=변동성이 적은 주식