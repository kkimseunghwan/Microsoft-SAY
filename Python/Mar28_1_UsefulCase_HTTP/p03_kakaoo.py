
# 카카오 개발자 센터 로그인
# https://developers.kakao.com/

# 내 애븦피케이션 - 애플리케이션 추가하기
#   아이콘 넘기고
#   앱 이름 알아서
#   회사명 알아서
#   카테고리 알아서
#   -> 앱 키 -> REST API KEY
#       -> 34123ebf23834864122c75d234e70515


# https://dapi.kakao.com/v2/local/search/keyword.${FORMAT}

# Authorization: KakaoAK ${REST_API_KEY}

# curl -v -G GET "https://dapi.kakao.com/v2/local/search/keyword.json?y=37.514322572335935&x=127.06283102249932&radius=20000" \  -H "Authorization: KakaoAK ${REST_API_KEY}" \--data-urlencode "query=카카오프렌즈"


from http.client import HTTPConnection
from json import loads
from urllib.parse import quote

q = input("키워드 검색 : ")
q = quote(q)

hc = HTTPConnection("dapi.kakao.com")

hc.request("GET", "/v2/local/search/keyword.json?query="+q, headers="Authorization":"KakaoAK 34123ebf23834864122c75d234e70515")

resbody = hc.getresponse().read()
kakaoMapData = loads(resbody)
hc.close()

for data in kakaoMapData["documents"]:
    print("주소", data["address_name"])
    print("이름", data["place_name"])
    print("-----")