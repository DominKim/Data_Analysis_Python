"""  
step03_sklearn_Regression.py

sklearn 관련 Linear Regression
"""

from sklearn.linear_model import LinearRegression        # model object
from sklearn.model_selection import train_test_split     # train /test
from sklearn.metrics import mean_squared_error, r2_score # model 평가
from sklearn.datasets import load_diabetes # dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#######################
## diabates
#######################
# 단순선형회귀 : x(1) -> y

# 1. dataset load
X, y = load_diabetes(return_X_y=True)
X.shape # (442, 10)

y.shape  # (442,)
y.mean() # 152.13348416289594

# 2. x, y 변수
# x(bmi : 비만도지수) -> y
x_bmi = X[:,2]
x_bmi.shape # (442,)

# 1d -> 2d reshape
x_bmi = x_bmi.reshape(-1, 1) # -1 은 지정한 열이나 행에 따라 가변적으로 행 열 지정

# 3. model 생성 : object -> traing -> model
obj = LinearRegression()  # 생성자   -> object
model = obj.fit(x_bmi, y) # (X, y) -> model : x는 2차원 matrix만 가능

# y 예측치
y_pred = model.predict(x_bmi) # predict(X)


# 4. model 평가 : MSE(정규화), r2_score(비정규화)
MSE = mean_squared_error(y, y_pred) # (y 정답, y 예측치)
score = r2_score(y, y_pred)         # (y 정답, y 예측치)
print("mse =", MSE)        # mse = 3890.4565854612724
print("r2score = ", score) # r2score =  0.3439237602253803

# 5. dataset split(70 : 30)
x_train, x_test, y_train, y_test = train_test_split(
    x_bmi, y, test_size = 0.3)

x_train.shape # (309,1)
x_test.shape  # (133,1)

# model 생성
obj = LinearRegression() # 생성자 -> object
model = obj.fit(x_train, y_train)

y_pred = model.predict(x_test)

# model 평가 : MSE(정규화), r2_score(비정규화)
MSE = mean_squared_error(y_test, y_pred)
score = r2_score(y_test, y_pred)

df = pd.DataFrame({"y_true":y_test, "y_pred":y_pred})
cor = df["y_true"].corr(df["y_pred"])
cor # 0.5729723593468679

plt.plot(x_test, y_test, "ro")
plt.plot(x_test, y_pred, "b-")


###############
## iris.csv
###############
# 다중회귀모델 : y(1) <- x(2 ~ 4)

# 1. dataset load
iris = pd.read_csv("../../../data/iris.csv")
iris.info()
"""  
Sepal.Length    150 non-null float64 -> y
Sepal.Width     150 non-null float64 -> x1
Petal.Length    150 non-null float64 -> x2
Petal.Width     150 non-null float64 -> x3
Species         150 non-null object
"""

# 2. x,y 변수 선택
iris.columns = iris.columns.str.replace(".", "_")
cols = list(iris.columns)

y_cols = cols[0]
x_cols = cols[1:4]
x_cols


# 3. dataset split(70:30)
iris_train, iris_test = train_test_split(iris, test_size = 0.3, 
random_state = 123) # default = 0.25
"""  
test_size : 검정데이터셋 비율(default = 0.25)
random_state : sampling seed값
"""
iris_train.shape
iris_test.shape

# 4. model 생성 : train data
lr = LinearRegression()
model = lr.fit(X=iris_train[x_cols], y = iris_train[y_cols])
model # object info

# 5. model 평가 : test data
y_pred = model.predict(X= iris_test[x_cols]) # 예측치
# numpy.ndarray로 반환

y_true = iris_test[y_cols] # 관측치(정답) = label

y_true.min() # 4.4
y_true.max() # 7.6

# 평균제곱오차 : mean((y_true - y_pred)**2)
mse = mean_squared_error(y_true, y_pred)
score = r2_score(y_true, y_pred)
print("MSE =", mse)        # MSE = 0.08427309395784154(0 기준)(오차)
print("r2 score =", score) # r2 score = 0.8655788590634174(1 기준)(85%)

# y_true vs y_pred 시각화
y_true # Series
y_true = np.array(y_true)
y_pred

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,5))
chart = fig.subplots()
chart.plot(y_true,c = "b", ls = "-", marker = "", label = "real values")
chart.plot(y_pred, c = "r", ls = "-", marker = "", label = "predict")
plt.legend(loc = "best")
plt.show()