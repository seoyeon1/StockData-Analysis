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


# 변동률의 시각화
plt.figure(figsize=(12,8)) # 표현할 그래프의 크기 설정
plt.plot(df.index, df['Fluctuation Rate']) # 변동률 데이터 시각화.x축:df.index
plt.axhline( y = 0, color = 'red', ls = '--') # y축:변동률. 변동률 폭을 관찰하기 위한 기준 수평선 추가


# 시각화 옵션 코드
# (시각화 강의에서 별도로 다루는 내용입니다)
plt.legend(loc='best')
plt.grid()
plt.savefig("plot3.png")#시계열 데이터(Time Serise Data)
elice_utils.send_image("plot3.png")