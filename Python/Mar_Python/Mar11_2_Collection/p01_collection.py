
# [ Collection 변수 ]
# 변수 하나에 : 데이터 N 개를 저장하는 것들 통칭
# 데이터가 여러개 들어가는 자료형

# Collection
#   List 계열   = Python List
#   Set 계열    = Python Set
#   Map 계열    = Python Dict (dictionary:사전)


# List : 평범
# 영어 점수가 80, 30, 54, 12
eng = [ 80, 30, 54, 12, 10, 60, 70, 95, 100, 40 ]
print(eng)
print(type(eng)) # <class 'list'>
print(len(eng)) # 내용물 갯수
print(eng.index(30))
print(eng[1]) # 1번데이터 접근 (0번부터 셈)
print(eng[1:5]) # 1번 ~ (5-1)번 데이터 
print(eng[0:9:3]) # 0번 ~ (9-1)번 데이터 2칸씩 점프 [80, 12, 70]
print(eng[::-1]) # 다 출력, 역순으로

# Python은 str을 List 처럼 사용
s = "옛날로 좀 돌아가봅시다, 얼마 안됐지만."
print(s[2])

mat = {100, 80, 50, 80, 70, 100, 50}
print(mat)
print(type(mat))

# dict - 순서 개념이 없음. 키-값 쌍 형식 데이터
student = { "반장":"홍길동", "부반장":"김길동"}
print(student)
print(type(student))
print(student["반장"])

