"""  
step01_Pipeline_GridSearch.py

Pipeline vs Grid Search
 1. SVM model
 2. Pipeline : model workflow (dataset 전처리 -> model -> test)
 3. Grid Search : model tuning
"""

from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline

# 1. SVM model

# 1) dataset load
X,y = load_breast_cancer(return_X_y= True)

# 2) X변수 정규화 : 전처리
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
X_scaled.mean(axis = 0)

x_train, x_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state = 123)

# 3) SVM model 새성
svc = SVC(gamma = "auto")
model = svc.fit(x_train, y_train)

# 4) model 평가
score = model.score(x_test, y_test)
score # 0.9590643274853801

# 2. Pipeline : model workflow

# 1) pipeline step : [(step1:scaler), (step), ..]
pipe_svc = Pipeline([("scaler", MinMaxScaler()), ("svc", SVC(gamma = "auto"))])

# 2) pipeline model
model = pipe_svc.fit(x_train, y_train)

# 3) pipeline model test
score = model.score(x_test, y_test)
score # 0.9590643274853801

# 3. Grid Search : model tuning
# Pipeline -> Grid Search -> model tuning

help(SVC)
# C=1.0, kernel='rbf', gamma='auto'

# 1) params 설정
params = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]

# dict 형식 = {"object__c" : params_range}
params_grid = [{"svc__C":params, "svc__kernel":["linear"]},
{"svc__C":params, "svc__gamma":params, "svc__kernel":["rbf"]}]

# 2) GridSearchCV
gs = GridSearchCV(estimator=pipe_svc, param_grid=params_grid,
scoring="accuracy", cv = 10, n_jobs=1)
# score : 평가방법, cv : 교차검정, n_jobs : cpu ㅛㅜ

model = gs.fit(x_train, y_train)
model.best_score_
# best score
acc = model.score(x_test, y_test)
acc # 0.9883040935672515

# best parameter
model.best_params_
# {'svc__C': 1.0, 'svc__gamma': 1.0, 'svc__kernel': 'rbf'}

