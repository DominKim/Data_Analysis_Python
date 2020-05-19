#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
step02_DataFrame.py

DataFrame 자료구조 특징
 - 2차원 행렬구조(table 유사함)
 - 열 단위 데이터 처리 용이
 - Series(1차)의 모음 <-> DataFrame(2차)
"""

import pandas as pd
from pandas import Series, DataFrame

# 1. DataFrame 생성

# 1. 기본 자료구조(list, dict) 이용
name = ["hong", "lee", "kang", "yoo"]
age = [35, 45, 55, 25]
pay = [250, 350, 450, 200]
addr= ['서울시', '부산시', '대전시', '인천시']

# dict
data = {"name" : name, "age" : age, "pay" : pay, "addr" : "addr"} # dict
frame = DataFrame(data, columns = ["name", "age", "addr", "pay"])
print(frame)
'''
   name  age  addr  pay
0  hong   35  addr  250
1   lee   45  addr  350
2  kang   55  addr  450
3   yoo   25  addr  200
'''

# 컬럼 추출
age = frame["age"] # or frame.age
print(age.mean())  # 40
print(type(age))   # <class 'pandas.core.series.Series'>

# 새 컬럼 추가
gender = Series(["남", "남", "남", "여"])
frame["gender"] = gender
print(frame)

# 2) numpy 이용 : 선형대수 관련 함수
import numpy as np
frame2 = DataFrame(np.arange(12).reshape(3,4),
					columns = ["a", "b","c","d"])

print(frame2)

# 행/열 통계 구하기
print("열 단위 평군 :", frame2.mean(axis = 0)) # 행축 : 열단위
print("행 단위 평균 :", frame2.mean(axis = 1)) # 열축 : 행단

# 2. DataFrame 컬럼 참조
frame2.index # 행 이름
# Out[95]: RangeIndex(start=0, stop=3, step=1)
frame2.values # 
'''
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
'''

# emp.csv
emp = pd.read_csv("/Users/mac/Desktop/bigdata/Python/4_Python-II/data/emp.csv", encoding = "utf-8")
print(emp.info())

# 단일 컬럼 선택
print(emp["No"])
print(emp.No)     # 컬럼명에 점 포함된 경우 (ㅌx)
print(emp.No[1:]) # 특정 원소 선택

# 2) 복수 컬럼 선택 : 중첩 list
print(emp[["No", "Pay"]])
# print(emp[["No": "Name"]]) # error
print(emp[["No", "Name"]])

# 3. subset 만들기 : old DF -> new DF

# 1) 특정 컬럼 제외 : 컬럼 적은 경우
emp.info()
subset1 = emp[["Name", "Pay"]]
subset1

# 2) 특정 행 제외
subset2 = emp.drop(0)
subset2

# 3) 조건식으로 행 선택
subset3 = emp[emp["Pay"] >= 350] # or emp[emp.Pay >= 350]
subset3

# 4) column 이용 : 컬럼 많은 경우
iris = pd.read_csv("iris.csv")
print(iris.info()) # file info
print(iris.head()) # 앞부분 5개 관측치

iris["Sepal.Width"]
# iris.Sepal.Width Error

cols = list(iris.columns) # 컬럼명 추출
cols
type(cols) # list

iris_x = cols[:4]
iris_y = cols[-1]
iris_x # ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']
iris_y # 'Species'

# x, y 변수 선택
X = iris[iris_x]
y = iris[iris_y]
X.shape # (150, 4) : 2차원
y.shape # (150,)   : 1차원

X.head()
y.head()


# 4. DataFrame 행렬 참조 : DF[row,col]
# 1) DF.loc[row, col]  : label index
# 2) Df.iloc[row, col] : integer index

emp
'''
    No Name  Pay
0  101  홍길동  150
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400
열이름 : No Name Pay
행이름 : 0 ~ 4
'''

# loc[행 lagel index, 열 label index]
emp.loc[1:3, :] # label index
emp.loc[1:3]
emp[1:3, "No":"Name"]
emp.loc[1:3, ["No", "Pay"]]
# emp.loc[1:3, [1:2]]

# iloc[행숫자 index, 열숫자 index]
emp.iloc[1:3] # 숫자 index : 2행
emp.iloc[1:3, :2]
emp.iloc[1:4, [0,2]]
# emp.iloc[1:4, ["No", "Pay"]]

########################
## DF 행렬 참조 example
########################
iris.shape # (150, 5)

from numpy.random import choice

help(choice)
# choice(a, size=None, replace=True, p=None)

row_idx = choice(a = len(iris), size = int(len(iris)*0.7),
				 replace = False)

row_idx
len(row_idx) # 105

# train dataset
train_set = iris.iloc[row_idx]
train_set.head()
train_set.shape # (105, 5)

train_set2 = iris.loc[row_idx]
train_set2.head()
train_set2.shape # (105, 5)

# test dataset : list + for
test_idx = [i for i in range(len(iris)) if not i in row_idx]
len(test_idx) # 45

test_set = iris.iloc[test_idx]
test_set.shape # (45, 5)

# x, y변수 분리
col = list(iris.columns)
x = cols[:4]
y = cols[-1]

iris_x = iris.loc[test_idx, x]
iris_y = iris.loc[test_idx, y]
iris_x.shape # (45,4)
iris_y.shape # (45,)








