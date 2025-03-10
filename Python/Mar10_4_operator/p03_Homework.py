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
# print("---------------")

# return_money = give_money - price
# print("거스름돈 : %d원" % return_money)
# print("5만원 : %d개" % (return_money//50000))
# print("1만원 : %d개" % (return_money//10000))
# print("5천원 : %d개" % (return_money//5000))
# print("1천원 : %d개" % (return_money//1000))

print("---------------\n거스름돈 : %d원\n5만원 : %d개\n1만원 : %d개\n5천원 : %d개\n1천원 : %d개" % (give_money-price, (give_money-price)//50000, (give_money-price)//10000, (give_money-price)//5000, (give_money-price)//1000))





