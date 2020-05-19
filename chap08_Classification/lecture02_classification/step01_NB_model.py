"""  
step01_NB_model

NB 모델
 GaussianNB    : x변수가 실수형이고, 정규분포 형태
 MultinomialNB : 희소행렬과 같은 고차원 데이터를 이용하여 다항분류
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from scipy import stats
import numpy as np

###################
### GaussianNB
###################

# 1. dataset load
iris = pd.read_csv("../../../data/iris.csv")
iris.info()
"""  
Sepal.Length    150 non-null float64
Sepal.Width     150 non-null float64
Petal.Length    150 non-null float64
Petal.Width     150 non-null float64
Species         150 non-null object
"""

# 정규성 검정
stats.shapiro(iris["Sepal.Width"])

# 2 . x,y 변수 선택
cols = list(iris.columns)
cols

x_cols = cols[:4]
y_cols = cols[-1]

# 3. split
train, test = train_test_split(iris, test_size = 0.3, random_state = 123)

# 4. NB model
nb = GaussianNB()
nb.fit(train[x_cols], train[y_cols])
nb

# 5. model 평가
y_pred = nb.predict(test[x_cols])
y_true = test[y_cols]

acc = accuracy_score(y_true, y_pred)
con_mat = confusion_matrix(y_true, y_pred)
f1_score = f1_score(y_true, y_pred, average = "micro") # y의 비율이 불균형인 경우

acc # 0.9555555555555556
con_mat
"""  
array([[18,  0,  0],
       [ 0, 10,  0],
       [ 0,  2, 15]])
"""
f1_score # 0.9555555555555556


###################
### MultinomialNB
###################

# 1. dataset load
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

newsgroups = fetch_20newsgroups(subset="all") # "train", "test"
# Downloading 20 news dataset

print(newsgroups.DESCR)
"""  
x변수 : news 기사 내용(text 자료)
y변수 : 해당 news의 group(20개)
"""
newsgroups.target_names

cats = newsgroups.traget_name[:4]
cats # 

# 2. test -> sparse matrix
news_train = fetch_20newsgroups(subset = "train", categories = cats)
news_train.data   # text(x변수)
news_train.target # 

# sparse matrix
 tfidf = TfidfVectorizer()
 sparse_mat = tfidf.fit_transform(news_train.data)
 sparse_mat.shape # 


#  3. model
nb = MultinomialNB()
model = nb.fit(X = sparse_mat, y = news_train.target)

# 4. model 평가 : fetch_20newsgroups()
news_test = fetch_20newsgroups(subset = "test", categories=cats)

news_test.data
news_test.target

sparse_test = tfidf.transform(news_test.datat)
sparse_test.shaep
"""  
obj.fit_transform(train_data)
obj.transform(test_data)
"""

y_pred = model.predict(sparse_test)
y_true = news_test.target

acc = accuracy_score(y_treu, y_pred)
acc

con_mat = confusion_matrix(y_true, y_pred)
con_mat
"""  

"""

