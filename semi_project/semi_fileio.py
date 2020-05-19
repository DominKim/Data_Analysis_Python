#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:24:42 2020

@author: mac
"""

import pandas as pd 

import glob
import os
import re

input_file = r"/Users/mac/Desktop/bigdata/Python/4_Python-II/workspace/semi_project/raw_data"

output_file = r"/Users/mac/Desktop/bigdata/Python/4_Python-II/workspace/semi_project/raw_data/stock.csv"

allfile_list = glob.glob(os.path.join(input_file, "*.csv"))
print(allfile_list)

# 각 회사명 추출
company_lst = []
for row in allfile_list:
    company = re.sub("/Users/mac/Desktop/bigdata/Python/4_Python-II/workspace/semi_project/raw_data/", "", row)
    company_lst.append(company)

name = {"company" : [], "industry" : []}

for i in company_lst:
    name["company"].append(i.split("_")[0])
    name["industry"].append(i.split("_")[1])


all_data = []
cnt = 0

for file in allfile_list:
    df = pd.read_csv(file, engine = "python", encoding = "euc-kr")
    df["company"] = name["company"][cnt]
    df["inudstry"] = name["industry"][cnt]
    all_data.append(df)
    cnt += 1

dataComine = pd.concat(all_data, axis = 0, ignore_index = True)
dataComine.to_csv(output_file, index = None, encoding = "utf-8")

data = pd.read_csv("/Users/mac/Desktop/bigdata/Python/4_Python-II/workspace/semi_project/raw_data/stock.csv", encoding="utf-8")

try:
    for i in range(len(data)):
        data.iloc[:,i] = data.iloc[:,i].str.replace(",", "")
except Exception as e:
    print("예외 발생 :", e)
finally:
    print("처리 완료")

# str > int
for i in range(1,18):
    data.iloc[:,i] = pd.to_numeric(data.iloc[:,i])

# re save
data.to_csv(output_file, index = None, encoding = "utf-8")

# read
stock = pd.read_csv(output_file, encoding="utf-8")
stock.info()
stock.head()

# 결측치 행 제거 axis = 0, 열 제거 axis = 1
stock1 = stock.dropna()
stock1.head()

