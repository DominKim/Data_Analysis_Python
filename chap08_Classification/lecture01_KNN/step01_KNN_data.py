"""  
step01_KNN_data
"""
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt

# 1. 알려진 두 집단 x,y 산점도 시각화 
plt.scatter(1.2, 1.1) # A 집단
plt.scatter(1.0, 1.0)
plt.scatter(1.8, 0.8) # B 집단 
plt.scatter(2, 0.9)

plt.scatter(1.6, 0.85, color='r') # 분류대상 
plt.show()

# 2. DATA 생성과 함수 정의 
p1 = [1.2, 1.1] # A 집단 
p2 = [1.0, 1.0]
p3 = [1.8, 0.8] # B 집단
p4 = [2, 0.9]
category = ['A','A','B','B'] # 알려진 집단 분류범주(Y변수)
p5 = [1.6, 0.85] # 분류대상 

# data 생성 함수 정의
def data_set():
    # 선형대수 연산 : numpy형 변환 
    know_group = np.array([p1, p2, p3, p4]) # 알려진 집단 
    not_know_group = np.array(p5) # 알려지지 않은 집단
    class_category = np.array(category) # 정답(분류범주)
    return know_group,not_know_group,class_category 


