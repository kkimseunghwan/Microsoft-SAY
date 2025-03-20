# 어우 복잡해

# OOP : 실생활 묘사
# OOD (Degsin)
# 객체지향스러운 디장장
#   1) 실제로 비만도 검사 센터에 가서 검사받은 상황을 생각
#   2) 프로그램에 필요한 것만 남기기
#   3) 속성 (프로그램에 필요한 것 만.)
#   4) 상황을 진행.
#   5) ㄱㄱ (최대한 실생활스럽게)

# 멤버 변수 - 객체의 속성 : 의사가 자기소개할 때 할만한거
# 지역 변수 : 메소드 진행 중에만 쓰고 버릴거
# 파라메터
# 전역 변수 - 자제
# 리턴

# 의사

class Doctor:
    # 업무 시작
    def start(self):
        guest = self.callGuest()
        self.ask(guest)
        self.calculBMI(guest)
        self.tellResult(guest)
        pass

    # 손님 call
    def callGuest(self):
        return Customer()

    # 정보 물어보기
    def ask(self, guest):
        guest.tell() # 굳이 Return을 쓰지 않아도 객체에 대한 원본 값이 변경됨. guest 객체가 변경됨.

    # BMI 계산
    def calculBMI(self, guest): # 객체 자체를 넣어 객체 내부의 데이터를 묶어 넣을 수 있다는 장점이 있음.
        guest.BMI = guest.weight/((guest.height/100)**2) # 값 계산 후, 객체의 속성을 추가 할 수 있음

        if guest.BMI >= 39: guest.result = "고도 비만"
        elif guest.BMI >= 37: guest.result = "중도 비만"
        elif guest.BMI >= 30: guest.result = "경도 비만"
        elif guest.BMI >= 24: guest.result = "과체중"
        elif guest.BMI >= 10: guest.result = "정상"
        else: guest.result = "저체중"

    # 결과 답변
    def tellResult(self, guest):
        print("BMI : %.2f" % guest.BMI)
        print("%s씨는 %s" % (guest.name, guest.result))

# 손님
# 속성 - 이름, 키, 몸무게
class Customer:
    # 현재 상태에서는 아래 생성자를 사용할 수 없음.
    # def __init__(self, name, height, weight):
    #     self.name = name
    #     self.height = height
    #     self.weight = weight

    # 답하기
    def tell(self):
        self.name = input("이름 : ")
        self.height = float(input("키 : "))
        self.weight = float(input("몸무게 : "))
        
        #return self.name, self.height, self.weight # 원본 객체의 값이 변경됨. 리턴 필요 없음.

####################
# global 자제
# 이 공간(전역) 최대한 자제

# 의사가 출근 (의사 객체 생성)
d = Doctor()
d.start() # 업무 시작


# def test(g):
#     print("green", g.name)
#     # Customer 객체의 내부 값 자체를 변경. 
#     # <- 원본 값에 영향을 미침. 
#     # 이전 List와 비슷한 상황이라고 보면 댐.
#     g.name = "길" 
#     print("green", g.name)

# g = Customer()
# g.name = "홍"
# print("red", g.name)
# test(g)
# print("red", g.name)

