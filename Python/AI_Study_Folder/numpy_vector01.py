import numpy as np

# 2차원 벡터 생성
u = np.array([2, 3])
v = np.array([1, -1])

# 덧샘
sum_result = v + u
print("SUM :", sum_result)

# 뺄셈
sub_result = v - u
print("SUB :", sub_result)

# 스칼라 곱
scalar = 2
scalar_result = v * scalar
print("SCALAR :", scalar_result)

# 벡터의 내적
dot_product = np.dot(u, v)
print("DOT :", dot_product)

# 3차원 벡터 정의
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

# 벡터의 외적 <- 헷갈림(보충 필요)
cross_product = np.cross(u, v)
print("CROSS :", cross_product)






