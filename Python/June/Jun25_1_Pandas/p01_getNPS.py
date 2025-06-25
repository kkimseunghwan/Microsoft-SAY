# data.seoul.go.kr 
# 생필품으로 검색
# -> 서울 시 생필품 농수축산물 가격...
# -> OpenAPI


from http.client import HTTPConnection


hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET", "/575a4655496b636839386f58586542/xml/ListNecessariesPricesService/1/10")
resBody = hc.getresponse().read()
print("ASD")
print(resBody.decode("utf-8"))  # 응답 본문을 UTF-8로 디코딩하여 출력
hc.close()  # 연결 종료