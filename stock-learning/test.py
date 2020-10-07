from datetime import datetime #날짜와 시간을 쉽게 조작할 수 있게 하는 클래스 제공
import pandas as pd

# csv 형태의 주식 데이터 파일을 불러오는 코드
df = pd.read_csv('stock.csv') 

# 데이터프레임 출력(데이터프레임은 (헹 X 열)로 이루어진 표 형태의 특수한 데이터 타입)
print(df)


# --- 주식 데이터 살펴보기 --- #

print('\n주식 데이터의 형태를 출력')
print(df.shape)

print('\n주식 데이터의 정보를 출력')
print(df.info)

print('\n주식 데이터의 데이터 타입을 출력')
print(df.dtypes)

print('\n주식 데이터의 상단 5개 행을 출력')
print(df.head())

print('\n주식 데이터의 하단 5개 행을 출력')
print(df.tail())

print('\n주식 데이터의 모든 열을 출력')
print(df.columns)

print('\n주식 데이터의 요약 통계 자료 출력')
print(df.describe())