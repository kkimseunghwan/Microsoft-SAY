
# JAVA가 1991년 태어남 : 2000년대 고려를 안하던

# 프로그래밍 언어의 어떤 기능이 만들어짐. 예)날짜 2025/3/25
# 세월이 가면, 기술이 발전하면 -> 그 기능이 안맞게됨.
# 그 기능 업그레이드 or 삭제하고 다시 만들게 됨.

# deprecated : 
#   현재 버전에서 사용은 가능한데
#   업그레이드 or 새로 만들 or 대체품 출시

# 패키지명 : x
# 모듈명 : datetime.py <= from datetime
# 클래스명 : datetime <= import datetime
# today으ㅢ 정채 : static 메소드

from calendar import weekday
from datetime import datetime
from time import strftime 

now = datetime.today()
print(now)

print(now.year) # 연도만
print(now.month) # 달만
print(now.day) # 날짜만
print("-----")

# 특정 시간 날짜
d = datetime(2000, 1, 1)
print(d)
print("-----")

# datetime 객체로

# 불-편
d2 = "1999,12,31"
d2 = d2.split(',')
print(d2)
d2 = datetime(int(d2[0]), int(d2[1]), int(d2[2]))
print(d2)
print("-----")

# 날짜 패턴 확인
# help(strftime)

# strptime
# => 날짜 패턴 쓰는 스타일
d3 = "2003/05/05"
d3 = datetime.strptime(d3, "%Y/%m/%d")
print(d3)
print("-----")

# today값이 2025.03.25 형태가 나오도록
d4 = datetime.today()
print(d4)
print("%d.%d.%d" % (d4.year, d4.month, d4.day)) # <= 불 편

# strftime
d4 = datetime.strftime(d4, "%Y.%m.%d")
print(d4)


# 생일 입력(yyyy-MM-dd) : 
# -----
# 한국나이 계산
# 만 나이 계산

birth = input("생일 (yyyy-MM-dd) : ")
birth = datetime.strptime(birth, "%Y-%m-%d")

# 1) 올해는 2025년이라고 값 저장x => 올해 연도 값을 구해야
# 2) 날짜라서 날짜x => 날짜로서 의미가 있으면 날짜.
now = datetime.today()
print("-----")
print("한국나이 : %d" % (now.year - birth.year + 1))
print("만나이 : %d" % (now.year - birth.year if (now.month >= birth.month) and (now.day >= birth.day) else now.year - birth.year -1))


# 생일날 무슨 요일에 태어났는지
birth = "2003/05/05"
birth = datetime.strptime(birth, "%Y/%m/%d")
birth = datetime.strftime(birth, "%A")
print(birth)
