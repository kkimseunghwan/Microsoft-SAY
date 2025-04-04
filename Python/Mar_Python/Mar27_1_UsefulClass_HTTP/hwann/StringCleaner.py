
# 자주 쓰니까 => 따로 정리하자

class StringCleaner:
    #@staticmethod # 객체를 만들지 않아도 쓸 수 있는 함수
    def DeleteBold(txt):
        txt = txt.replace("&quot;", "")
        txt = txt.replace("<b>", "")
        txt = txt.replace("</b>", "")
        return txt
    
    def CleanTXT(txt):
        txt = txt.replace("&quot;", "")
        txt = txt.replace("<b>", "")
        txt = txt.replace("</b>", "")
        txt = txt.replace(",", "")
        return txt

