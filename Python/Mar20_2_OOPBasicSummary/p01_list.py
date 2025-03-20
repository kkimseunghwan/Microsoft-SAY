
# 홍 : 100, 80, 70
# 김 : 90, 20, 10
# ...
score = [["홍", 100, 80, 70], ["김", 90, 20]]
# print(score[0][0]) # <= 이게 뭔지 어케 암? - 유지보수가 어려워짐

# 이름이 홍길동, 국어 100, 영어 50, 수학 50 인 학생

class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        
        self.kor = kor
        self.eng = eng
        self.math = math

    def printScore(self):
        print("이름 : %s" % self.name)
        print("국어 : %d" % self.kor)
        print("영어 : %d" % self.eng)
        print("수학 : %d" % self.math)


####################
# 2차원, 3차원 List 사용 => 유지 보수가....
# => 객체 List
#       소스 가독성 증가
#       메소드 사용 가능
#       정렬할 때 편해짐

s = Student("홍길동", 100, 90, 80)
# s.printScore()
# Student.printScore(s)

# 객체가 들어있는 List 
score = [
    s, 
    Student("김길동", 30 ,50, 60), 
    Student("이길동", 70, 50, 40),
    Student("최길동", 80, 80, 20)
]

# 2번 학생의 국어 점수를 알고 싶음 
print( score[1].kor )

# 3번 학생의 전체 정보를 알고 싶음
score[2].printScore()

for s in score:
    s.printScore()
    print("-----")

# 학생 객체를 넣으면 
# 총점이 리턴되는 함수
def getScoreSum(student):
    return student.kor + student.eng + student.math

# 2번 학생의 점수 전체 합.
print(getScoreSum(score[1]))

# Lambda 사용
print((lambda s : s.kor + s.eng + s.math)(score[1]))


# 성적 순 정렬
# key= : 정렬 기준을 정해줘라.
# 성적순 정렬(list에 있는 학생 하나씩 빼서 자동으로 정렬을 해줌)
# score.sort(key=lambda s : s.kor + s.eng + s.math, reverse=True)

# 리흠 이름순 정렬(list에 있는 학생 하나씩 빼서 자동으로 정렬을 해줌)
score.sort(key=lambda s : s.name, reverse=True)

for s in score:
    s.printScore()
    print("-----")

