

# 1 와이파이 
# 2 주차장
# 4 흡연실
# 8 24시간

# value = 1 ~ 15

# shift << 활용?

# 3 와이파이, 주차장 0011 0100 0001
# 12 24시간, 흡연실 1100 0001
# 13 흡연실 24시간 와이파이
# 7이면 흡연실 주차장 와이파이
# <= 얘는 반복되서 value 값이 0이 될 때까지 출력 되는거

# 그러면 value 값이 1, 2, 4, 8이 아니면 반복되겠지
# 1, 2, 4, 8
# 2진수? 0001 0010 0100 1000

value = int(input())
print(bin(value))

# if문 4개 - 내가 푼 버전.
if (value & 1): print("와이파이")
if (value & 2): print("주차장")
if (value & 4): print("흡연실")
if (value & 8): print("24시간")

print("-----")

# shift 사용?
# if value & 1 : print("와이파이")
# value = value >> 1
# print(bin(value))

# if value & 1 : print("주차장")
# value = value >> 1
# print(bin(value))

# if value & 1 : print("흡연실")
# value = value >> 1
# print(bin(value))

# if value & 1 : print("24시간")
# value = value >> 1
# print(bin(value))

print("-----")


# 선생님 교육용 코드 : (이후 반복문 활용 가능)


# if value >= (1 << 3): # 8
#     print("24시간")
#     value -= (1 << 3)
# if value >= (1 << 2): # 4
#     print("흡연실")
#     value >= (1 << 2)
# if value >= (1 << 1): # 2
#     print("주차장")
#     value -= (1 << 1)
# if value >= (1 << 0): # 1
#     print("와이파이")
#     value -= (1 << 0)

# print("-----")

# # 아래와 같음
# if value >= 8: # 8
#     print("24시간")
#     value -= 8
# if value >= 4: # 4
#     print("흡연실")
#     value -= 4
# if value >= 2: # 2
#     print("주차장")
#     value -= 2
# if value >= 1: # 1
#     print("와이파이")
#     value -= 1





# 반복문 배우고 문제 재 풀이.
print_dict = { 8:"24시간", 4:"흡연실", 2:"주차장", 1:"와이파이" }

for x, y in print_dict.items():
    if value >= x:
        print(y)
        value -= x

