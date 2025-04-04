# [ 추가적인 Collection ]
# list, set, dict

# range - 범위 표현, 규칙적인 list가 필요할 때.
from re import I
from tempfile import tempdir


a = range(5) # 0 ~ 5 범위
print(a, type(a))

a = range(1, 15) # 1 ~ 15
print(a, type(a))

a = range(1, 15, 2) # 1 ~ 15, 2칸씩
print(a, type(a))

# list 1 ~ 20
a = list(range(1, 20))
print(a)


# Tuple : 튜플 - (  )
t = (10, 10, 20, 30, 40) # 튜플 정의
print(t, type(t))

# 튜플 활용

q = 100
w = 200
print(q, w)

# 값 바꾸기

# 다른언어 버전
temp = q
q = w
w = temp

# 파이썬 버전
q, w = w, q
# q, w = w, q -> 해당 코드 내부적으로 w, q 값을 튜플로 묶음 (w, q)가 생성됨
# 튜플 (w, q)를 풀어서 q, w에 각 각 값을 할당 (튜플 언패킹)
# 결과적으로 q w 의 값이 교환됨  
print(q, w)


