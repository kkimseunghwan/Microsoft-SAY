
# 가위 바위 보 게임.
# 연승 저장 포함.

from random import randint

####################

# 컴퓨터 출력 값 반환
def pickGameAns():
    ran = randint(1,3) # 1, 2, 3
    print(ran)
    return ran

# 유저 출력 값 검사 및 반환
def getUserAns():
    userHand = int(input("뭐 : "))
    if userHand in {1, 2, 3}: # 해시 탐색, O(1)
        return userHand
    else:
        return getUserAns()

## 디코딩 ##
# 쌩if, 함수, list, dict 등 가능

# 컴퓨터, 유저 가위,바위,보 값 출력
def printRSP(userHand, gameAns):
    rsp = [None, "가위", "바위", "보"]
    print("나 : %s" % rsp[userHand]) # 나 결과 출력
    print("컴 : %s" % rsp[gameAns]) # 컴 결과 출력

# 가위 바위 보 결과 판단
def getResult(userHand, gameAns):
    global nowWin, win

    if gameAns == userHand: # 무승부
        print("무")
        win = max(win, nowWin)
        nowWin = 0
    elif (gameAns, userHand) in ((1, 2), (2, 3), (3, 1)): # 승리
        print("승")
        nowWin += 1
    else: # 패배
        print("패")
        win = max(win, nowWin)
        print("%d연승!" % win)
        return True



# bool : True/False 2가지만 표현 가능.
# => 다른거 쓰자

# 상태가 총 3개
# 판정 + 게임 계속 해야하는지 판단.
# 무 -> 2
# 패 -> 0
# 승 -> 1


# 가위 바위 보 판정 알고리즘
# 슈벌 내 대가리는 왜 이런 생각을 못할꺄
def ANS(userHand, gameAns):
    t = userHand - gameAns
    if not t:
        print("무")
        return 0
    elif t == -1 or t == 2:
        print("패")
        return -1
    else:
        print("승")
        return 1

####################

win = 0 # 최종 연승 계산
while True:
    gameAns = pickGameAns()
    userHand = getUserAns()
    printRSP(userHand, gameAns)

    #getResult(userHand, gameAns) 
    go = ANS(userHand, gameAns)
    if go == -1:
        print('%d승' % win)
        break
    win += go
    

