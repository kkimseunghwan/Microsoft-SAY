

value = int(input())

# 1 와이파이 
# 2 주차장
# 4 흡연실
# 8 24시간


# 3 와이파이, 주차장
# 12 와이파이, 흡연실
# 13 흡연실 24시간 와이파이
# 7이면 흡연실 주차장 와이파이
# <= 얘는 반복되서 value 값이 0이 될 때까지 출력 되는거

# 그러면 value 값이 1, 2, 4, 8이 아니면 반복되겠지
# 1, 2, 4, 8
# 2진수? 0001 0010 0100 1000

isRepeat = not(value in (1,2,4,8))

while value != 0:
    if value == 1:
        value -= 1 
        print("와이파이")
    elif value == 2: 
        value -= 2
        print("주차장")
    elif value == 4: 
        value -= 4
        print("흡연실")
    elif value == 8: 
        value -= 8
        print("24시간")



