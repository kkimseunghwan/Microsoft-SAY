
# 사람의 나이 데이터 30을 임시 저장해야 함 ==>> 변수 저장
from encodings.punycode import T

age = 30
print(age)

# 출력 형식 지정해서 출력에 관하여
#   1) 콘솔 출력만 해당X - 웹 출력에도 활용 가능
#   2) 모든 프로그래밍 언어에 동일하게 사용

# %d (decimal) : 정수형 데이터 들어갈 자리
# %05d : 0 채워서 5자리로 표현d
print("나이 : %d살" % age) # ("나이 : %d살" %(구분자) age)
print("나이 : %05d살" % age) 

# %f (float):  실수 데이터 들어살 자리
# %.5f 
eye = 1.2
print("시력 : %f" % eye)
print("시력 : %.3f" % eye)

# %s (string) : 글자데이터 들어갈 자리
addr = "분당"
print(addr)
print("집 : %s" % addr)

# # %b (Boolean) : 논리형데이터 들어갈 자리 ?
hungry = True
print(hungry)
print("배고픈가 : %s" % hungry)
# print("배고픈가 : %b" % hungry) # <- 이딴거 없음

# % 출력 : %%
humi = 30.123123
print("습도 : %.1f%%" % humi)

# 출력 타입 여러개 사용
temp = 10
Today = "기온은 %d도고, 습도는 %.1f%%다" % (temp, humi)
print(Today)

'''
# 콘솔창에 \ 출력
# print("\") <- 오류 발생
print("\\")

# \n (NewLine) -> 줄"만" 바꾸는거
print("가나다\n라마바사")

# \r (Carriage Return) -> 커서를 행의 앞으로 이동
print("가가\r나나")

# 엔터 기능 = \r\n

# 모든 프로그래밍 언어의 공통되는 사항
# \ 뒤에 어떤 문자가 오느냐에 따라 발동되는 효과가 다름

'''

