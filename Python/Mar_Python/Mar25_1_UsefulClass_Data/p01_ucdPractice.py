
# 숫자(str이 포함된) : a,b,c,d
# -----
# 합계, 평균 출력

newList = []
for i in input("숫자 : ").split(','):
    try:
        newList.append(int(i))
    except:
        continue

print("-----")
print("합계 : %d" % sum(newList))
print("평균 : %.1f" % (sum(newList) / len(newList)))

#########################


