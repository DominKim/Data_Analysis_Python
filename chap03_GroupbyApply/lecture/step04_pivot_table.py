'''
step04_pivot_table.py

피벗테이블(pivot table)
 - 사용자가 행, 열 그리고 교차셀에 변수를 지정하여 테이블 생성
'''

pip install pandas
pip install matplotlib
import pandas as pd
import os
os.getcwd()

pivot_data = pd.read_csv("../../data/pivot_data.csv")
pivot_data.info()
'''
교차셀 : 매출액(price) -> 연속형변수
행 : 년도(year), 분기(quarter) -> 집단변수
열 : 매출규모(size) -> 집단변수
셀에 적용할 통계 : sum
'''

ptable = pd.pivot_table(pivot_data, values = "price",
index = ["year", "quarter"],
columns="size",
aggfunc="sum")

ptable
'''
size	LARGE	SMALL
year	quarter		
2016	1Q	2000	1000
2Q	2500	1200
2017	3Q	2200	1300
4Q	2800	2300
'''
ptable.shape # (4, 2)

ptable.plot(kind = "barh", title = "2016 vs 2017")
ptable.plot(kind = "barh", title = "2016 vs 2017", stacked = True)

# movie_rating.csv
# 행 : 평가자
# 열 : 영화제목
# 셀 : 평점
# 적용함수 : 합계

movie = pd.read_csv("../../data/movie_rating.csv")
movie.info()
ptable_movie = pd.pivot_table(movie, values = "rating",
                              index = "critic",
                              columns = "title", 
                              aggfunc = "sum")
ptable_movie
'''
title    Just My  Lady  Snakes  Superman  The Night  You Me
critic                                                     
Claudia      3.0   NaN     3.5       4.0        4.5     2.5
Gene         1.5   3.0     3.5       5.0        3.0     3.5
Jack         NaN   3.0     4.0       5.0        3.0     3.5
Lisa         3.0   2.5     3.5       3.5        3.0     2.5
Mick         2.0   3.0     4.0       3.0        3.0     2.0
Toby         NaN   NaN     4.5       4.0        NaN     1.0
'''

# 평가자 기준 평점의 평균
ptable_movie.mean(axis = 1)
# 영화 기준 평점의 평균
ptable_movie.mean(axis = 0)
