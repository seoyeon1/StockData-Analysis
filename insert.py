from datetime import datetime #날짜와 시간을 쉽게 조작할 수 있게 하는 클래스 제공
import pandas as pd
import matplotlib.pyplot as plt
from elice_utils import EliceUtils
pd.set_option('display.max_columns', None)
elice_utils = EliceUtils()


# 주식 데이터 불러오기
df = pd.read_csv('stock.csv') 


# 수정 종가 이동평균(MA: Moving Average) 값 구하기
ma5 = df['Adj Close'].rolling(window=5).mean() # 수정 종가 5일 이동평균
ma20 = df['Adj Close'].rolling(window=20).mean() # 수정 종가 20일 이동평균
ma60 = df['Adj Close'].rolling(window=60).mean() # 수정 종가 60일 이동평균


# 이동평균 값 추가하기
df.insert(len(df.columns), "MA5", ma5) # 'MA5'라는 열 이름으로 ma5 값 추가
df.insert(len(df.columns), "MA20", ma20) # 'MA20'라는 열 이름으로 ma20 값 추가
df.insert(len(df.columns), "MA60", ma60) # 'MA60'라는 열 이름으로 ma60 값 추가


# 거래량 5일 이동평균 추가(.insert())   #4일차부터 확인 가능. 그 전에는 NaN
vma5 = df['Volume'].rolling(window=5).mean() # 거래량의 5일 이동평균 구하기
df.insert(len(df.columns), "VMA5", vma5) # 'VMA5'라는 열 이름으로 vma5 값 추가


# --- 이격도 추가 --- #
# 수정 종가 데이터를 5일 이동평균 값으로 나눈 비율
disp5 = (df['Adj Close']/df['MA5'])*100

# 이격도 데이터를 'Disp5'라는 열 이름으로 추가
df.insert(len(df.columns), "Disp5", disp5) 



# 데이터 확인
print('이동평균 및 이격도가 추가된 주가 데이터')
print(df)

#NaN : 값이 정해지지 않았다