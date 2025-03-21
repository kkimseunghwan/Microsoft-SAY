
# 등장인물
# 친구, 나

# 속성 ??

# 진행시켜 메소드
# 0) 친구/나 둘이 둘이 앉아있는 상황에서 친구가 하자고 해서.
# 1) 친구가 속으로 랜덤한 숫자 하나 생각해놓고
# 2) 나한테 뭐게
# 3) 내가 생각해서 대답
# 4) 친구가 판정
# 5) 2~4를 정답 나올 때까지 반복
# 6) 정답 나오면 몇번 만에 정답이네 얘기

from random import randint

class Enemy:

    def gameStart(self, user):
        gameAns = self.thinkAns()
        print(gameAns) # 확인용
        
        n = 1
        while self.judge(gameAns, self.ask(user)): n += 1
        self.tellResult(n)

    def thinkAns(self):
        return randint(1, 10000)

    def ask(self, user):
        userAns = user.tell()
        return userAns if 0 < userAns < 10001 else self.ask(user)
        
    def judge(self, gameAns, userAns):
        if gameAns > userAns: print("UP")
        elif gameAns < userAns: print("Down")
        else: 
            print("정답")
            return False

        return True

    def tellResult(self, n):
        print("%d만에 성공" % n)

class User:

    def tell(self):
        return int(input("숫자는? : "))

####################

e = Enemy()
u = User()
e.gameStart(u)

