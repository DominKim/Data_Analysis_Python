"""  
step02_newsQueryCrawling.py

news Crawling : url query 이용
    url : http://media.daum.net
    url : http://media.daum.net/newsbox
    url : http://media.daum.net/newsbox?regDate=20200505
    url : http://media.daum.net/newsbox?regDate=20200505&page=1
"""

import urllib.request as req # url 요청
from bs4 import BeautifulSoup as bts # html 파싱

# 1. url query 만들기
"""  
date : 2020.2.1 ~ 2020.2.29
page : 1 ~ 10
"""

# base url + date
base_url = "http://media.daum.net/newsbox?regDate="
date = list(range(20200201, 20200230))
date
len(date) # 29

url_lst = [base_url + str(i) for i in date]
url_lst

# base url _ date _ page

page = list(range(1,11)) # 1 ~ 10
page

pages = ["&page=" + str(p) for p in page]
pages
final_url = []

for url in url_lst:
    for page in pages:
        final_url.append(url + page)

len(final_url) # 290

# Crawler 함수 정의
def Crawler(url):
    res = req.urlopen(url)
    src = res.read()
    src = src.decode("utf-8")

    html = bts(src, "html.parser")

    links = html.select("a[class = 'link_txt']")

    one_page_data = []
    for link in links:
        link_str = str(link.string)
        one_page_data.append(link_str.strip())

    return one_page_data[:40]

one_page_data = Crawler(final_url[0])
len(one_page_data)

# 2월(1개월) 전체 news 수집
month_news = []

for url in final_url:
    try:
        one_page_data = Crawler(url)
        month_news.extend(one_page_data)
    except Exception as e:
        print("해당 url 없음 : ", url)


import pickle

file = open("../data/news_data.pck", mode = "wb")
pickle.dump(month_news, file)
file.close()

file = open("../data/news_data.pck", mode = "rb")
a = pickle.load(file)
print(a)