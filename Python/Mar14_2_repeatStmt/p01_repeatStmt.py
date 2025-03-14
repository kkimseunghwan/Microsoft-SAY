# 재귀 <= 연속적인 숫자 찍어내는 용도가 아님.

# 반복문
#   횟수 : 푸쉬업 100개
#   조건 : 푸쉬업 점심먹고 5교시 시작 전까지 반복


# 일반적인 프로그래밍 언어]
# 횟수 반복 : for 문
# 조건 반복 : while 문
# List 탐색용 : foreach 문

# 파이썬]
#   컬렉션 탐색용 : for
#   조건 따져서 반복 : while

# 컬렉션

a = [234, 56, 23, 98, 3, 7896]

# [ for문 ]
# for 변수병 in 컬렉션:
#     내용

for v in a:
    print(v)


# 1 ~ 5 출력
for i in range(1,11):
    print(i)

# 10!
num = 1
for i in range(1, 11):
    num *= i
print(num)


# 변수 만들기만 하고 값은 안넣으면?
# => 프로그램 언어마다 다름 (0값, 쓰레기값, 에러, 등등..)
# JAVA] 정의만 하고 값을 주지 않으면 에러 발생
# PYTHON] 문법상 존재 자체가 불가능. 값이 없는 변수는 선언할 수 없음. => 값을 안넣으면 안됨.

b = [12, 234, 456]
# enumerate() => (인덱스, 값)을 튜플 형태로 받아오는 것.
for v in enumerate(b):
    print(v, type(v))

c = {"기온":20, "미세먼지":"심함"}
for k, v in c.items():
    print(k, v, type(k), type(v))