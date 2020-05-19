"""  
step03_KNN_class
"""

from step01_KNN_data import data_set
import numpy as np

know, not_know, cate = data_set()

class KNNClassify:
    # 생성자, 멤버(메서드, 변수)

    def classify(self, know, not_know, cate, k):

        # 단계1 : 거리 계산식
        diff = know - not_know
        square_diff =diff ** 2
        sum_square_diff = square_diff.sum(axis = 1)
        distance = np.sqrt(sum_square_diff)

        # 단계2: 오름차순 정렬 -> index
        sortDist = distance.argsort()

        # 단계3 : 최근접 이웃(k = 3)
        self.class_result = {} # 빈 set

        for i in range(k): # k = 3(0 ~ 2)
            key = cate[sortDist[i]]
            self.class_result[key] = self.class_result.get(key,0) + 1

    def vote(self):
        vote_re = max(self.class_result)
        print("분류결과 :", vote_re)

# 객체 생성 : 생성자 이용
knn = KNNClassify()
knn.classify(know, not_know, cate, 3) # class_result 생성
knn.class_result
knn.vote()
