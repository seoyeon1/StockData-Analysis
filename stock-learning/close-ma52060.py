from datetime import datetime #날짜와 시간을 쉽게 조작할 수 있게 하는 클래스 제공
import pandas as pd
import matplotlib.pyplot as plt
from elice_utils import EliceUtils
elice_utils = EliceUtils()

#주가, 이동 평균선 시각화하기

# 주식 데이터 불러오기
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


# 이동평균선 시각화. plot을 여러번 하면 여러가지 그래프가 겹쳐서 보임
plt.plot(df['Adj Close'], label="Adj Close") # 수정 종가
plt.plot(df['MA5'], label="MA5") # 종가 5일 이동평균
plt.plot(df['MA20'], label="MA20") # 종가 20일 이동평균
plt.plot(df['MA60'], label="MA60") # 종가 60일 이동평균


# 시각화 옵션 코드
# (시각화 강의에서 별도로 다루는 내용입니다)
plt.legend(loc='best')
plt.grid()
plt.savefig("plot2.png")
elice_utils.send_image("plot2.png")
#상승세:단기이동평균선이 장기이동평균선보다 높음