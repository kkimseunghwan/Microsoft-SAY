import numpy as np

# 행렬 생성
A = np.array([[2, 3, 1], [1, 4, 0]])

# 첫 번째 행 출력
print("첫 번째 행 :", A[0, :])

# 두 번째 열 출력
print("두 번째 열", A[:, 1])

# 행렬 생성
A = np.array( [[2, 3], [1, 4]])
B = np.array( [[5, 1], [2, 2]])

# 행렬 덧셈
sum_matrix = A + B
print("행렬 덧셈\n", sum_matrix)

# 행렬 뺼셈
sub_matrix = A - B
print("행렬 뺄셈\n", sub_matrix)

# 행렬 스칼라 곱
scalar = 2
scalar_matrix = A * scalar
print("행렬 스칼라 곱\n", scalar_matrix)

# 행렬의 곱
# 첫 번째 행렬의 '행'과 두 번째 행렬의 '열'을 조합하여 새로운 행렬을 만드는 연산
# 행렬 A의 열 수과 행렬 B의 행 수가 같아야 연산 가능

dot_matrix = np.dot(A, B)
print("행렬의 곱\n", dot_matrix)

