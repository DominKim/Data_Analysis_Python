""" 
step03_newsQueryCrawling2.py

 방법2) url query 이용 : 년도별 뉴스 자료 수집
    ex) 2015.01.01 ~ 2020.01.01
        page : 1 ~ 5
"""

import urllib.request as req
from bs4 import BeautifulSoup as bts
from datetime import datetime
import pandas as pd
from collections import Counter
import re

# 1. 수집 년도 생성 : 시계열 date이용
date = pd.date_range("2015-12-20", "2020-01-01")
len(date) # 1474
date[0]

sdate = [str(day).split()[0].replace("-", "") for day in date]

# 2. Crawler 함수
def newsCrawler(date, pages = 5):

    one_day_date = []
    for page in range(1, pages + 1):
        url = f"http://media.daum.net/newsbox?regDate={date}&page={page}"

        try:
            res = req.urlopen(url)
            src = res.read().decode("utf-8")

            html = bts(src, "html.parser")

            links = html.select('a[class="link_txt"]')

            one_page_data = []
            for link in links:
                link_str = str(link.string)
                one_page_data.append(link_str.strip())

            one_day_date.extend(one_page_data[:40])
        except Exception as e:
            print("예외 발생 :", e)

    return one_day_date # list

# 3. Crawler 함수 호출
year_news_date = [newsCrawler(date) for date in sdate]


