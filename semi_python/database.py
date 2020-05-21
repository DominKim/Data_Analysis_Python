# encoding=utf-8
def db_conn(x):
    if x == "sql":
        import pymysql
        config = {'host': '127.0.0.1', 'user': 'scott', 'password': 'tiger', 'database': 'work','port': 3306,'charset': 'utf8', 'use_unicode': True}
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        return conn, cursor

    elif x == "oracle":
        import cx_Oracle
        import os 
        os.environ["NLS_LANG"] = ".AL32UTF8"
        START_VALUE = u"Unicode \u3042 3".encode('utf-8')
        END_VALUE = u"Unicode \u3042 6".encode('utf-8')
        conn = cx_Oracle.connect("scott/tiger@localhost:32769/xe")
        cursor = conn.cursor()
        return conn, cursor
    

def news_tab(x):
    _, cursor = db_conn(x)
    if x == "oracle":
        sql = """create table news(text nvarchar2(2000) not null,
        count int not null, 
        search nvarchar2(2000) not null)"""
        cursor.execute(sql)
    else:
        sql = """create table news(text varchar(100) not null,
        count int not null)"""
        cursor.execute(sql)


def search_tab(x):
    _, cursor = db_conn(x)
    if x == "oracle":
        sql = """create table search(text varchar(100) not null)"""
        cursor.execute(sql)
    else:
        sql = """create table search(text varchar(100) not null)"""
        cursor.execute(sql)