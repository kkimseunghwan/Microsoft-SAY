# Colab


## 불용어
# - 문장에서는 자주 등장하지만 실제 의미 분석을 하는데는 거의 기여하는 바가 없는 단어들
import nltk
nltk.download('stopwords')
nltk.download('punkt_tab')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt

# 불용어 확인하기 
stop_word_list = stopwords.words('english')
print("불용어 개수 :", len(stop_word_list))
print("불용어 개수 10개 출력 :", stop_word_list[:50])



# 불용어 제거하기
example = "Family is not an important thing. It's everything."
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example)

result = []

for word in word_tokens:
  if word not in stop_words:
    result.append(word)

print("불용어 제거 전 :", word_tokens)
print("불용어 제거 후 :", result)


# 한국어 불용어 제거

okt = Okt()
example = "고기를 아무렇게나 구우려고 하면 안 돼. 고기라고 다 같은 게 아니거든. 예컨대 삼겹살을 구울 때는 중요한 게 있지."
stop_words = "를 아무렇게나 구 우려 고 안 돼 같은 게 구울 때 는"

stop_words = set(stop_words.split(' '))
word_tokens = okt.morphs(example)

result = [word for word in word_tokens if not word in stop_words]

print("불용어 제거 전 :", word_tokens)
print("불용어 제거 후 :", result)
