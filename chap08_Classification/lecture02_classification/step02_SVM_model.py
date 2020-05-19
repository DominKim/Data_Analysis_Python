"""  
step02_SVM_model.py

SVM model 
 - 선형 SVM, 비선형 SVM
 - Hyper parameter(kernel, C, gamma)
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from scipy import stats

# 1. dataset load
iris = pd.read_csv("../../../data/iris.csv")
iris.info()

# 2 . x,y 변수 선택
cols = list(iris.columns)
cols

x_cols = cols[:4]
y_cols = cols[-1]

# 3. train(60) / test(40) split
train, test = train_test_split(iris, test_size = 0.4, random_state = 123)

# 4. SVM model 생성
svc = SVC(C = 1.0, gamma="auto", kernel="rbf") # 비선형 SVM model 생성
# default : C = 1.0, kernel = "rbf"(비선형 옵션)

svc2 = SVC(C= 1.0,kernel="linear") # 선형 SVM model

model = svc.fit(X = train[x_cols], y = train[y_cols])
model2 = svc2.fit(X = train[x_cols], y = train[y_cols])

# 5. model 평가
y_pred = model.predict(X = test[x_cols])
y_true = test[y_cols]

y_pred2 = model2.predict(X = test[x_cols])

acc = accuracy_score(y_true, y_pred)
acc
acc2 = accuracy_score(y_true, y_pred2)
acc2

###################
### Grid Search
###################
# Hyper parameter(Kernel, C, gamma)

# C, gamma
params = [0.001, 0.01, 0.1, 1, 10, 100]
kernel = ["linear", "rbf"]
best_score = 0
best_parmeter = {}
for k in kernel:
    for gamma in params:
        for C in params:
            svc = SVC(kernel=k, gamma=gamma, C=C)
            model = svc.fit(train[x_cols], train[y_cols])
            score = model.score(test[x_cols], test[y_cols])

            if score >= best_score:
                best_score = score
                best_parameter = {"kernel":k, "gamma":gamma, "C":C}

print(best_score)
print(best_parameter)