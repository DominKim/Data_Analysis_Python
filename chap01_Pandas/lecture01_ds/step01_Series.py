#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
step01_Series.py

Series 객체 특징
 - 1차원의 배열구조
 - 수학/통계 함수 제공
 - 범위 수정, 블럭 연산
 - indexing / slicing
 - 시계열 데이터 생성
 - 표 형식의 데이터, 다양한 데이터를 다루는 데 초점
 - dict 형 대체 하여 사용
"""

import pandas as pd
from pandas import Series, DataFrame

# 1. Series 객체 생성

# 1) list 이용
lst = [4000, 3000, 3500, 2000]
ser = pd.Series(lst)
print("lst =", lst)
print("ser = ", ser)

# object.member
print(ser.index)   # 색인
# RangeIndex(start=0, stop=4, step=1)
print(ser.values) # 값
# [4000 3000 3500 2000]

print(ser[0]) # 4000

ser1_2 = Series([4000, 3000, 3500, 2000],
                index = ['a', 'b', 'c', 'd'])
print(ser1_2.index)
# Index(['a', 'b', 'c', 'd'], dtype='object')
print(ser1_2.values)

# 2) dict 이용
person = {"name" : "이순신", "age":35, "add" : "서울시"}
ser2 = Series(person)
print("ser2", ser2)
'''
name    이순신
age      35
add     서울시
'''
print(ser2.index)
print(ser2.values)

# index 사용 : object[n or 조건식]
print(ser2["age"]) # 35

# boolean 조건식
print(ser[ser >= 3000])
'''
0    4000
1    3000
2    3500
'''

# 3) name 생성
ser.name = "끼끼"
ser.index.name = "까까"

# 2. indexing : list 동일
ser3 = pd.Series([4, 4.5, 6, 8, 10.5]) # 생성
print(ser3[0])  # 4.0 
print(ser3[:3]) # 0 ~ 2
print(ser3[3:]) # 3 ~ n
# print(ser3[-1]) # KeyError 음수 객체 사용 불가

# 3. Series 결합과 NA 처리
p1 = Series([400, None, 350, 200],
		   index = ["a", 'b', "c", 'd'])
p2 = Series([400, 150, 350, 200],
		   index = ["a", 'c', "d", 'e'])

# Series 결합
p3 = p1 + p2
print(p3)
'''
a    800.0
b      NaN
c    500.0
d    550.0
e      NaN
'''

# 4. 결측치 처리 방법(평균, 0, 제거)
print(type(p3))
# <class 'pandas.core.series.Series'>

# 1) 평균 대체
p4 = p3.fillna(p3.mean())
print(p4)

# 2) 0 대체
p5 = p3.fillna(0)
print(p5)

# 3) 결측치 제거
p6 = p3[pd.notnull(p3)] # subset
print(p6)
'''
a    800.0
c    500.0
d    550.0
'''
 
# 5. 범위 수정, 블럭 연산
print(p2)
'''
a    400
c    150
d    350
e    200
'''

# 1) 범위 수정
p2[1:3] = 300
print(p2)
'''
a    400
c    300
d    300
e    200
'''

# list에서는 불가능
# lst = [1, 2, 3, 4]
# lst[1:3] = 3

# 2) 블럭 연산
print(p2 + p2) # 2배
print(p2 - p2)

# 3) brodcast 연산(1차 vs 0차)
v1 = pd.Series([1, 2, 3, 4])
scala = 0.5

b = v1 * scala # vector(1) 8 scala(0)
print(b)
'''
0    0.5
1    1.0
2    1.5
3    2.0
'''

# 4) 수학 / 통계 함수
print("sum =", v1.sum())
print("mean =", v1.mean())
print("var =", v1.var())
print("std =", v1.std())
print("max =", v1.max())

# 호출 가능한 멤버 확인
dir(v1)

print(v1.shape) # (4,)
print(v1.size)  # 4
