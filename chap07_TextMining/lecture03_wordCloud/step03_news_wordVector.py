"""  
step03_news_wordVector.py

news Crawling data -> word vector
    문장 -> 단어 벡터 -> Sparse matrix(희소행렬)
    ex) "직업은 데이터 분석가 입니다." -> "직업 데이터 분석가"
"""

import pickle
from konlpy.tag import Kkma
from wordcloud import WordCloud
from collections import Counter
import re

# object 생성
kkma = Kkma()

# 1.pickle file 읽기 : text_data.txt
file = open("../data/news_data.pck", mode = "rb")
news_data = pickle.load(file)
file.close()
news_data
type(news_data) # list
len(news_data)  # 11600
news_data[:5]

# 2. docs -> sentence
ex_sent = [kkma.sentences(sent)[0] for sent in news_data] #[0] : 원소만 반환 하기
# ex_sent = kkma.sentences(docs) # list
ex_sent
len(ex_sent) # 11600

# 3. sentence -> word vector
from re import match

sentence_nouns = [] # 단어 벡터 저장
for sent in ex_sent:
    word_vec = ""
    for noun in kkma.nouns(sent): # 문장 -> 명사 추출
        if len(noun) > 1 and not(match("^[0-9]", noun)):
            word_vec += noun + " " # 명사 + 명사
    print(word_vec)
    sentence_nouns.append(word_vec)

len(sentence_nouns) # 11600

# 4. file save
file = open("../data/sentence_nouns.pickle", mode = "wb")
pickle.dump(sentence_nouns, file)
file.close()

# file load
file = open("../data/sentence_nouns.pickle", mode = "rb")
word_vector = pickle.load(file)
word_vector[0]
file.close()
