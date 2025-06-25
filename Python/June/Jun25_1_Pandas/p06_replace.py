
import pandas as pd
import numpy as np


df = pd.read_csv("C:/Users/soldesk/Downloads/titanic.csv")
df = df[["Name", "Age", "Survived"]]

# 나이 -> 10대/20대/30대 로 나오도록
df["Age"] = df["Age"].fillna(0)  # NaN을 0으로 대체
df["Age"] = df["Age"].astype(int)  # 정수형으로 변
df["Age"] = df["Age"] // 10 * 10  # 10의 자리로 내림
df["Age"] = df["Age"].astype(str) + "대"  # 문자열로 변환 후 '대' 추가
# 생존 여부 -> '생존'/'사망'으로 변경
df["Survived"] = df["Survived"].replace({0: "사망", 1: "생존"}) 
# 이름 -> 성과 이름으로 분리
df["Name"] = df["Name"].str.split(", ")  # 쉼표로
df["Name"] = df["Name"].apply(lambda x: x[1] + " " + x[0])  # 성과 이름 순서로 변경
# 인덱스 재설정
df = df.reset_index(drop=True)  # 기존 인덱스 제거하고 새로
df = df.set_index("Name")  # 이름을 인덱스로 설정
# 나이 순으로 정렬
df = df.sort_values(by="Age")
# 인덱스 이름 변경
df.index.name = "이름"
# 컬럼 이름 변경
df.columns = ["나이", "생존 여부"]
# 최종 결과 출력
print(df) 
 