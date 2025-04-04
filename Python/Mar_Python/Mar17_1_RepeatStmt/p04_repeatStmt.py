
for i in range(5):
    for j in range(5):
        for k in range(5):
            if k == 2:
                break # 현재 진행중인 for문 k 종료
            print(i, j ,k)

print("-----")
ibreak = False
for i in range(5):
    for j in range(5):
        for k in range(5):
            if k == 2:
                ibreak = True # for문 i 자채가 깨지게
            if ibreak: break
            print(i, j ,k)
        if ibreak: break
    if ibreak: break

print("ASd")

# ((덥다는 사실이)진실이)==거짓이 없다면 ==> ??

덥나 = False
if not 덥나:
    print("가만히")

# == True는 생략가능
# == False는 not 어쩌고 로 판별 가능

