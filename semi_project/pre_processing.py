import pandas as pd
import numpy as np
from re import sub, findall

stock = pd.read_csv("/Users/mac/Desktop/bigdata/Python/4_Python-II/workspace/semi_project/raw_data/stock.csv", encoding="utf-8")

# PER, EPS, 영익증가, 지배EPS 제거
stock = stock.drop(["PER", "EPS", "영익증가", "지배EPS"], axis = 1)

# 결측치 행 확인 및 제거 

# subset
stock_df = stock.iloc[:6142,:]
stock_df.head()
stock_df["year"] = None
stock_df["quarter"] = None

# 연도, 분기 분류
for i in range(len(stock_df)):
    stock_df["year"][i] = sub("년", "",findall("..년", stock_df.결산년도[i])[0])
    stock_df["quarter"][i] = findall("[1-4]Q", stock_df.결산년도[i])[0]
stock_df.head()
_ = pd.to_numeric(stock_df.year)
stock_df.info()

# drop 조건식
# df = df.drop(df[<some boolean condition>].index)
stock_df = stock_df.drop(stock_df[stock_df["year"] == 10].index)
stock_df.tail()
stock_df = stock_df.dropna(thresh = 16)
# 결측치 여러개 행 제거
stock_df.shape # (5705, 18)

# 결측치 가진 회사 년도
no_dic = {"company" : [], "year": []}


# 결측치 가진 행 추출
stock1 = stock_df.dropna()
idx = []

for i in stock_df.index:
    if i not in stock1.index:
        idx.append(i)
stock_no = stock_df.loc[idx,:]

# 결측치 가진 회사 년도 추가
for i in stock_no[["company", "year"]].values:
    no_dic["company"].append(i[0])
    no_dic["year"].append(i[1])

dica = {}
for i in range(len(no_dic["company"])):
    dica[no_dic["company"][i]] = dica.get(no_dic["company"][i], 0) + 1

real_dict = {}
for key, value in dica.items():
    real_dict[key] = []
    for i in range(value):
        real_dict[key].append(no_dic["year"][i])

new_dict = {}
for key, value in real_dict.items():
    a = set(value)
    new_dict[key] = list(a)
new_dict

# 결측치 각 column 평균으로 대체
for key, value in new_dict.items():
    for i in value:
        stock_df[(stock_df["company"] == key) & (stock_df["year"] == i)] = stock_df[(stock_df["company"] == key) & (stock_df["year"] == i)].fillna(stock_df[(stock_df["company"] == key) & (stock_df["year"] == i)].mean())

# 결측치 앞에 행 으로 채우기        
stock_df = stock_df.fillna(method = "ffill")
stock_df.isnull().sum()



# 최종 결측치 처리 값 저장
stock_df.to_csv("/Users/mac/Desktop/bigdata/Python/4_Python-II/workspace/semi_project/raw_data/f_stock.csv", index = None, encoding = "utf-8")            