
#계산기
# print("-------------\nx는 %d, y는 %d" % (int(input("x : ")), int(input("y : "))))

x = int(input("x : "))
y = int(input("y : "))
print("-------------")
print("x는 %d, y는 %d" % (x,y))

a = x + y
b = x - y
c = x * y
d = x / y
e = x // y
f = x % y # 나머지 구하기
print(a,b,c,d,e,f)

print("-------------")
z = 'ㅋ'

# int * str
#   일반적인 다른언어에서는 안됨
#   Python 에서는 int번 만큼 str 문자 반복
print(10*z) # => ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

# x ** y 
#   일반적인 다른언어에서는 없음
#   Python 에서는 x의 y승
j = x ** y
print(j)

print("-------------")

x = x + 3
print(x)