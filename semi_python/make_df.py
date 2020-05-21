# encoding=utf-8
import sys

def df(x, y):
    from news_crawling import crawler
    import pandas as pd
    from database import db_conn

    data = crawler(y)
    conn, cursor = db_conn(x)
    text = []
    count = []
    for key, value in data.items():
        if len(key) >= 2:
            text.append(str(key))
            count.append(value)
    for i in range(len(text)):
        sql = f"insert into news values('{text[i]}', {count[i]}, '{y}')"
        cursor.execute(sql)
        conn.commit()

    b = {"Text" : text, "Count" : count}
    a = pd.DataFrame(b)
    b = a.sort_values(by="Count", ascending=False).head(10)


    import matplotlib.pyplot as plt
    from matplotlib import font_manager, rc
    # mac
    rc('font', family='AppleGothic')

    plt.rcParams['axes.unicode_minus'] = False
    # 윈도우
    # font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name() 
    # rc('font', family=font_name)
    plt.bar(b["Text"], b["Count"])
    plt.savefig(f'./semi_python/static/news_plot.png')
