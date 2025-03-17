
# 컴퓨터가 1 ~ 10000 사이 랜덤한 숫자 하나 생각해놓고
# 그 숫자를 맞추는 게임

# 예) 5912
# 입력 - 4000
# => UP
# 입력 - 6000
# => DOWN
# ...
# 13번 만에 정답.

from random import randint

random_num = randint(1, 10000)
print(random_num)

n = 1
while True:
    a = int(input("뭐 : "))
    if not (a in range(1, 10001)):
        continue
    
    if random_num > a: print("UP")
    elif random_num < a: print("Down")
    else: break
    n += 1

print("%d번만에 정답" % n)
