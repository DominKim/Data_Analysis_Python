'''
step05_regression.py

scipy 패키지의 stats 모듈의 함수
 - 통계적인 방식의 회귀분석
 1. 단순선형회귀모델
 2. 다중선형회귀모델
'''

from scipy import stats # 회귀모델 생성
from statsmodels.formula.api import ols # 다중선형회귀모델 
import pandas as pd

# 1. 단순선형회귀모델
'''
x -> y
'''

score_iq = pd.read_csv("/Users/mac/Desktop/bigdata/Python/4_Python-II/data/score_iq.csv")
score_iq.info()

x = score_iq.iq
y = score_iq["score"]

# 회귀모델 생성
model = stats.linregress(x,y)
model
'''
slope=0.6514309527270075      : 기울기
intercept=-2.8564471221974657 : 절편
rvalue=0.8822203446134699     : 설명력
pvalue=2.8476895206683644e-50 : x의 유의성 검정
stderr=0.028577934409305443   : 표본 오차
'''

print("x 기울기 =", model.slope)
print("y 절편 =", model.intercept)
'''
x 기울기 = 0.6514309527270075
y 절편 = -2.8564471221974657
'''

score_iq.head(1)
'''
	sid	score	iq	academy	game	tv
0	10001	90	140	2	1	0
'''
# y = X * a _ b
X = 140
y_pred = 140* model.slope + model.intercept
y_pred # 88.34388625958358

Y = 90
err = Y - y_pred
err # 1.6561137404164157

#################
# product.csv
#################
import os
os.getcwd()
product = pd.read_csv("../../../data/product.csv")

product.corr()

# x : 제품적절성 vs y : 제품만족도
model2 = stats.linregress(product["b"], product["c"])
model2

product.head(1)

X = 4
y_pred = X * model2.slope + model2.intercept
y_pred # 3.735963048858919
Y = 3
err = (Y - y_pred) ** 2
err # 0.5416416092857157

X = product["b"]
y_pred = X*model2.slope + model2.intercept
Y = product["c"]

len(y_pred)

# 2. 회귀모델 시각화
from pylab import plot, legend, show

plot(product["b"], product["c"], c = "b", ls = "", marker = ".")
plot(product["b"], y_pred, c = "r", ls = "-", marker = "")
legend(["x,y scatter", "regress model line"])
show()

# 3. 다중선형회귀모델 : y ~ x1 + x2, ...
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt

wine = pd.read_csv("../../../data/winequality-both.csv")
wine.info()
wine.columns = wine.columns.str.replace(" ", "_")

# quality vs other
cor = wine.corr()
formula = "quality ~ alcohol + chlorides + volatile_acidity"
model = ols(formula, data = wine).fit() # model 생성(.fit())

model # object info

model.summary()
'''
Adj. R-squared:	0.259 -> 설명력
F-statistic:	758.6
Prob (F-statistic):	0.00 < 0.05 : 모델 유의성 검정
x의 유의성 검정
'''

# 기울기,절편
model.params
type(model.params)
'''
Intercept           2.909941
alcohol             0.319578
chlorides           0.159258
volatile_acidity   -1.334944
'''

# y의 예측치 vs 관측치
y_pred = model.fittedvalues # 예측치
y_true = wine["quality"]    # 관측치

# 차트확인
import matplotlib.pyplot as plt

plt.plot(y_true[:50], "b", label = "real values")
plt.plot(y_pred[:50], "r", label = "y prediction")
plt.yticks(range(0,10))
plt.legend(loc = "best")
plt.show()