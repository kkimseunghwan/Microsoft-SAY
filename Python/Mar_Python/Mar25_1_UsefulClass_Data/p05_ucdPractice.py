

# .csv(Comma Separated Value)
# 콤마로 구분되어있는 데이터
# 엑셀에서 열면 이쁘게 열림
#   전세계적으로 주력은 utf-8
#   원래 win : euc-f => 이제는 utf-8인데
#   MS Office가 euc-kr만 인식하고, utf-8은 감당 못함.
#   => 엑셀도 딱히 이쁘게 열린다고 하기는....
# 메모장에서도 열리고
# => 확장자는 허상이다.


# 1) snack.csv 읽어서 한 줄씩 출력
# 2) 이름, 가격, 중량 따로 출력력
# 3) 과자 객체로 만들어서 정보 출력
# 4) g당 가격순 정렬

class Snack:
    def __init__(self, line):
        line = line.replace("\n", "").split(",")
        self.name = line[0]
        self.price = int(line[1])
        self.weight = float(line[2])
    
    def printInfo(self):
        print("이름 : %s" % self.name)
        print("가격 : %d" % self.price)
        print("중량 : %.1f" % self.weight)
    
####################


f = open("C:\\Hwan\\workspace\\TestData\\snack.csv", "r", encoding="utf-8")
print(f)

snackData = []
for line in f.readlines():
    snack = Snack(line)
    snackData.append(snack)
    print("-----")

f.close()

print("-----무게당 가격 순 정렬-----")

for data in sorted(snackData, key=lambda x: (x.price / x.weight)):
    data.printInfo()
    print("g당 가격 : %.1f" % (data.price / data.weight))
    print("-----")

