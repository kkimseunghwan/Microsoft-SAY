# Anaconda
#   Python + BD/AI 필요한 라이브러리가 다 갖춰진 가상환경
#   +
#   Jupyter Notebook 이라는 툴
#   -> 대화형 처리 가능 : 한 줄 써서 한줄 실행해보고 가능
#   -> 코드와 결과를 함께 볼 수 있음. 분석스러운 작업 하기에 적합함

score = [[100, 90, 80], [50, 60, 70], [90, 100, 80]]
print(score)

import numpy as np
score2 = np.array(score)
print(score2)



# 영어점수가 50 ~ 70인 사이인 학생 ㅡ이름
import pandas as pd
df = pd.DataFrame({
    'name': ['홍길동', '이순신', '강감찬'],
    'kor': [100, 50, 90],
    'eng': [90, 60, 100],
    'math': [80, 70, 80]
})
print(df) 