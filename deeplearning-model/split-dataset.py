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



# --- 주식 데이터 불러오고 전처리하기(이전 실습에서 진행) --- #
df = pd.read_csv('stock.csv') 

# 주가의 중간값 계산하기
high_prices = df['High'].values
low_prices = df['Low'].values
mid_prices = (high_prices + low_prices) / 2

# 주가 데이터에 중간 값 요소 추가하기
df['Mid'] = mid_prices

# 종가의 5일 이동평균값을 계산하고 주가 데이터에 추가하기
ma5 = df['Adj Close'].rolling(window=5).mean()
df['MA5'] = ma5

df = df.fillna(0) # 비어있는 값을 모두 0으로 바꾸기

# Date 열를 제거합니다.
df = df.drop('Date', axis = 1)

# 데이터 스케일링(MinMaxScaler 적용)
min_max_scaler = MinMaxScaler()
fitted = min_max_scaler.fit(df)

output = min_max_scaler.transform(df)
output = pd.DataFrame(output, columns=df.columns, index=list(df.index.values))



# --- 데이터셋 나누기(학습용 : 테스트용 : 검정용 = 6:3:1) --- #



# 충분한 데이터를 구할 수 없을 경우, 효과적인 예측을 위해 데이터셋을 분할한 후 학습을 진행

# 데이터 전체 길이 파악
# print(len(output))


# 0~60% 지점까지를 트레인셋(학습 데이터)으로 설정(전체의 60%)
train_size = int(len(output)* 0.6) 

# 60-90% 지점까지를 테스트셋으로 설정(전체의 30%)
test_size = int(len(output)*0.3) + train_size


#train/test 학습 및 라벨 설정
#종가를 예측하기 위해 종가를 label로 설정
train_x = np.array(output[:train_size]) # 트레인셋의 독립변수
train_y = np.array(output['Close'][:train_size]) # 트레인셋의 종속변수
test_x =np.array(output[train_size:test_size]) # 테스트셋의 독립변수
test_y = np.array(output['Close'][train_size:test_size]) # 테스트셋의 종속변수
validation_x = np.array(output[test_size:]) # 트레인셋의 독립변수
validation_y = np.array(output['Close'][test_size:]) # 테스트셋의 종속변수

print('분할 전 전체 데이터의 길이: %s' % len(output))
print('학습 데이터의 길이: %s' % len(train_x))
print('테스트 데이터의 길이: %s' % len(test_x))
print('검증용 데이터의 길이: %s' % len(validation_x))