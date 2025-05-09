import pandas as pd

# df = pd.read_csv("C:\Hwan\TestData\서울시 부동산 실거래가 정보-양천구.csv", encoding="CP949")
df = pd.read_csv("C:\Hwan\TestData\서울시 부동산 실거래가 정보-양천구.csv", encoding="CP949")


# 데이터 확인
# 데이터의 상위 5개의 행을 출력
print(df.head())

# 데이터 요약 메서드
print(df.describe())

# 데이터프레임의 null값의 개수를 확인
print(df.isnull().sum())

# 데이터 시각화 라이브러리
import matplotlib.pyplot as plt
# matplotlib을 기반으로 다양한 색 테마, 차트 기능을 추가한 라이브러리
import seaborn as sns

apartment_df = df[df['건물용도'].str.contains('아파트', na = False)]

# 실제 컬럼명을 반영하여 연도별 아파트 평균 물건금액 계산 및 시각화
mean_by_year = df.groupby('접수연도')['물건금액(만원)'].mean().reset_index()

plt.figure(figsize=(12, 6))

# 평수, 가격 관계
sns.scatterplot(data=df, x="건축년도", y="물건금액(만원)", alpha=0.3, s=15)  # alpha는 투명도, s는 점 크기

# 범위 제한
plt.xlim(1900, 2025)            # 건물면적(㎡) 제한
#plt.ylim(0, 450000)      # 물건금액(만원) 제한

# plt.plot(mean_by_year['접수연도'], mean_by_year['물건금액(만원)'], marker='o')
plt.title('Average apartment price by footage')
plt.xlabel('footage')
plt.ylabel('AVG Price (10,000)')
plt.grid(True)
plt.tight_layout()
plt.show()
