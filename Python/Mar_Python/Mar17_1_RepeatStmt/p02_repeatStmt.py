
# 1 + 2 + 3 + ... 100 = ?
from random import randint

n = 0
for i in range(0, 101):
    n += i
print(n)

k = sum(i for i in range(0, 101))
print(k)



# 파이썬의 for 은 콜렉션 탐색용.
#   range를 활용하여 특정 회수 반복 느낌을 내는거

# 1 + 2 + .. ? >= 100를 만족하는 ? 의 최소값을 구하시오.

# 반복 조건 - while
#    while 조건식:
#       조건식 맞으면 실행
# while 문법 구조상 조건식을 먼저 써야 되는데 - 이게 참 애매함

n = i = 0
while n < 100:
    i += 1
    n += i

print(n, i)


# 1 ~ 10 사이 랜덤한 정수
c = randint(1, 10)
print(c)

print("-----")

# 1 ~ 5 사이 랜덤한 정수
# 10번
for i in range(10):
    d = randint(1, 5)
    print(d)

print("-----")

# 1 ~ 5 사이 랜덤한 정수
# 4가 나올 떄 까지.

num = 0 # 변수 선언을 안하면 아래 조건식에서 오류가 발생함.
while num != 4:
    num = randint(1, 5)
    print(num)

print("-----")

# 수 입력 받아서 10일 경우 멈추기

# 아쉽
# f = int(input("뭐 : "))
# print(f)
# while f != 10:
#     f = int(input("뭐 : "))
#     print(f)


# print("-----")

# 반복문 제어
#   break : 반복문 종료
#   continue : 턴 종료

for i in range(10):
    if i == 3:
        # break # 반복문 바로 종료
        # continue # 아래 남은 코드줄 실행 안하고 바로 위 (for i in range(10)) 반복으로
        pass
    print(i)

print("-----")

# while
#    while 문법 구조상 조건식을 먼저 써야 되는데 - 이게 참 애매함

# 아무 숫자나 입력받아서 출력, 10이라고 쓰면 그만
# 그럼 걍 무한루프 돌리고, 반복문 내부에 종료 조건이 담긴 동작 코드를 추가.
while True:
    menu = int(input("뭐 : "))
    if menu == 1: print("메뉴를 등록...")
    elif menu == 2: print("메뉴를 조회")
    elif menu == 10: break

# while int(input()) != 10:
#     pass

# 4나올때까지 랜덤 정수
while True:
    a = randint(1,5)
    print(a)
    if a == 4: break
