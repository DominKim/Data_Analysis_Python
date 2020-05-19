"""  
step02_dot_regression.py

행렬곱 함수(np.dot) 이용 y 예측치 구하기
 y_pred = np.dot(X, a) + b

** 수치가 높을 수록 더 많은 영향을 미침**
np.dot(X, a) 전제조건
 1. X, a : 행렬 구조
 2. 수일치 : X열 차수 = a행 차수
"""
from scipy import stats                 # 단순회귀모델 - dot(x) 행렬을 만들지 못한다.
from statsmodels.formula.api import ols # 다중회귀모델
import pandas as pd                     # csv file load
import numpy as np

# 1.dataset load
score = pd.read_csv("../../../data/score_iq.csv")
score.info()
"""  
sid        150 non-null int64
score      150 non-null int64 -> y
iq         150 non-null int64 -> x1
academy    150 non-null int64 -> x2
game       150 non-null int64
tv         150 non-null int64
"""

formula = "score ~ iq + academy"
model = ols(formula, data = score).fit()

model.params
"""  
model.params
Intercept    25.229141
iq            0.376966
academy       2.992800
"""

# model 결과 확인
model.summary()

# model 예측치
model.fittedvalues

# y_pred = np.dot(X, a) + b

X = score[["iq", "academy"]]
X.shape # (150, 2)
"""  
np.dot(X, a) 전제조건
 1. X, a : 행렬 구조
 2. 수일치 : x열 차수 = a행 차수
"""
# list -> numpy array
a = np.array([[0.376966], [2.992800]])
a.shape # (2, 1)

matmul = np.dot(X, a) # 행렬곱
matmul.shape # (150, 1) = X([150], 2)/ a(2,[1])

b = 25.229141       # 절편
y_pred = matmul + b # broadcast(2차원 + 0차원)
y_pred.shape        # (150,1)

# 2차원 -> 1차
y_pred1d = y_pred.reshape(150)
y_pred1d.shape # (150,)

y_true = score["score"]
y_true.shape # (150,)

df = pd.DataFrame({"y_true":y_true, "y_pred":y_pred1d})
df.head()
df.tail()

cor = df["y_true"].corr(df["y_pred"])
cor # 0.9727792069594754