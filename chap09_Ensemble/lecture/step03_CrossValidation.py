"""  
step03_CrossValidation.py

교차검정(CrossValidation)
"""

from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.metrics import accuracy_score, classification_report

# 1. dataset load
digit = load_digits()

X = digit.data
y = digit.target

X.shape
y

# 2. model
rf = RandomForestClassifier()
model = rf. fit(X, y)

pred = model.predict(X)
pred

pred2 = model.predict_proba(X)
pred2

# 확률 -> index(10진수)
pred2_dit = pred2.argmax(axis = 1)
pred2_dit

# 3. CrossValidation
score = cross_validate(model, X, y, scoring = "accuracy", cv = 5)

score
test_score = score["test_score"]

# 산술평균
test_score.mean() # 0.9049405408893294