# 바퀴 둘레 
wheel = float(input("바퀴 둘레 : "))

# 앞 기어 톱니 수
front_gear = int(input("앞 기어 톱니 수 : "))

# 뒤 기어 톱니 수
back_gear = int(input("뒤 기어 톱니 수 : "))

# 발 구른 횟수
foot_stomps = float(input("발 구른 횟수 : "))

print("--------------")
# 이동 거리 출력
move_distance = ((front_gear / back_gear) * foot_stomps) * wheel
# rstrip : 문자열에 오른쪽 공백이나 인자가된 문자열의 모든 조합을 제거
print("이동 거리 : {0}".format(str(move_distance).rstrip('0').rstrip('.')))
