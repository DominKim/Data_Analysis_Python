def crawler(x):
    import os
    import sys
    import urllib.request
    from bs4 import BeautifulSoup as bts
    from text_preprocessing import clean_text
    from lst_pick import lst_pick
    client_id = "IFvtovuLLdeQi6K6jywv"
    client_secret = "_51j6auaOC"
    encText = urllib.parse.quote(x)
    start = 1
    str_big = []
    while start < 1000:
        url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText + \
            "&display=30" +  "&sort=date" + "&start=" + str(start)  # xml 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            a = response_body.decode('utf-8')
        else:
            print("Error Code:" + rescode)

        html = bts(a, "html.parser")
        news_titles = html.find_all("title")

        for title in news_titles:
            title_str = str(title.string)
            str_big.append(title_str.strip())
        start += 30

    try:
        pre_str_big = [clean_text(i) for i in str_big]
        data = {}
        for row in pre_str_big:
            for text in row.split():
                data[text] = data.get(text, 0) + 1
    except Exception as e:
        print("예외 발생", e)
    return data