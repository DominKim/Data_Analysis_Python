"""  
step03_SMS_spam_classification.py

NB vs SVM : 희소행렬(고차원)
 - 가중치 적용 : Tfidf
"""

from sklearn.naive_bayes import MultinomialNB # NB model
from sklearn.svm import SVC # SVM model
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np

# 1. dataset load
x_train, x_test, y_train, y_test = np.load("../../../data/spam_data.npy",allow_pickle = True)

x_train.shape # (3901, 4000)

x_test.shape  # (1673, 4000)
# list -> numpy
y_train = np.array(y_train)
y_test = np.array(y_test)

# 2. NB model
nb = MultinomialNB()
model = nb.fit(x_train, y_train)
y_pred = nb.predict(x_test)
y_true = y_test
acc = accuracy_score(y_true, y_pred)
acc # 0.9754931261207412
con_mat = confusion_matrix(y_true, y_pred)
con_mat
"""  
array([[1446,    1],
       [  40,  186]])
"""

# 3. SVM model
svc = SVC()
model_svc = svc.fit(x_train, y_train)

y_pred = model_svc.predict(x_test)

acc2 = accuracy_score(y_true, y_pred)
acc2 # 0.8649133293484758
con_mat2 = confusion_matrix(y_true, y_pred)
con_mat2
"""  
array([[1447,    0],
       [ 226,    0]])
"""
