import pandas as pd# python 데이터 분석 라이브러리

# 코로나 엑셀 데이터 파일(.xlsx)이 저장된 경로입니다.
data_path = '#'

# pandas를 활용해 엑셀 파일을 불러오고, corona_data에 저장합니다.
corona_data = pd.read_excel(data_path)

# corona_data셋에서 '확진자' 데이터만 추출하여 출력해보세요
confirmed = corona_data['확진자']#데이터셋[열이름]
print(confirmed)