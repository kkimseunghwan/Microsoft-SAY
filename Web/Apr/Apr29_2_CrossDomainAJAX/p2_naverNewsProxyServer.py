# 산불로 검색했을 때
# 네이버 뉴스 XML 나오는거
# 콘솔에 출력

# 파싱까지는 x


from fastapi import FastAPI, Response
from p2_naverNewsDAO import NaverNewsDAO

# 실행 명령어(코드 폴더 위치에서.) : uvicorn (파일명):app --host=0.0.0.0 --port=5678 --reload
app = FastAPI()
nnDAO = NaverNewsDAO()


# http://195.168.9.139:1234/naverNews/ <= 접속 가능?
@app.get("/naverNews")
def NaverNews(q):
    rb = nnDAO.getNews(q)
    h = {"Access-Control-Allow-Origin" : "*"}
    return Response(rb, media_type="application/xml", headers=h)
    