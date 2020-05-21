def clean_text(texts):

    from re import sub  # gsub() 유사함

    # 1. 소문자 변경
    texts_re = texts.lower() # 문장 1개 소문자 변경

    # 3. 문장부호 제거(불용어 제거 (2))
    punc_str = "[.,;:!?]"
    texts_re2 = sub(punc_str, "", texts_re)

    # 4. 문장부호 제거(불용어 제거 (3))
    spec_str = "[!@#$%^&*()]"
    texts_re3 = sub(spec_str, "", texts_re2)

    # 5. naver open api - enws '빅데이터' 제거
    naver_str = "naver open api - news 빅데이터"
    texts_re4 = sub(naver_str, "", texts_re3)

    # 6. <b> 제거
    texts_re5 = sub("[<b>]", "", texts_re4)

    # quot 제거
    texts_re6 = sub("[quot]", "", texts_re5)

    # 7. 공백(white space) 제거(불용어 제거 (4)) : 'abtta a' -> ''.join('abtta', 'a') -> 'abttaa'
    texts_re7 = " ".join(texts_re6.split())

    # 8. 메타문자 제거
    symbols = [',', '.', ':', '-', '+', '/', '*', '&', '%', '[', ']', '(', ')', "'", '"']
    for symbol in symbols:
        texts_re7 = texts_re7.replace(symbol, '')

    # 9.'' 제거
    if(texts_re7[0] == texts_re7[-1]) and texts_re7.startswith(("'", '"')):
        texts_re7 = texts_re7[1:-1]

    return texts_re7
