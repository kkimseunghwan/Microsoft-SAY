
# 카카오톡 톡방에서 어떤 단어가 제일 많이 사용되었는지.

#f = open("C:\\Hwan\\workspace\\TestData\\KakaoTalkChats.txt", "r", encoding="utf-8")
f = open("C:\\Hwan\\workspace\\TestData\\KakaoTalkChats_teacher.txt", "r", encoding="utf-8")

txtData = []
for line in f.readlines():
    line = line.replace("\n", "").split(":") # : 기준 채팅 나누기
    if len(line) > 2: # list값이 3일 경우. 날짜 및 시간 분류 되어있는거 거르기 ex) 2023년 12월 2일 오후 1:28
        line = line[-1].lstrip(" ").split(" ") # 데이터의 뒤에서 첫번째 값.(채팅값). 왼쪽 공백 지우고, 공백 기준 단어 나누기
        txtData.extend(line) # 리스트에 붙여서 추가

max_num, max_txt = 0, ""
txtData_dict = {} # 단어별 사용 횟수 저장 딕셔너리
for word in txtData:
    if word in txtData_dict: # 해당 단어가 딕셔너리에 있으면, 횟수 +1
        txtData_dict[word] += 1
    else: # 해당 단어가 딕셔너리에 없으면 횟수 1로 초기화.
        txtData_dict[word] = 1

    # 가장 많이 나온 단어 비교 후 저장
    if max_num < txtData_dict[word]:
        max_num = txtData_dict[word]
        max_txt = word

for i, j in txtData_dict.items():
    if j > 50:
        print(i, j)

print("-----")
print(max_txt, txtData_dict[max_txt]) # 가장 많이 나온 단어와 횟수 출력.

##############################
