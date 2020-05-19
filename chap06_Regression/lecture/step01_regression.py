'''
step01_regression.py

회귀방정식에서 기울기(slope)와 절편(intercept)식
    기울기(slope) = Cov(X, Y) / Sxx(x의 편차 제곱 평균)
    절편(intercept) = y_mu - (slope * x_mu)
'''

from scipy import stats # 회귀모델
import pandas as pd     # csv file read
import numpy as np

galton = pd.read_csv("../../../data/galton.csv")
galton.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 928 entries, 0 to 927
Data columns (total 2 columns):
child     928 non-null float64
parent    928 non-null float64
'''

# x,y 변수 선택
x = galton.parent
y = galton["child"]

# model 생성
model = stats.linregress(x, y)
""" 
slope=0.6462905819936423, 
intercept=23.941530180412748, 
rvalue=0.4587623682928238, 
pvalue=1.7325092920142867e-49, 
stderr=0.04113588223793335
"""

# Y = x * a(기울기) + b(절편)
y_pred = x * model.slope + model.intercept
y_pred

y_true = y

# 예측치 vs 관측치(정답)
y_pred.mean() # 68.08846982758534
y_true.mean() # 68.08846982758512

# 1. 기울기 계산식
# 기울기(slope) = Cov(x, y) / Sxx(x의 편차 제곱 평균)
xu = x.mean() # x_mu
yu = y.mean() # y_mu

Cov_xy = sum((x - xu) * (y - yu)) / len(x)
Cov_xy # 2.062389686756837

Sxx = np.mean((x - xu) ** 2)
Sxx # 3.1911182743757336

slope = Cov_xy / Sxx
slope # 0.6462905819936413

# 2. 절편 계산식
# 절편(intercept) = y_mu - (slope * x_mu)

intercept = yu - (slope * xu)
intercept # 23.94153018041171

# 3. 설명력(rvalue)
# rvalue = 0.4587623682928238
galton.corr()
"""  
	       child	parent
child	1.000000	0.458762
parent	0.458762	1.000000
"""

y_pred = x * slope + intercept

y_pred.mean() # 68.08846982758423
