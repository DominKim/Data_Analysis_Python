"""  
step02_news_wordCloud.py

1. text file load
2. 명사 추출 : Kkma
3. 전처리 : 단어 길이 제한, 숫자 제외
4. wordcloud
"""
import pickle
from wordcloud import WordCloud
from collections import Counter
from konlpy.tag import Kkma
import re
import matplotlib.pyplot as plt

# object 생성
kkma = Kkma()

# 1. pickle file 읽기 : text_data.txt
file = open("../data/news_data.pck", mode = "rb")
news_data = pickle.load(file)
file.close
len(news_data)

# 2. 명사 추출 : kkma
nouns_word = [kkma.nouns(i) for i in news_data]
len(nouns_word) # 11600

# 3. 전처리 : 단어 길이 제한(1음절), 숫자 제외
nouns_count = {}

for idx, value in enumerate(nouns_word):
    for noun in value:
        if not(re.findall("^[0-9]", noun)) and len(noun) > 1:
            nouns_count[noun] = nouns_count.get(noun,0) + 1

nouns_count
len(nouns_count) # 17155

nouns_count["확진자"] = nouns_count["진자"]
del nouns_count["진자"]

# 4. wordcloud

# 1) top50 word
word_count = Counter(nouns_count)
top50 = word_count.most_common(50)

# 2) wordcloud
wc = WordCloud(font_path="Library/Fonts/AppleGothic.ttf",
width=800, height=600, max_words=100, max_font_size = 150, background_color="white")
img = wc.generate_from_frequencies(dict(top50))

plt.imshow(img)
plt.axis("off")
