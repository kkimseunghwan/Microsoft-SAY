
# 자료형 설정은 Python이 알아서 함

# Python 입장에서는 str로 받아야 글자든 숫자든 다 소화가능
# type casting (형변환) : 자료형을 내가 원하는 자료형으로 바꾸는 것
# => 자료형(값) ex) int(값), float(값) ...
# =>> 사실은 객체 생성

name = input("메뉴\t: ")
price = input("가격\t: ")
print("-------------")

print(name, type(name)) # str
print(price, type(price), id(price)) # str

print("%s원짜리 %s 먹자" % (price, name)) # str 형으로 출력

price = int(price)
print(price, type(price), id(price)) # int
print("%d원짜리 %s 먹자" % (price, name)) # 형변환 진행 후 출력




