import pandas as pd

# List 같은거
a = pd.Series([1,2,3,4])
print(a)
print(a[1])

# MS Excel 같은거
b = pd.DataFrame()
b["이름"] = ["홍길동", "이순신", "강감찬"]
b["나이"] = [20, 30, 40]

print(b)

# Pandas는 원본 데이터에 영향 안가는걸 추구함
# index : 찾는 기준
b = b.set_index(b["이름"])
print(b)


print(b.loc["홍길동"])  # index로 찾기
print(b.iloc[0])  # 순서로 찾기