
from random import randint

turn = 0
###############

def pickGameAns():
    return randint(1, 10000)

def getUserAns():
    userAns = int(input("뭐 : "))
    if 0 < userAns < 10001:
        return userAns
    else:
        return getUserAns()

def judge(userAns, gameAns):
    global turn
    turn += 1
    if userAns == gameAns: 
        print("%d번 만에 정답." % turn)
        return True
    elif userAns > gameAns:
        print("DOWN")
    else:
        print("UP")

###############

gameAns = pickGameAns()
print(gameAns)

while True:
    userAns = getUserAns()
    if judge(userAns, gameAns):
        break

