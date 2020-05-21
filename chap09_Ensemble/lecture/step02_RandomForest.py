"""  
step02_RandomForest.py

Random Forest Ensemble model
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# 1. dataset load
wine = load_wine()
names = wine.feature_names # x변수명
wine.target_names

X = wine.data
y = wine.target

X.shape # (178, 13)

# 2. RF model
rf = RandomForestClassifier()
"""  
n_estimators : integer, optional(default = 100) : tree 갯수
criterion : string, optional (default="gini") or "entropy" : 중요변수 선정 기준
max_depth : integer or None, optional (default=None) tree 깊이 ! 모델생성에서 자동 설정
min_samples_split : int, float, optional (default=2) 노드 분할 최소 샘플수
min_samples_leaf : int, float, optional (default=1)  단노드 분할 최소 샘플수
max_features : int, float, string or None, optional (default="auto") 최대 x 변수 사용수
n_jobs : int or None, optional (default=None) cpu 수
random_state : int, RandomState instance or None, optional (default=None)
"""
rf
help(rf)

import numpy as np
idx = np.random.choice(a = X.shape[0], size=int(X.shape[0]*0.7), replace=False)

X_train = X[idx, :]
y_train = y[idx]

model = rf.fit(X_train, y_train)

idx_test = [i for i in range(X.shape[0]) if i not in idx]
X_test = X[idx_test]
y_test = y[idx_test]

y_pred = model.predict(X_test)
y_true = y_test
y_pred

report = classification_report(y_true, y_pred)
report
model.feature_importances_