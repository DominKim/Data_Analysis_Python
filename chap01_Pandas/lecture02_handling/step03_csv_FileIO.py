#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
step03_csv_FileIO.py

1. csv file read
2. csv file write
3. random sampling
"""

import pandas as pd

# 1. csv file read
iris = pd.read_csv("iris.csv")
iris.info()

# 컬럼명 : 특수문자 or 공백 -> 문자 변경
iris.columns = iris.columns.str.replace(".", "_")
iris.head()

# 컬럼명이 없는 경우
st = pd.read_csv("student.csv", header = None)
st #   0     1    2   3
col_name = ["학번", "이름", '키', '몸무게']
st.columns = col_name
st

# 행 이름 변경
# st.index = 수정 값

# 체질량 지수(BMI)
# BMI = 몸무게 / 키**2 
BMI = [st.loc[i,"몸무게"] / (st.loc[i,"키"]*0.1)**2 for i in range(len(st))]
print(BMI)
type(BMI)

st["bmi"] = BMI
st["bmi"] = st["bmi"].round(2)
st

# 2. csv file write
st.to_csv("student_df.csv", index = None, encoding = "utf-8")
# index : 행이름 저장여부

st_df = pd.read_csv("student_df.csv")
st_df.info()
st_df

# 3. random sampling
wdbc = pd.read_csv("wdbc_data.csv")
wdbc.info()

wdbc_train = wdbc.sample(round(len(wdbc) * 0.7))
wdbc_train.shape # (398, 32)

wdbc_train.head()
wdbc_train.index
wdbc_test = wdbc - wdbc_train
wdbc.shape
wdbc_test = wdbc.drop(wdbc_train.index)
wdbc_test.shape



