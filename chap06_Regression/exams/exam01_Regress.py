﻿'''
문) load_boston() 함수를 이용하여 보스턴 시 주택 가격 예측 회귀모델 생성 
  조건1> train/test - 7:3비울
  조건2> y 변수 : boston.target
  조건3> x 변수 : boston.data
  조건4> 모델 평가 : MSE, r2_score
'''

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import numpy as np
import pandas as pd

# 1. data load
boston = load_boston()
print(boston)


# 2. 변수 선택
x = boston.data
y = boston.target


# 3. train/test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)


# 4. 회귀모델 생성 : train set
obj = LinearRegression()
model = obj.fit(x_train, y_train)
model
y_pred = model.predict(x_test)

# 5. 모델 평가 : test set
mse = mean_squared_error(y_test, y_pred)
mse
score = r2_score(y_test, y_pred)
score