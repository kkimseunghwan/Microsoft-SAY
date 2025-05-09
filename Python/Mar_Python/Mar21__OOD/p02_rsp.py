

# 컴퓨터, 나
# 내가 1.가위 2.바위 3.보 중 하나를 내면
# 컴퓨터가 가위, 바위 보 중 하나를 랜덤으로 냄
# 내가 낸거와 비교해서 승패 판단
# 패배 시 게임이 종료되며, 승리 수를 출력.

from random import randint

class GameRefree:
    def callUserCorner(self):
        return User()

    def callEnemyCorner(self):
        return Enemy()

    def start(self):
        enemyCorner = self.callEnemyCorner() # Enemy
        userCorner = self.callUserCorner() # User
        self.tellRule()

        while True:
            enemyHand = self.enemyFire(enemyCorner)
            userHand = self.userFire(userCorner)
            self.tellHand(userHand, enemyHand)
            end = self.judge(userHand, enemyHand, userCorner)
            if end: break
        
        self.tellResult(userCorner.win)
    
    def tellRule(self):
        self.ruleBook = [None, "가위", "바위", "보"]
        for i, v in enumerate(self.ruleBook): # enumerate
            if i != 0: print("%d) %s" % (i, v))
        print("-----")

    def enemyFire(self, enemy):
        return enemy.fire()
    
    def userFire(self, user):
        userFire = user.fire()
        if 0 < userFire < 4:
            return userFire
        return self.userFire(user)
    
    def tellHand(self, userHand, enemyHand):
        print("User :\t", self.ruleBook[userHand])
        print("Enemy :\t", self.ruleBook[enemyHand])

    def judge(self, userHand, enemyHand, user):
        t = userHand - enemyHand
        if not t:
            print("무")
        elif t == -1 or t == 2:
            print("패")
            return True
        else:
            print("승")
            user.win += 1
        return False
    
    def tellResult(self, win):
        print('%d승' % win)

class Enemy:
    def fire(self):
        ran = randint(1,3) # 1, 2, 3
        print("(컴)", ran)
        return ran

class User:
    def __init__(self):
        self.win = 0

    def fire(self):
        return int(input("뭐 : "))

####################

game = GameRefree()
game.start()

