from datetime import datetime #날짜와 시간을 쉽게 조작할 수 있게 하는 클래스 제공
import pandas as pd

# csv 형태의 주식 데이터 파일을 불러오는 코드
df = pd.read_csv('stock.csv') 

# 데이터프레임 출력(데이터프레임은 (헹 X 열)로 이루어진 표 형태의 특수한 데이터 타입)
print(df)


# --- 주식 데이터 살펴보기 --- #

print('\n주식 데이터의 형태를 출력')
print(df.shape)#(105, 7)

print('\n주식 데이터의 정보를 출력')
print(df.info)

print('\n주식 데이터의 데이터 타입을 출력')
print(df.dtypes)
# Date         object
# High          int64
# Low           int64
# Open          int64
# Close         int64
# Volume        int64
# Adj Close     int64
# dtype: object

print('\n주식 데이터의 상단 5개 행을 출력')
print(df.head())

print('\n주식 데이터의 하단 5개 행을 출력')
print(df.tail())

print('\n주식 데이터의 모든 열을 출력')
print(df.columns)
#Index(['Date', 'High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close'], dtype='object')

print('\n주식 데이터의 요약 통계 자료 출력')
print(df.describe())

#                High           Low  ...        Volume     Adj Close
# count    105.000000    105.000000  ...  1.050000e+02    105.000000
# mean   51996.190476  50637.619048  ...  2.390007e+07  51310.476190
# std     3278.145108   3365.597879  ...  1.152018e+07   3331.829995
# min    43550.000000  42300.000000  ...  0.000000e+00  42500.000000
# 25%    49350.000000  48500.000000  ...  1.621493e+07  48800.000000
# 50%    51600.000000  50300.000000  ...  2.105442e+07  51200.000000
# 75%    54700.000000  53200.000000  ...  2.759696e+07  53800.000000
# max    60400.000000  59000.000000  ...  5.946293e+07  59000.000000