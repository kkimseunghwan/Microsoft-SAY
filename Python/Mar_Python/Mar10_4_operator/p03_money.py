# 과?제

# 구매한 물건가 : N
# 낸 돈 : M
#-------------
# 거스름돈 : x
# 5만원 : x개
# 1만원 : x개
# 5천원 : x개
# 1천원 : x개

price = int(input("구매한 물건가 : "))
give_money = int(input("낸 돈 : "))
print("---------------")

return_money = give_money - price
print("거스름돈 : %d" % return_money)

money = [50000, 10000, 5000, 1000]

for m in money:
    print("%d원 : %d개" % (m, return_money // m))
    return_money %= m



