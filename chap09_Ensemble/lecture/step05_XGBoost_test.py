"""  
step05_XGBoost_test.py

XGBoost model : 분류트리

> pip isntall xgboost
"""

# import test
from xgboost import XGBClassifier
from xgboost import plot_importance
from sklearn.datasets import make_blobs
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
from pandas import plotting

# 1. dataset load
X, y = make_blobs(n_samples=2000, n_features = 4, centers = 3, cluster_std=2.5)
"""  
n_samples   : 데이터셋 크기
n_features  : x변수
centres     : y변수 범주
cluster_std : 클러스터 표준편차
"""
plt.scatter(X[:,0], X[:,1], s = 100, c = y, marker="o", alpha=0.5)
pd.DataFrame(X).plot(kind = "kde")
plotting.scatter_matrix(pd.DataFrame(X), c)
# 2. train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

# 3. model 생성
xgb = XGBClassifier()
model = xgb.fit(x_train, y_train)
model
# objective = "binary:logistic"(sigmoid) -> 이항분류
# objective = "multi:softporb"(softmax) -> 다항분류
# n_estimators : tree 수
# max_depth : tree 깊이
# learning_rate = 0.3 : 학습률(숫자가 낮을수록 정확도가 높아진다.)

# 4. model 평가
y_pred = model.predict(x_test)

acc = accuracy_score(y_test, y_pred)
acc # 0.9783333333333334

report = classification_report(y_test, y_pred)
print(report)
"""  
precision    recall  f1-score   support

           0       1.00      0.99      0.99       213
           1       0.94      0.99      0.97       184
           2       0.99      0.96      0.97       203

    accuracy                           0.98       600
   macro avg       0.98      0.98      0.98       600
weighted avg       0.98      0.98      0.98       600
"""

# 5. 중요변수 시각화
fscore = model.get_booster().get_fscore()
fscore # {'f2': 337, 'f3': 322, 'f0': 206, 'f1': 292}
plot_importance(model)