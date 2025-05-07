# 프로젝트
# 고객

# 개발자
# Backend 1 중에 PL
# Backend 2
# Backend 3
# Frontend 1
# Frontend 2
# DBA 1
# DBA 2
# 디자인
# 실재 프로젝트에서 분업

############################

# MVC 패턴
#   파일을 나누고, 한 파일은 한 명이 책임지고 끝내자
#   한 파일은 M/V/C 셋 중에 하나만
#       M:Model     : 비즈니스로직 (실제 계산) (백엔드)
#       V:View      : 실제로 사용자 눈에 보이는 항목(디자이너, 프론트엔드)
#                     입력받고, 결과 출력하고
#       C:Controller: 상황 판단해서 M이 필요하면 M소환, V필요하면 V소환. (흐름제어)  -> 짬 필요

x = int(input("x : ")) # 
y = int(input("y : "))
print("-----")
print(x+y)


