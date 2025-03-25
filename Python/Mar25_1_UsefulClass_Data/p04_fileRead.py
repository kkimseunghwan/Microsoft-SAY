
f = open("C:\\Hwan\\workspace\\Python\\Mar25_1_UsefulClass_Data\\0325Test.txt", "r", encoding="utf-8")

# 1) 전체를 다 읽어서 str로
# data = f.read()
# print(data, type(data))

# 2) 다음 한 줄 읽어서 str로, 다시 부를 때마다 다음 한 줄씩 반환
# data = f.readline()
# print(data, type(data))
# data = f.readline()
# print(data, type(data))

# 3) 전체를 다 읽어서, 엔터키 기준으로 나눠서 List로 
# 데이터에 \n은 남아있음
data = f.readlines()
#print(data, type(data))
for line in data:
    line = line.replace("\n", "") 
    print(line) 

f.close()

