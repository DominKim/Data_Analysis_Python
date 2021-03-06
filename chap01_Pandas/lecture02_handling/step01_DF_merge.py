#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
step01_DF_merge.py

DataFame 병합(merge)
 ex) DF1(id) + DF2(id) -> DF3
"""

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# 1. Series merge : 1차원
s1 = Series([1,3], index = ["a", "b"])
s2 = Series([5, 6, 7], index = ["a", "b", "c"])
s3 = Series([11, 13], index = ["a", "b"])

# 행 단위 결합 : rbind()
s4 = pd.concat([s1, s2, s3], axis = 0) # 행 결합
s4.shape # (7,)

# 열 단위 결합 : cbind()
s5 = pd.concat([s1, s2, s3], axis = 1) # 열 결합
s5.shape # (3,3) 2차원
s5

# 2. DataFrame 병합
wdbc = pd.read_csv("wdbc_data.csv")
print(wdbc.info())
'''
RangeIndex: 569 entries, 0 to 568
Data columns (total 32 columns):
'''

# DF1(16) + DF2(16)
cols = list(wdbc.columns)
len(cols) # 32

DF1 = wdbc[cols[:16]] # [["]]
DF1.shape # (569, 16)

DF2 = wdbc[cols[16:]]
DF2.shape # (569, 16)

# id 컬럼 추가
id = wdbc.id
DF2["id"] = id
DF2.shape # (569, 17)
DF2.head()

# 병합 ! 공통의 컬럼이 필요
DF3_merge = pd.merge(DF1, DF2)
DF3_merge.info()
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 569 entries, 0 to 568
Data columns (total 32 columns):
'''

# 결합 : 컬럼 단위 결합
DF1 = wdbc[cols[:16]] # [["]]
DF1.shape # (569, 16)

DF2 = wdbc[cols[16:]]
DF2.shape # (569, 16)

DF4 = pd.concat([DF1, DF2], axis = 1) # 열 단위
DF4.info()