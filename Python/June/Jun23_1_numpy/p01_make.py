# SQL / 객체 List / Pandas 놔두고 Numpy 쓰는 이유
# 1) Pandas / sklearn / Tensorflow / PyTorch 등은 Numpy를 기반으로 만들어짐
# 2) 인공신경망 (사실은 행렬계산) 구현에 최적화되어 있음

import numpy as np

c = np.arange(1, 10, 2)  # 1부터 10까지 2씩 증가하는 배열 생성
# print(c)

d = np.random.randint(1, 10, size=(3, 4))  # 1부터 10까지의 랜덤 정수로 3x4 배열 생성
# print(d)


g = np.array_split(d, 2, axis=1)  # d를 2열씩 나누어 리스트로 반환
# print(g)

# add() - 요소별 덧셈
# subtract() - 요소별 뺄셈
a = np.random.randint(1, 11, [2, 3])  # 1부터 10까지의 랜덤 정수로 2x3 배열 생성
b = np.random.randint(1, 11, [2, 3])  #

print(a)
print(b)

d = np.add(a, b)  # a와 b의 요소별 덧셈as
print(d)
d = np.subtract(a, b)  # a와 b의 요소별 뺄셈
print(d)
d = np.multiply(a, b)  # a와 b의 요소별 곱셈
print(d)    
d = np.divide(a, b)  # a와 b의 요소별 나눗셈
print(d)


# greater() - 요소별 비교 (a > b)
# greater_equal() - 요소별 비교 (a >= b)
# equal() - 요소별 비교 (a == b)
# not_equal() - 요소별 비교 (a != b)
# less() - 요소별 비교 (a < b)
# less_equal() - 요소별 비교 (a <= b)
j = np.less_equal(a, b)  # a와 b의 요소별 비교 (a <= b)
print(j)

# maximum() - 요소별 최대값
# minimum() - 요소별 최소값
k = np.maximum(a, b)  # a와 b의 요소별 최대값
print(k)



###


name = np.array( ["홍길동", "이순신", "강감찬"] )  # 문자열 배열 생성
kor = np.array( [90, 80, 70] )  # 국어 점수 배열 생성
eng = np.array( [80, 90, 70] )  # 영어 점
math = np.array( [70, 60, 50] )  # 수학 점수 배열 생성

# 평균이 60이 넘는 학생이름
print(name[np.greater(np.divide(np.add(np.add(kor, eng), math), 3), 60)])  # 평균이 60이 넘는 학생 이름 출력


# floor() - 내림
# ceil() - 올림
# rint() - 반올림
# round() - 반올림 (자리수 지정)

