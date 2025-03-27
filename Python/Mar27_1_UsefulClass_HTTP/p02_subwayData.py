
# 2015/01/01 ~ 2024/12/31 전체 지하철 운행 정보 subway.csv로
# -> 2015,01,01,1호선,서울역,45000,30000

# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/1000/20150101/
# http://openapi.seoul.go.kr:8088/.../xml/CardSubwayStatsNew/1/1000/20150101/



defaultURL = "/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/620/"

import time # 코드 시간 측정.

from datetime import datetime, timedelta
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

hc = HTTPConnection("openapi.seoul.go.kr:8088")

## 내가 썼던 코드

start_time = time.time()

start = datetime.strptime("20150101", "%Y%m%d")
end = datetime.strptime("20241231", "%Y%m%d")

f = "C:\\Hwan\\workspace\\TestData\\SeoulSubwayData.csv"
csvFile = open(f, "a", encoding="utf-8")

for i in range((end-start).days+1):
    nowDay = start + timedelta(days=i)
    hc.request("GET", defaultURL + nowDay.strftime("%Y%m%d"))
    resbody = hc.getresponse().read()

    station = fromstring(resbody).iter("row")
    if station != None:
        for r in station:
            use_ymd = nowDay.strftime("%Y,%m,%d")
            sbwy_rout_ln_nm = r.find("SBWY_ROUT_LN_NM").text
            sbwy_stns_nm = r.find("SBWY_STNS_NM").text
            gton_tnope = r.find("GTON_TNOPE").text
            gtoff_tnope = r.find("GTOFF_TNOPE").text
            data = "%s,%s,%s,%s,%s\n" % (use_ymd, sbwy_rout_ln_nm, sbwy_stns_nm, gton_tnope, gtoff_tnope)
            csvFile.write(data)
       

hc.close()

end_time = time.time()
print(f"총 실행 시간: {end_time - start_time:.2f}초")


## 강사님 코드 ##

# start_time = time.time()

# new_f = "C:\\Hwan\\workspace\\TestData\\newSeoulSubwayData.csv"
# csvFile = open(new_f, "a", encoding="utf-8")

# for yy in range(2015, 2025):
#     for mm in range(1, 13):
#         for dd in range(1,32):
#             when = "%d%02d%02d" % (yy, mm, dd)
#             hc.request("GET", defaultURL + when) # 없는 날짜는 애초에 출력을 하지 않음
#             resbody = hc.getresponse().read()

#             station = fromstring(resbody).iter("row")
#             if station != None:
#                 for r in station:
#                     use_ymd = r.find("USE_YMD").text
#                     y, m, d = use_ymd[0:4], use_ymd[4:6], use_ymd[6:8]
#                     sbwy_rout_ln_nm = r.find("SBWY_ROUT_LN_NM").text
#                     sbwy_stns_nm = r.find("SBWY_STNS_NM").text
#                     gton_tnope = r.find("GTON_TNOPE").text
#                     gtoff_tnope = r.find("GTOFF_TNOPE").text
#                     data = "%s,%s,%s,%s,%s,%s,%s\n" % (y,m,d, sbwy_rout_ln_nm, sbwy_stns_nm, gton_tnope, gtoff_tnope)
#                     csvFile.write(data)


# hc.close()

# end_time = time.time()
# print(f"총 실행 시간: {end_time - start_time:.2f}초")

####