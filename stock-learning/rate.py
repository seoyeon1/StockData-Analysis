from datetime import datetime #날짜와 시간을 쉽게 조작할 수 있게 하는 클래스 제공
import pandas as pd
import matplotlib.pyplot as plt
from elice_utils import EliceUtils
elice_utils = EliceUtils()
pd.set_option('display.max_columns', None)


#다음 날 종가를 계산하여 새로운 데이터에 추가하고, 이를 이용해 주가 변동률을 계산

# 주식 데이터 불러오기
df = pd.read_csv('stock.csv') 
    

# 당일 종가가 아니라 다음 날 종가를 새로운 컬럼(tomorrow Adj Close)으로 추가하기
# shift(-1) 옵션을 사용하여 데이터를 하루씩 밀어서 삽입
df['tomorrow Adj Close']= df['Adj Close'].shift(-1)


# 주가 변동 및 변동률(%) 추가하기 - 기대 수익률 계산 가능
df['Fluctuation'] = df['tomorrow Adj Close'] - df['Adj Close'] # 주가 변동 데이터(다음날 종가 - 오늘 종가)
#if 내일주가 상승, 변동 = +, else 변동 = -
df['Fluctuation Rate'] = df['Fluctuation'] / df['Adj Close'] # 주가 변동률 데이터(변동 / 오늘 종가)


# 데이터 보기
print(df)