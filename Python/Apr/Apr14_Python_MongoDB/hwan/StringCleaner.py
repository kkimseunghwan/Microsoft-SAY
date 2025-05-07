
class StringCleaner:
    
    def CleanTXT(txt):
        txt = txt.replace("&quot;", "")
        txt = txt.replace("&apos;", "")
        txt = txt.replace("&amp;", "")
        txt = txt.replace("&lt;b&gt", "")
        txt = txt.replace("&lt;/b&gt", "")
        txt = txt.replace("<b>", "")
        txt = txt.replace("</b>", "")
        txt = txt.replace(",", "")
        return txt