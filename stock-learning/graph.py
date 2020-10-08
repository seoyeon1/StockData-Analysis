from datetime import datetime #날짜와 시간을 쉽게 조작할 수 있게 하는 클래스 제공
import pandas as pd
import matplotlib.pyplot as plt
from elice_utils import EliceUtils
elice_utils = EliceUtils()


# 주식 데이터 불러오기:[105 rows x 7 columns]
df = pd.read_csv('stock.csv') 
print('초기 데이터 확인')
print(df)


# 주식 데이터 전처리하기(이전 문제에서 실행했던 코드)
ma5 = df['Adj Close'].rolling(window=5).mean()
ma20 = df['Adj Close'].rolling(window=20).mean()
ma60 = df['Adj Close'].rolling(window=60).mean()

df.insert(len(df.columns), "MA5", ma5)
df.insert(len(df.columns), "MA20", ma20)
df.insert(len(df.columns), "MA60", ma60)

vma5 = df['Volume'].rolling(window=5).mean()
df.insert(len(df.columns), "VMA5", vma5)


# 이동평균선의 시각화
plt.plot(df.index, df['MA5'], label = "MA5") # 이동평균선 시각화 index:x축, 범례:ma5
plt.plot(df.index, df['Adj Close'], label='Adj Close') # 수정 종가 시각화


# 시각화 옵션(graph) 코드
# (시각화 강의에서 별도로 다루는 내용입니다)
plt.legend(loc='best')
plt.xticks(rotation = 45)
plt.grid()
plt.savefig("plot.png")
elice_utils.send_image("plot.png")#추세:우상향 그래프