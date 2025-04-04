
class StringCleaner:
    
    def CleanTXT(txt):
        txt = txt.replace("&quot;", "")
        txt = txt.replace("<b>", "")
        txt = txt.replace("</b>", "")
        txt = txt.replace(",", "")
        return txt