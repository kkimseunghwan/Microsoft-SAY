# Colab


import nltk
nltk.download('punkt')
nltk.download('punkt_tab') # Download the missing 'punkt_tab' resource
from nltk.tokenize import word_tokenize, sent_tokenize, WordPunctTokenizer, TreebankWordTokenizer
from nltk.tag import pos_tag

text = "Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."

# 아포스트로피를(') 포함한 단어 토큰화 처리 관련
# 단어 토큰화 1 : word_tokenize
token01 = word_tokenize(text)  # 단어 토큰화
print("단어 토큰화 1 :", token01) # Don't를 Do와 n't로 분리, Jone's는 Jone과 's로 분리

# 단어 토큰화 2 : WordPunctTokenizer().tokenize
token02 = WordPunctTokenizer().tokenize(text) # 구두점을 별도로 분류
print("단어 토큰화 2 :", token02) # Don't를 Don과 '와 t로 분리,Jone's를 Jone과 '와 s로 분리


# 토큰화 작업 시 고려해야할 사항
# 1. 구두점이나 특수문자를 제외해서는 안된다.
# 2. 줄임말이나 단어내에 띄어쓰기가 있는 경우

# 표준 토큰화 : Penn Treebank Tokenization
tokenizer = TreebankWordTokenizer()
text2 = "Starting a home-based restaurant may be an ideal. it doesn't have a food chain or restaurant of their own."
token03 = tokenizer.tokenize(text2)
print("표준 토큰화 트리뱅크 워드토크나이저 :", token03)


# 문장 토큰화 : sent_tokenize
text03 = "His barber kept his word. But keeping such a huge secret to himself was driving him crazy. Finally, the barber went up a mountain and almost to the edge of a cliff. He dug a hole in the midst of some reeds. He looked about, to make sure no one was near."
token04 = sent_tokenize(text03)
print("문장 토큰화 :", token04)


# 한국어 토큰화 라이브러리 도구 : kss
try:
  import kss
except:
  #!pip install kss # Colab 미설치 시, 설치 진행 필요
  import kss

text = '딥 러닝 자연어 처리가 재미있기는 합니다. 그런데 문제는 영어보다 한국어로 할 때 너무 어렵습니다. 이제 해보면 알걸요?'
print('한국어 문장 토큰화 :',kss.split_sentences(text))

# 영문과 다르게 한국어에는 토큰화 작업에 어려움이 있음

# 1. 교착어의 특성 - 한국어는 조사라는 것이 존재한다. 
# 그(He/Him) 단어 하나에도 [그, 그가, 그는, 그에게, 그를, 그와] 처럼 같은 단어임에도 조가사 붙어 다른 단어로 인식이 되면 자연어 처리가 어려워지는 경우가 많다.
# 이로 인하여 한국어 자연어 처리 진행 시, 단일 단어에 조사 등의 무언가가 붙어있는 경우에는 분리하여 처리가 필요하다.

# 2. 한국어는 띄어쓰기가 잘 지켜지지 않는다.
# 한국어는 띄어쓰기가 어렵고 띄어쓰기가 지켜지지 않아도 이해할 수 있는 점으로 인해 한국어는 수 많은 코퍼스에서 띄어쓰기가 무시되는 경우가 많아 자연어 처리가 어렵다.

# 한국어 토큰화 작업 주요 개념. - 형태소
# ** 형태소란? ** 뜻을 가진 가장 작은 말의 단위
# - 자립 형태소 : 접사, 어미, 조사와 상관없이 자립적으로 쓸 수 있는 형태소. 그 자체로 단어가 된다.
# - 의존 형태소 : 다른 형태소와 결합되어 사용되는 형태소. 접사, 어미, 조사, 어간을 말한다.

'''
예를 들어 다음과 같은 문장이 있다고 합시다.

문장 : 에디가 책을 읽었다
이 문장을 띄어쓰기 단위 토큰화를 수행한다면 다음과 같은 결과를 얻습니다.

['에디가', '책을', '읽었다']
하지만 이를 형태소 단위로 분해하면 다음과 같습니다.

자립 형태소 : 에디, 책
의존 형태소 : -가, -을, 읽-, -었, -다

??? 읽 < 이건 자립 형태소가 아닌가? < 나중에 더 조사해봐야 될 듯.
'''


# 품사 태깅
# 단어 토큰화 과정에서 각 단어가 어떤 품사로 쓰였는를 구분해 놓는 작업을 뜻한다.





