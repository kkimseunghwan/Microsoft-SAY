
from math import floor

name = input("이름 : ")
height = float(input("키 : "))
weight = float(input("몸무게 : "))
print("---------------")

# 계산 해놓고 => 변수 저장
# 결과 출력
# 판정도 필요
BMI = weight/((height/100)**2)

print("BMI : %.2f" % (floor(BMI * 100) / 100))

# 소스가 길다 : 프로그램 용량이 커짐 => HDD를 많이 차지
print("%s씨는" % name, end=' ')
if BMI >= 39: print("고도 비만")
elif BMI >= 37: print("중도 비만")
elif BMI >= 30: print("경도 비만")
elif BMI >= 24: print("과체중")
elif BMI >= 10: print("정상")
else: print("저체중")


# 소스가 짧음
# result 라는 변수 사용 : 램 RAM을 많이 사용
if BMI >= 39: result = "고도 비만"
elif BMI >= 37: result = "중도 비만"
elif BMI >= 30: result = "경도 비만"
elif BMI >= 24: result = "과체중"
elif BMI >= 10: result = "정상"
else: result = "저체중"
print("%s씨는 %s" % (name, result))
