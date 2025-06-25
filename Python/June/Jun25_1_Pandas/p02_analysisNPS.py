import pandas as pd
import numpy as np


# 물가.csv 파일 불러서 df로
# 마트이름, 품명, 가격, 날짜, 종류, 구
df = pd.read_csv(
    'C:/Users/soldesk/Downloads/lnps.csv', 
    names=["마트", "품명", "가격", "날짜", "종류", "구"]
)

# 마트 이름으로 찾게 세팅
df = df.set_index(df["마트"])

# 마트 이름 가나다 순 정렬
df = df.sort_index()

# 한번 출력
print(df)
print("=====")

# 통인시장 데이터만
print(df.loc["통인시장"])  # 통인시장의 모든 데이터 출력
print("=====")

# 마트명에 '농협'들어있는 데이터만
print(df[df["마트"] == "농협"])
print("=====")

# 사과는 어떤 마트에 가면 살 수 있는지
print(df[df["품명"] == "사과"])  # 사과가 있는 마트 출력
print("=====")

# 품명 가나다순 -> 가격 비싼 순 정렬


# 30000원 이상인 데이터 품명, 가격
print(df[df["가격"] >= 30000][["품명", "가격"]])
print("=====")

# 종로구 데이터만 반복문 돌려서 하나하나 출력
for index, row in df[df["구"] == "종로구"].iterrows():
    print(row)
