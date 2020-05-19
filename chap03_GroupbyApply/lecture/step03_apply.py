'''
step03_apply.py

1. group 객체에 외부 함수 적용
 - obj.apply(func1)
 - obj.agg([func1, func2, ...])

2. data 정규화
'''

import pandas as pd

# 1. group 객체에 외부 함수 적용
'''
apply vs agg
 - 공통점 : 그룹 객체에 외부 함수 적용(df도 가능)
 - 차이점 : 적용할 함수의 개수
'''

# apply()
test = pd.read_csv("../../../data/test.csv")
test.info()

grp = test["data2"].groupby(test["key"])
grp.size()
grp.sum()
grp.max()
grp.min()

# 사용자 정의함수
def diff(grp):
    result = grp.max() - grp.min()
    return result

# 내장함수 적용
grp.apply(sum)
grp.apply(max)
grp.apply(min)

# 사용자함수 적용
grp.apply(diff)
'''
key
a      0
b    100
'''

# agg([func1, func2, ...]) : bulitin 함수는 "", 사용자 정의 함수는 x
agg_func = grp.agg(["sum", "max", "min", diff])
agg_func

# 2. data 정규화:
# - 다양한 특징을 갖는 변수를 대상으로 일정한 범위로 조정
# - x(30) -> y

import numpy as np # max, min, log

# 1) 사용자 함수 : 0 ~ 1
def normal(x):
    n = (x - np.min(x)) / (np.max(x) - np.min(x))
    return n

x = [10, 20000, -100, 0]

normal(x)
# array([0.00547264, 1.        , 0.        , 0.00497512])

# 2) 자연 log
np.log(x) # 밑수 e : 음수, 영 -> 결측치, 무한대
# array([2.30258509, 9.90348755,        nan,       -inf])

e = np.exp(1)
e # 2.718281828459045

# 로그 -> 지수값(8 = 2^3)
np.log(10) # 밑수 e : 2.302585092994046 = e^2.3025
e**2.3025 3 9.99

# 지수 -> 로그값
np.exp(2.3025)  # 10.00
'''
로그 vs 지수 역함수 관계
 - 로그 : 지수값 반환
 - 지수 : 로그값 반환
'''

iris = pd.read_csv("../../../data/iris.csv")
# 전체 컬럼명 가져오기
cols = list(iris.columns)
cols # ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']

iris_x = iris[cols[:4]]
iris_x.shape # (150, 4)
iris_x.head()

# x변수 정규화
iris_x_nor = iris_x.apply(normal)
iris_x_nor.head()

iris_x.agg(["var","mean","max","min"])
train = iris_x_nor.sample(round(len(iris_x_nor) * 0.7))
test = iris_x_nor.drop(train.index)
