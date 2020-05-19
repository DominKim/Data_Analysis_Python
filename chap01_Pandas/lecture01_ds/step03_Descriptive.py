#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
step03_Descriptive.py
 - DataFrame의 용약통계
 - 상관계수
"""
import pandas as pd

product = pd.read_csv("product.csv")
product.info()
product.head()
product.tail()

# 요약통계량
summ = product.describe()
print(summ)

# 행 / 열 통계
product.sum(axis = 0) # 행축
product.sum(axis = "rows")
product.sum(axis = 1) # 열축
product.sum(axis = "columns")

# 산포도 : 분산, 표준편차
product.var() # axis = 0
product.std() # axis = 0

# 빈도수 : 집단변수
a_cnt = product.a.value_counts()
print(a_cnt)
'''
3    126
4     64
2     37
1     30
5      7
'''

# 유일값 보기
print(product["c"].unique())
# [3 2 4 5 1]

# 상관관계
product.corr() # 상관계수 정방행

# iris dataset 적용
iris = pd.read_csv("iris.csv")
iris.info()

# subset 생성
iris_df = iris.iloc[:,:4]
iris_df.shape # (150, 4)

# 변수 4개 요약통계량
iris_df.describe()

# 상관계수 행렬
iris_df.corr()

# 집단변수
species = iris.Species
species.value_counts()
'''
setosa        50
versicolor    50
virginica     50
'''
species.unique()
'''
array(['setosa', 'versicolor', 'virginica'], dtype=object)
'''

list(species.unique())
# ['setosa', 'versicolor', 'virginica']
