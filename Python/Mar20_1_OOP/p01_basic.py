
# 리얼월드 고양이
# 멤버 xx : 객체의 xx => 변수명.xx
# 1) 고양이 class
# class를 만든다 : 도장/붕어빵 틀


class Cat:
    # 속성 :멤버 변수
    # 밖에서도 변수 정의가 되는데 무슨의미가.. => 딱히 여기를 잘 안씀
    name = None
    age = None
    weight = None

    # 액션/프로그램 상 필요한 기능 : 메소드
    def meow(self, cnt): # 메소드는 첫번째 파라미터로 self를 무조건, 두번째부터는 마음대로
        print("냥" * cnt)

    def showInfo(self):
        print(self.name) # 멤버 뭐시기는 주어가 필요 # 누구의 변수인 것인지. self = 자기자신.
        print(self.age)
        print(self.weight)
        print(self.color)




###############

# 2) 고양이 갹체 object 생성
c1 = Cat()
c1.name = "후추"
c1.age = 3
c1.weight = 5

c1.color = "yellow" # 클래스 내에 정의 되지 않는 함수 => 파이썬은 클래스 외부에서 멤버 추가 가능
print(c1.color) # 되긴 됨.

# 다른 프로그래밍 언어 스타일
c1.meow(5) # 호출할 때는 self는 없는 셈 치고(?) 실행
c1.showInfo()

# Python 정통 메소드 호출 스타일
# 클래스명.메소드명(변수명, ...)
Cat.meow(c1, 5) # <= c1이 메소드의 self로 들어감
Cat.showInfo(c1)


