"""  
1. news Crawling
    url : http://media.daum.net
2. pickle save
    binary file save
"""

import urllib.request as req
from bs4 import BeautifulSoup as bts

url = "http://media.daum.net"

# 1. url 요청
res = req.urlopen(url)
src = res.read()
src = src.decode("utf-8") # decode 전 웹페이지

# 2. html 파싱
html = bts(src, "html.parser")
print(html)

# 3. tag[속성="값"] -> "a[class = "link_txt"]"
links = html.select('a[class = "link_txt"]')

crawling_data = []

for link in links:
    link_str = str(link.string)
    crawling_data.append(link_str.strip())

print(crawling_data)
print(len(crawling_data))

# 4. pickle file save
import pickle

# save
import os
file = open("../data/news_crawling.pck", mode = "wb")
pickle.dump(crawling_data, file)

# pickle file load
file = open("../data/news_crawling.pck", mode = "rb")
news = pickle.load(file)
print(news)