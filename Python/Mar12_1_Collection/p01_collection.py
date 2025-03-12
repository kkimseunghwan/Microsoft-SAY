#List : 주력
a = [1, 1, 1, 1, 1, 2, 3, 4, 6]
print(a)

# set : 중복X, 순서? => 잘 안쓰게 됨.
a = set(a) # list를 set으로 변환 시킨 것.
print(a)

a = list(a)
print(a) # 중복 제거 후 리스트로 다시 변환

# 한번에 가능
a = [1, 1, 1, 1, 1, 2, 3, 4, 6]
a = list(set(a))
print(a)

# JSON과 생긴게 거의 비슷함
# dict : 키(데이터를 찾는 기준)-값(데이터) 쌍, 순서 X
student = {
    "홍길동":[100, 90, 80], 
    "김길동":[50, 30, 20], 
    "이길동":{"국어":30, "영어":10, "수학":0}
    }
print(student["홍길동"][0]) # <- 이딴거 하지 마셈 알아보기 힘듬
print(student["이길동"]["국어"])

l = [[[1,2], [3,4]]] # n차원 리스트 > 현업에서 이런거 쓰겠음?
# 2차원 넘기면 >> 죽어

# 데이터가 아닌 키 값 만 추출하여 구해야 할 경우.
print(student.keys())
print(list(student.keys())) # List로 변환 가능


# student에 최길동이 있나 없나?
# 특정 데이터가 있는제 확인 하는 연산자 : in
# in : 왼쪽 피연산자가 오른쪽 피연산자 내부에 존재하는지 확인하는 연산자
Gildong = "최길동" in student
print(Gildong) # 현재 student 에는 "최길동"이 없기 때문에 False가 출력됨.

# student가 딕셔너리라면 in 연산자는 "최길동"이 student의 키(key) 중에 있는지 확인하는 코드

# dict의 value 내부 검사 방법
for i in student.values():
    a = 100 in i
    print(a)
