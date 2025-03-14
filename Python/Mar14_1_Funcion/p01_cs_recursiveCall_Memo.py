
# 1 + 2 + 3 + .... + 50 = ?
# 1 + 2 + 3 + ... 1000 = ?

# 반복문 없이
value = int(input("value : "))

# 내 풀이.
# sum을 배우지는 않았음. 이거 아닌거 같은데.
print("대충 sum :", sum(range(value+1)))


import sys
sys.setrecursionlimit(10000000) # 돌아는 가게 함.
# -- 추가 문제 힌트 --

# 펙토리얼
# 1 까지 다 더하면 = 1
# 3 까지 다 더하면 = 1 + 2 + 3 = 2 
#   => 2까지 다 더한거에서 3을 더함

# 반복문 없이 = 재귀

# 함수를 recursive(재귀적)하게 호출 : 기술명
#   함수 내부에서 자기 자신을 호출해서 반복이 생기게 하는 것.

def getSum(x):
    if x == 1: return 1
    return x + getSum(x-1)

# Factorial
# 수열의 곱
def Factorial(x):
    if x == 1: return 1
    return x * Factorial(x-1)

# 피보나치 수열
# => 첫번째와 두번째 항은 1로 시작되며, 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열이다
# 1, 1, 2, 3, 5, 8, 13, 21. 34, 55, 89
def Fibonacci(x):
    if x < 3: 
        return 1

    return Fibonacci(x-2) + Fibonacci(x-1)

####################

print("GetSum (1 ~ value) :", getSum(value))
print("Factorial :", Factorial(value)) #  ex) 5 : 5 x 4 x 3 x 2 x 1
print("Fibonacci :", Fibonacci(value))


# 함수를 recursive(재귀적)하게 호출 : 기술명
#   함수 내부에서 자기 자신을 호출해서 반복이 생기게 하는 것.
#   언제? 규칙적인 숫자를 계산할때. (개소리)

# 이 재귀라는 놈을 언제 어따가 쓸까?
# 그냥 반복문 쓰면 되는거 아님? 메모리 낭비 심하자너
# => 다음장에 계속

# (나중에 할거) 인공 신경망 - 백프로퍼게이션(Backpropagation, 역전파)
# => 신경망이 학습할 때 가중치를 조정하는 핵심 알고리즘 (가중치는 뭐여?)

'''
🚀 1️⃣ 역전파 과정이 재귀적인 이유
✅ 역전파는 "출력층 → 입력층"으로 오차를 거꾸로 전파하는 과정
신경망이 깊어질수록 가중치 업데이트 과정이 여러 층을 거쳐야 함
이 과정이 순차적으로 반복되며, 수학적으로 재귀적인 구조를 가짐
특정 노드의 가중치를 조정하려면, 이전 층의 오류 정보가 필요하므로 재귀적 접근이 자연스럽다
<= 지금 할거는 아닌듯함
'''
