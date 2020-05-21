"""  
step06_XGBoost_boston.py

XGBoost 회귀트리 : XGBRegressor
"""
# import test
from xgboost import XGBRegressor
from xgboost import plot_importance
from sklearn.datasets import load_boston
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

# 1. dataset load
boston = load_boston()
x_names = boston.feature_names
X, y = load_boston(return_X_y=True)
X.shape # (506, 13)

y # 비율척도, 비정규화

# 2. split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

# 3. model 생성
xgbr = XGBRegressor()
model = xgbr.fit(x_train, y_train)
model

# 4. 중요변수 시각화
plot_importance(model)
fscore = model.get_booster().get_score()
fscore

# 5. model 평가
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
score = r2_score(y_test, y_pred)
mse
score