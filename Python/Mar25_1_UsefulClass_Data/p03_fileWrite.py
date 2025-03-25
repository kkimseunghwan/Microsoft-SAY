
# 데이터 -> 임시저장 : 변수 형태로 RAM에 저장
#        -> 영구저장 : 파일 형태로 SDD/HDD에 저장.

# WORA(Write Once, Run Anywhere) : 한번 써두면 어디서든 다 돌아감
#   원래는 시스템 별로 프로그램을 따로 만들어야
#   Win, linux, Unix, Mac, Android, IOS
#   프로그램 하나 만들어 놓으면, 어떤 시스템이든 다 돌아가는거

# 확장자 : Ms Windows에만 있는 허상.
#   .txt : 메모장에서 열면 잘 열릴 것 같은 파일
#   .xls : 엑셀에서 열면 잘 열릴 것 같은 파일
#   .ppt : 파워포인트에서 열면 잘 열릴 것 같은 파일

# 경로
#   Windows : 대소문자 구별x, \, 드라이브로 시작
#   Linux : 대소문자 구별o, /, 드라이버 없음

# ㅋㅋㅋㅋ- 인코딩 -> 10110101 -디코딩 -> ㅋㅋㅋ
# 인코딩 방식이 여러종류
#   utf-8 : 전세계적으로 주력 (Linux가 주로 써서)
#   euc-k



txt = input("뭐 : ")

# open("열고 싶은 파일 경로")
# 파일은 없으면 만들어줌, 드라이브/폴더는 안만들어줌
f = open("C:\\Hwan\\workspace\\Python\\Mar25_1_UsefulClass_Data\\0325Test.txt", "a", encoding="utf-8")
# r : read
# w : write(기존거 지우고)
# a : append (기존거 뒤에)

f.write(txt + "\n")
f.close()





