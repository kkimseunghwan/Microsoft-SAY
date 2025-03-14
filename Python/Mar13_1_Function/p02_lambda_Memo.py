
# 함수
# 언제?
#   소스 정리 차원
#   작업이 포함된 함수를 한번 만들어 놓고 반복해서 계속 쓰게

# 1회용 함수
# 함수와 완전히 반대되는 느낌
# => Lambda 함수 : 무명의 1회용 함수.
# => 언제?
#   값 간단하게 구할 때.

# [1] 본인 이름 출력하는 함수를 만들어서 사용해봐라
def printMyName(x):
    print("김승환" * x)

# [1] Lambda
# (lambda parameter변수명, parameter변수명... : 함수 내용)(parameter변수 입력, parameter변수 입력...) 
(lambda x : print("김승환" * x))(3) # 아래와 동일한 함수 _ 대신 이름이 없는. 1회용 함수.


# [2] 숫자 2개 넣으면 합 구하는 함수
def getSum(x,y): return x+y

# [2] Lambda
# 내용 자리에 값만 띡 있으면 그 값을 return.
c = (lambda x,y : x+y)(5, 7)
print(c)

####################

# [1]
printMyName(3)

# 그걸로 5, 7 구해서 콘솔에 찍기
print(getSum(5,7))

