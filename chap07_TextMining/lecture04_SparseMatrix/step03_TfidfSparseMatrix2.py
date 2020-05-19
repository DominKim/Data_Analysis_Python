"""  
step03_TfidfSparseMatrix2.py

1. csv file read
2. texts, target -> 전처리
3. max features
4. Sparse matrix
5. train / test split
6. binary file save
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# 1. csv file load
sapm_data = pd.read_csv("../data/temp_spam_data2.csv", encoding="utf-8",
header=None)
sapm_data.info()
"""  
RangeIndex: 5574 entries, 0 to 5573
Data columns (total 2 columns):
"""

target = sapm_data[0]
texts = sapm_data[1]

target  # y변수
texts   # sparse matrix -> x변수

# 2. texts, target -> 전처리

# 1) target 전처리 -> dummy(0 ~ 1)
target = [1 if i == "spam" else 0 for i in target]
target # [0, 1, 0, 1, 0]

# 2) texts 전처리
# class 객체에서 불용어 제거 가능

# 3. max features
"""  
사용할 x변수의 개수(열의 차수)
"""
tfidf_fit = TfidfVectorizer().fit(texts) # 문장 -> 단어 생성
vocs = tfidf_fit.vocabulary_
vocs # 
len(vocs) # 8722
max_features = 4000
"""  
전체 단어 8,722 중에서 4,000개 단어 ㅣㅇ용 열의 차수로 사용
만약 max_features = 10 라고 하면 16개 단어 중 10개 단어만 이용
sparse matrix = [574 x 4000]
"""

# 4. sparse matrix
sparse_mat = TfidfVectorizer(stop_words="english",
max_features=4000).fit_transform(texts)
sparse_mat

# scipy -> numpy
sparse_mat_arr = sparse_mat.toarray()
sparse_mat_arr.shape # (5, 16)
sparse_mat_arr

# 5. train / test split
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(sparse_mat_arr, target, test_size = 0.3)

x_train.shape # (3901, 4000)
x_test.shape  # (1673, 4000)

# 6. numpy binary file save
import numpy as np

# file save
spam_data_split = (x_train, x_test, y_train, y_test)
# allow_pickle = True(저장시 생략 가능)
np.save("../data/spam_data", spam_data_split)

# file load allow_pickle = True(load 필수 입력)
x_train, x_test, y_train, y_test = np.load("../data/spam_data.npy", allow_pickle = True)
x_train.shape
x_test.shape

