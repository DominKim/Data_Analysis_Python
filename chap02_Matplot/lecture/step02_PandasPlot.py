# -*- coding: utf-8 -*-
"""
step02_PandasPlot.py

Pandas 객체에서 지원하는 시각화
 형식) object.plot(kind = 차트유형)
    object : Sries or DataFrame
    kind   : bar, barh, pie, hist, kde(히스토그램을 밀도분포 곡선으로), box, scatter
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1. Sreis 객체 시각화
# pd.index : 데이터가 저장되어 있는 위
ser = pd.Series(np.random.randn(10), index = np.arange(0,100,10))
print(ser)

ser.plot()

# 2. DataFrame 객체 시각화
df = pd.DataFrame(np.random.randn(10,4),
                  columns = ["one", "two", "three", "four"])
df.shape # (10, 4)

# 기본 차트
df.plot() # 

# 세로 막대 차트
df.plot(kind = "bar", title = "bar plot")

# 가로 막대 차트
df.plot(kind = "barh", title = "barh plot")

# 가로 막대차트, 누적형
df.plot(kind = "barh", title = "bar plot", stacked = True)

# 도수분포(히스토그램)
df.plot(kind = "hist", title = "histogram")

# 커널밀도추정 : kde
df.plot(kind = "kde", title = "Kernel Density Estimate plot")

'''
tips.csv 적용
'''
tips = pd.read_csv("tips.csv")
tips.info()
tips.head()

tips.plot(kind = "kde")

# 요일(day) vs 파티규모(size)
tips["day"].unique() # ['Sun', 'Sat', 'Thur', 'Fri']
tips["size"].unique() # [2, 3, 4, 1, 6, 5]
tab = pd.crosstab(tips["day"], tips["size"])
print(tab)
'''
size  1   2   3   4  5  6
day                      
Fri   1  16   1   1  0  0
Sat   2  53  18  13  1  0
Sun   0  39  15  18  3  1
Thur  1  48   4   5  1  3
'''
type(tab) # pandas.core.frame.DataFrame

tab_result = tab.loc[:,2:5]
tab_result

tab_result.plot(kind = "barh", stacked = True, title = "day vs size columns plot")

# 3. 산점도 matrix
from pandas import plotting
iris = pd.read_csv("iris.csv")
iris.info()

cols = list(iris.columns)
iris_x = iris[cols[:4]]

plotting.scatter_matrix(iris_x)

# 4. 3d 산점도
from mpl_toolkits.mplot3d import Axes3D

col1 = iris[cols[0]]
col2 = iris[cols[1]]
col3 = iris[cols[2]]
col4 = iris[cols[3]]

cdata = [] # 빈 list
for s in iris["Species"]:
    if s == "setosa":
        cdata.append("hotpink")
    elif s == "versicolor":
        cdata.append("grey")
    else:
        cdata.append("blue")

fig = plt.figure()
chart = fig.add_subplot(1,1,1, projection = "3d")

chart.scatter(col1, col2, col3, c = cdata) # (x, y, z)
chart.set_xlabel("col1")
chart.set_ylabel("col2")
chart.set_zlabel("col3")


