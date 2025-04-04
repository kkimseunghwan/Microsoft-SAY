
# 로또 번호 자동 생성기
# set 쓰지 말고

# 45개 숫자 중
# 순서와 상관없이 당첨번호 6개

from random import randint

lotto_list = [0, 0, 0, 0, 0, 0]

# 뭔가 확률이 안 맞아 보임
def getNumber(lotto_list):
    randNum = randint(1, 45)
    if randNum in lotto_list:
        return getNumber(lotto_list)
    return randNum

for i in range(6):
    lotto_list[i] = getNumber(lotto_list)

print(lotto_list)

print("-----")


lotto_list = []

while len(lotto_list) < 6:
    randNum = randint(1, 45)
    if randNum not in lotto_list:
        lotto_list.append(randNum)


print(lotto_list)


print("-----")

def pick(i, lotto):
    ball = randint(1,45)
    for j in range(i):
        if ball == lotto[j]:
            return pick(i, lotto)
    return ball

lotto = []
for i in range(6):
    lotto.append(pick(i, lotto))


print("-----")

a = randint(1, 6)
b = randint(1, 6)
c = randint(1, 6)
d = randint(1, 6)
e = randint(1, 6)

print(a,b,c,d,e)