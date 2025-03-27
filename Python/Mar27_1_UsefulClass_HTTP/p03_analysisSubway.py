# 월요일 학원 지하철
# 월요일만 출근하나
# 가설 설정 -> 월요일만 지하철 사용률이 가장 많은가
# => 요일별 이용객 수 평균 데이터 계산
#   => (탄사람 + 내린사람) 평균 값. 


# from datetime import datetime

# import time
# import tracemalloc

# # 코드 시간, 메모리 사용 분석
# start_time = time.time()
# tracemalloc.start()

# f = "C:\\Hwan\\workspace\\TestData\\SeoulSubwayData.csv"
# csvFile = open(f, "r", encoding="utf-8")
# data = csvFile.readlines()

# # 요일 별, 총 날짜, 누적 유저 저장
# weekData = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

# lastDay = ""
# value = 0
# try:
#     for line in data:
#         value += 1
#         line = line.replace("\n", "").split(",")
#         nowDay = line[0]+line[1]+line[2]
#         when = datetime.strptime(nowDay, "%Y%m%d").weekday()
#         h_InOut = int(line[5]) + int(line[6])
#         weekData[when][0] += h_InOut

#         if lastDay != nowDay:
#             weekData[when][1] += 1 
#             lastDay = nowDay
# except KeyboardInterrupt:
#     print("조기 종료!")


# dateDict = {0: '월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}

# print("확인 데이터 개수 : %d" % value)
# print("확인 한 날짜 : %d일" % sum(x[1] for x in weekData))
# print(weekData)
# print("-----")

# maxDay, maxAvg = 0, 0
# for k in range(0,7):
#     avg = weekData[k][0] / weekData[k][1]
#     print("%s 평균 : %d" % (dateDict[k], avg))
#     if maxAvg < avg:
#         maxDay = k
#         maxAvg = avg

# print("-----")
# print("제일 복잡한 요알 : %s" % dateDict[maxDay])
# print("하루 평균 이용자 : %d" % maxAvg)

# end_time = time.time()
# current, peak = tracemalloc.get_traced_memory()
# print("-----")
# print(f"총 실행 시간: {end_time - start_time:.2f}초")
# print(f"현재 메모리 사용량: {current / 1024 / 1024:.2f} MB")
# print(f"최대 메모리 사용량: {peak / 1024 / 1024:.2f} MB")
# tracemalloc.stop()

##### 스승님 코드 #####


#### GPT 개선 코드####

from datetime import datetime
import time
import tracemalloc

# 코드 시간 분석
start_time = time.time()
tracemalloc.start()

'''
csvFile = open(f, "r", encoding="utf-8") # # 데이터를 메모리에 로드
data = csvFile.readlines() # 해당 데이터들을 리스트 형식으로 저장
# 데이터 크기가 매우 클 경우, 메모리 디짐
# => 파일을 한 줄씩 불러와 실시간으로 처리 
'''

# 요일 별, 총 날짜, 누적 유저 저장
weekData = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

lastDay = ""
value = 0
try:
    with open("C:\\Hwan\\workspace\\TestData\\SeoulSubwayData.csv", "r", encoding="utf-8") as csvFile:
        for line in csvFile:
            value += 1
            line = line.strip().split(",")
            nowDay = line[0]+line[1]+line[2]
            when = datetime.strptime(nowDay, "%Y%m%d").weekday()
            h_InOut = int(line[5]) + int(line[6])
            weekData[when][0] += h_InOut

            if lastDay != nowDay:
                weekData[when][1] += 1 
                lastDay = nowDay
except KeyboardInterrupt:
    print("조기 종료!")


dateDict = {0: '월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}

print("확인 데이터 개수 : %d" % value)
print("확인 한 날짜 : %d일" % sum(x[1] for x in weekData))
print(weekData)
print("-----")

maxDay, maxAvg = 0, 0
for k in range(0,7):
    avg = weekData[k][0] / weekData[k][1]
    print("%s 평균 : %d" % (dateDict[k], avg))
    if maxAvg < avg:
        maxDay = k
        maxAvg = avg

print("-----")
print("제일 복잡한 요알 : %s" % dateDict[maxDay])
print("하루 평균 이용자 : %d" % maxAvg)

end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
print("-----")
print(f"총 실행 시간: {end_time - start_time:.2f}초")
print(f"현재 메모리 사용량: {current / 1024 / 1024:.2f} MB")
print(f"최대 메모리 사용량: {peak / 1024 / 1024:.2f} MB")
tracemalloc.stop()




