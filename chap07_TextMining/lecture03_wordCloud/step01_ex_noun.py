"""  
step01_ex_noun.py

1. text file load
2. 명사 추출 : Kkma
3. 전처리 : 단어 길이 제한, 숫자 제외
4. wordcloud
"""

from konlpy.tag import Kkma
from wordcloud import WordCloud
from collections import Counter
import re
import matplotlib.pyplot as plt

# obejct 생성
kkma = Kkma()

# 1.text file 읽기 : text_data.txt
file = open("../data/text_data.txt", mode = "r", encoding="utf-8")
docs = file.read()
docs
# docs -> sentence
ex_sent = kkma.sentences(docs)
# docs -> nouns
ex_nouns = kkma.nouns(docs)

# 2. 명사 추출 : Kkma
nouns_word = []
sents = kkma.sentences(docs)

for sent in sents:
    for noun in kkma.nouns(sent):
        nouns_word.append(noun)

nouns_word

# 3. 전처리 : 단어길이 제한, 숫자 제외
nouns_count = {}

for noun in nouns_word:
    if not(re.findall("^[0-9]", noun)) and len(noun) > 1:
        nouns_count[noun] = nouns_count.get(noun, 0) + 1

nouns_count

# 4. wordcloud

word_count = Counter(nouns_count)
top5_word = word_count.most_common(5)
top5_word

# 2) wordcloud
wc = WordCloud(font_path = "/Library/Fonts/AppleGothic.ttf",width=500, height = 400, max_words=100, max_font_size=150, background_color="white")

wc_result = wc.generate_from_frequencies(dict(top5_word))
plt.imshow(wc_result)
plt.axis("off")