from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf#증권 데이터에 특화된 그래프를 출력하는 라이브러리
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker 
import matplotlib.dates as mdates
import numpy as np
from elice_utils import EliceUtils
elice_utils = EliceUtils()


#캔들 차트 그리기

# 주식 데이터 불러오기
df = pd.read_csv('stock.csv', index_col = 0, parse_dates = True) 
df2 = pd.read_csv('stock.csv', index_col = 0, parse_dates = True) 

print('주가 데이터 출력')
print(df)


# mplfinance 라이브러리를 사용하면 캔들 차트를 간편하게 시각화할 수 있습니다.
mc = mpf.make_marketcolors(up='r',down='b')#상승은 빨강, 하락은 파랑
s  = mpf.make_mpf_style(marketcolors=mc)#mc로 스타일 저장
mpf.plot(df, type='candle', figscale=1.2, style=s)#type=캔틀차트 표시


# 시각화 함수
plt.savefig("candle-plot.png")
elice_utils.send_image("candle-plot.png")
#시가 : 아침에 주식시장이 문을 열고나서 처음 이루어진 거래가격
#종가: 주식시장이 문을 닫을 때의 가격
#주가가 올랐을 때는 빨간색으로 표현하며 = ‘양봉’
#주가가 내렸을 때는 파란색으로 = ‘음봉’

#캔들의 두꺼운 부분의 양쪽 끝은 시가와 종가
#양봉의 경우 가격이 아래에서 위로 올라갔다는 의미
# = 두꺼운 부분의 아래쪽이 시가, 윗부분이 종가. 음봉의 경우 반대

#캔들의 얇은선의 양 끝은 해당 장 시점의 최고가&최저가