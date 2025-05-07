
# C:Controller 
#   상황 판단해서 M이 필요하면 M소환, V필요하면 V소환. (흐름제어)  -> 짬 필요
# 프로그램에 진입점 역할

## x, y 받아서 덧셈 출력

# 프로그램 실행을 C 이곳에서 
from p02_M import Calculator
from p02_V import ConsoleScreen

if __name__ == "__main__":
    # 1. x, y 입력을 받아와야됨. => V
    x, y = ConsoleScreen.getXY()
    z = Calculator.getSum(x, y)
    ConsoleScreen.printResult(z)








