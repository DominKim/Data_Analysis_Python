"""  
step07_XGBoost_parameter.py

1. XGBoost Hyper Parameter
2. model 학습 조기종료 : early stopping rounds
3. Best Hyper Parameter : Grid Search
"""

from xgboost import XGBClassifier
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, r2_score, classification_report
from sklearn.model_selection import train_test_split, GridSearchCV

# 1. XGBoost Hyper Parameter
X, y = load_breast_cancer(return_X_y=True)

X.shape # (569, 30)
y # 0 or 1

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

xgb = XGBClassifier(colsample_bylevel=1,
learning_rate=0.3,
max_depth=6,
min_child_weight=1,
n_estimators=100)

model = xgb.fit(x_train, y_train)
model
"""  
colsample_bylevel=1         : tree model 생성시 훈련셋의 샘플링 비율(0.6 ~ 1)
learning_rate=0.3           : 학습율(0.01 ~ 0.1)
max_depth=6                 : 트리 깊이, 과적합 영향
min_child_weight=1          : 자식 노드 분할 결정하는 최소 가중치 합
n_estimators=100            : 트리 모델 수
objective='binary:logistic' : 이항과 다항분류 결정
"""


# 2. model 학습 조기종료 : early stoppng rounds
eval_set = [(x_test, y_test)]

model_early = xgb.fit(x_train, y_train, eval_set = eval_set,
eval_metric="error", early_stopping_rounds=50, verbose=True)
"""  
X, y : 훈련셋
eval_set : 평가셋
eval_metric : 평가방법(이항분류 :error, 다항분류 : merror, 회귀 : rmse)
early_stopping_rounds : 학습조기종료
verbose : 학습 -> 평가 출력여부
"""

score = model_early.score(x_test, y_test)
score # 0.9532163742690059

# 3. Best Hyper Parameter : Grid Search
from sklearn.model_selection import GridSearchCV

# default model object
xgb = XGBClassifier()

params = {"colsample_bylevel":[0.6,0.8,1],
"learning_rate":[0.01,0.1],
"max_depth":[3,5],
"min_child_weight":[1,3],
"n_estimators":[100,300]}

gs = GridSearchCV(xgb, params, cv = 5, n_jobs = -1)

model = gs.fit(x_train, y_train, eval_set = eval_set,
eval_metric = "error", verbose = True)

# best score
model.best_score_ # 0.9698492462311558

# best parameter
model.best_params_
"""  
{'colsample_bylevel': 0.8,
 'learning_rate': 0.1,
 'max_depth': 3,
 'min_child_weight': 1,
 'n_estimators': 300}
"""
model.best_estimator_.feature_importances_
