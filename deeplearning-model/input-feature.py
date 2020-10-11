from datetime import datetime #날짜와 시간을 쉽게 조작할 수 있게 하는 클래스 제공
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Dense, Activation
from elice_utils import EliceUtils
elice_utils = EliceUtils()


#딥러닝을 통해 주식 가격 예측하기
#model 만들기
# 주식 데이터 불러오기
df = pd.read_csv('stock.csv') 
print('주식 데이터 확인하기')
print(df)


#피쳐 엔지니어링:기존의 값들을 가공해서 새로운 피쳐를 만드는 것
#딥러닝 전처리 과정 & 매우 중요한 부분
#입력피쳐:고가, 저가
# 주가의 중간값 계산하기

high_prices = df['High'].values # 고가
low_prices = df['Low'].values # 저가
mid_prices = (high_prices + low_prices) / 2 # 고가와 저가의 중간값
print('주가의 중간값:', mid_prices)


# 주가 데이터에 중간 값 요소 추가하기
df['Mid'] = mid_prices # 'Mid' 열을 새로 만들고 mid_prices 데이터를 넣습니다.
print(df)


# 종가의 이동평균값을 계산하고 및 주가 데이터에 추가합니다.
ma5 = df['Adj Close'].rolling(window=5).mean()
df['MA5'] = ma5 # 'MA5' 열을 새로 만들고 ma5 값을 넣습니다.


df = df.fillna(0) # 비어있는 값을 모두 0으로 바꾸기
print(df)