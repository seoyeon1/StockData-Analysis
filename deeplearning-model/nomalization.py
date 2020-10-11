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
pd.set_option('display.max_columns', None)
elice_utils = EliceUtils()



# --- 주식 데이터 불러오기(이전 실습에서 진행) --- #
df = pd.read_csv('stock.csv') 

# 주가의 중간값 계산하기
high_prices = df['High'].values # 고가
low_prices = df['Low'].values # 저가
mid_prices = (high_prices + low_prices) / 2 # 고가와 저가의 중간값

# 주가 데이터에 중간 값 요소 추가하기
df['Mid'] = mid_prices # df.insert() 대신 이와 같이 사용 가능합니다.

#이동평균값 계산 및 주가 데이터에 추가하기
ma5 = df['Adj Close'].rolling(window=5).mean()
df['MA5'] = ma5

df = df.fillna(0) # 비어있는 값을 모두 0으로 바꾸기
print('전처리 전의 주가 데이터')
print(df)



# --- 데이터 전처리 --- #

#(이전 과정에서 시가, 종가 데이터를 저장해뒀기 때문) Date 열을 제거합니다.
df = df.drop('Date', axis = 1)


# 데이터 스케일링(MinMaxScaler 적용)
#모든 데이터를 0~1 사이에 값으로 변경:스케일링(정규화)
min_max_scaler = MinMaxScaler()
fitted = min_max_scaler.fit(df)
output = min_max_scaler.transform(df)
output = pd.DataFrame(output, columns=df.columns, index=list(df.index.values))


print('\n전처리 후의 주가 데이터')
print(output.head())





# 전처리 후의 주가 데이터
#        High       Low      Open     Close    Volume  Adj Close       Mid  \
# 0  0.709199  0.676647  0.661017  0.757576  0.511300   0.757576  0.698341   
# 1  0.792285  0.766467  0.796610  0.781818  0.510071   0.781818  0.785822   
# 2  0.833828  0.736527  0.689266  0.903030  0.416490   0.903030  0.791855   
# 3  0.857567  0.862275  0.847458  0.927273  0.364916   0.927273  0.867270   
# 4  0.810089  0.832335  0.785311  0.848485  0.314762   0.848485  0.828054   

#         MA5  
# 0  0.000000  
# 1  0.000000  
# 2  0.000000  
# 3  0.000000  
# 4  0.984986