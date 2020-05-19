"""  
step02_KNN_func
"""

# from modul import function
from step01_KNN_data import data_set
import numpy as np

# data_set
know, not_know, cate = data_set()
know.shape # (4,2)
not_know
cate

# 거리계산식 : 차 > 제곱 > 합 > 제곱근
diff = know - not_know
diff
square_diff = diff ** 2
square_diff

sum_square_diff =square_diff.sum(axis = 1) # 행 단위 합계
sum_square_diff # array([0.2225, 0.3825, 0.0425, 0.1625])

distance = np.sqrt(sum_square_diff)
cate # ['A', 'A', 'B', 'B']

sortDist = distance.argsort()
sortDist # [2, 3, 0, 1]

result = cate[sortDist]
result # ['B', 'B', 'A', 'A']

k = 3 # 최근접 이웃 3개
k3 = result[:k]

# dict
classify_re = {}

for key in k3:
    classify_re[key] = classify_re.get(key, 0) + 1

classify_re # {'B': 2, 'A': 1}

vote_re = max(classify_re)
vote_re

def knn_classify(know, not_know, cate, k):

    # 단계1 : 거리 계산식
    diff = know - not_know
    square_diff =diff ** 2
    sum_square_diff = square_diff.sum(axis = 1)
    distance = np.sqrt(sum_square_diff)

    # 단계2: 오름차순 정렬 -> index
    sortDist = distance.agresort()

    # 단계3 : 최근접 이웃(k = 3)
    class_result = {} # 빈 set

    for i in range(k): # k = 3(0 ~ 2)
        key = cate[sortDist[i]]
        class_result[key] = class_result.get(key,0) + 1

    return class_result