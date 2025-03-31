
# http://openapi.seoul.go.kr:8088//json/CardBusStatisticsServiceNew/1/5/20151101/

# 1) 파싱해서 csv로 만들기
# 2) 노선별 평균 이용객 수 / 제일 사람이 많은 정류장 / 사계절 중 버스 정류장이 제일 복잡한 계절

# 2015/01/01 ~ 2024/12/31 전체 지하철 운행 정보 subway.csv로
# -> 2015,01,01,1호100번(하계동~용산구청)), 명륜3가 성대입구,45000,30000

from datetime import datetime
from http.client import HTTPConnection
from json import loads
from hwan.StringCleaner import StringCleaner
import time

defaultURL = "//json/CardBusStatisticsServiceNew/"

hc = HTTPConnection("openapi.seoul.go.kr:8088")

startDate = datetime.strptime("20150101", "%Y%m%d")
endDate = datetime.strptime("20241231", "%Y%m%d")

year = int(input("몇년도부터 호출? : "))
# 2015는 이미 돌림
for yy in range(year, 2025):
    
    f = "C:\\Hwan\\workspace\\TestData\\BusDataSet\\BusData"+ str(yy) +".csv"
    csvFile = open(f, "a", encoding="utf-8")
    
    for mm in range(1, 13):
        for dd in range(1,32):
            nowDay = "%d%02d%02d" % (yy, mm, dd)

            try: # 날짜가 존재하는지 확인
                datetime.strptime(nowDay, "%Y%m%d")
            except: # 없는 날짜라면 다음 루프로 패스
                continue

            # 날짜 하루 검사. 1 ~ 끝까지 까지 검사
            limit = 1000
            start_index = 1
            while True: # 날짜마다 Total 값이 다름
                t_start = time.time()
                hc.request("GET", defaultURL + str(start_index) + "/" + str(start_index + limit - 1) + "/" + nowDay)
                resbody = hc.getresponse().read()
                busData = loads(resbody)

                rows = busData.get("CardBusStatisticsServiceNew", {}).get("row", [])

                if not rows: # 현재 rows가 빈 값일 경우 해당 날짜의 반복문은 종료됨.
                    break
                
                buffer = []
                for data in rows:
                    use_ymd = nowDay[0:4] + "," + nowDay[4:6] + "," + nowDay[6:8]
                    rte_name = data["RTE_NM"].replace(",", "")
                    sbwy_stns_nm = data["SBWY_STNS_NM"].replace(",", "")
                    gton_tnope = data["GTON_TNOPE"]
                    gtoff_tnope = data["GTOFF_TNOPE"]
                    data = "%s,%s,%s,%s,%s\n" % (use_ymd, rte_name, sbwy_stns_nm, gton_tnope, gtoff_tnope)
                    #csvFile.write(data)
                    buffer.append(data)
                
                csvFile.write("".join(buffer))
                buffer.clear()

                if len(rows) < limit: # 남은 데이터의 수가 1000개보다 작다면 반복 종료 
                    break

                start_index += limit

                t_end = time.time()
                print(f"{yy,mm,dd}처리 시간: {t_end - t_start:.2f}초")
    
    go = int(input("계속하시겠습니까? 1:(yes) / 0:(no) : "))
    if go == 0:
        break

hc.close()