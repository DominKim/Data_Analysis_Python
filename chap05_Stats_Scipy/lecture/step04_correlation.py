'''
step04_correlation.py

공분산 vs 상관계수(correlation)
 - 공통점 : 변수간의 상관성 분석

1. 공분산 : 두 확률변수 간의 분산(평균에서 퍼짐 정도)을 나타내는 통계
 - 두 확률변수 : X, Y -> X 표본평균(ux), Y 표본평균(uy)
 Cov(X, Y) = sum((X-ux) *(Y - uy)) / n
 Cov(X, Y) > 0 : X증가 -> Y증가
 Cov(X, Y) < 0 : X증가 -> Y감소
 Cov(X, y) = 0 : 두 변수는 선형관계가 아님
 문제점 : 값이 큰 변수에 영햐을 받는다.

2. 상관계수 : 공분산을 각각의 표준편차로 나누어서 정규화한 통계
 - 부호는 공분산과 동일하고, -1 ~ +1(절대값 1을 넘지 않음)
 - Cor(x, y) = Cov(X, Y) / std(X) * std(Y)
'''

import numpy as np
import pandas as pd

score_iq = pd.read_csv("/Users/mac/Desktop/bigdata/Python/4_Python-II/data/score_iq.csv")
score_iq.info()
score_iq.head()

cor = score_iq.corr()
cor
'''
	sid	score	iq	academy	game	tv
sid	1.000000	-0.014399	-0.007048	-0.004398	0.018806	0.024565
score	-0.014399	1.000000	0.882220	0.896265	-0.298193	-0.819752
iq	-0.007048	0.882220	1.000000	0.671783	-0.031516	-0.585033
academy	-0.004398	0.896265	0.671783	1.000000	-0.351315	-0.948551
game	0.018806	-0.298193	-0.031516	-0.351315	1.000000	0.239217
tv	0.024565	-0.819752	-0.585033	-0.948551	0.239217	1.000000
'''
score_iq["score"].corr(score_iq["iq"]) # 0.88222034461347


'''
1. 공분산
 - score vs iq
 - score vs academy
'''
X = score_iq["score"]
Y1 = score_iq["iq"]
Y2 = score_iq["academy"]

# 공분산 함수 정의
def Cov(X, Y):
    ux = X.mean(); uy = Y.mean()
    cov_re = sum((X-ux)*(Y-uy)) /len(X)
    return cov_re

cov1 = Cov(X, Y1) # score vs iq
cov2 = Cov(X, Y2) # score vs academy
print(cov1, cov2)
# 50.99528888888886 7.072444444444438

score_iq.cov()
score_iq["score"].cov(score_iq["iq"]) # 51.33753914988811
score_iq[["score", "iq"]].cov()

'''
2. 상관계수
 Cor(x, y) = Cov(X, Y) / std(X) * std(Y)
'''

def Cor(X,Y):
    cov = Cov(X,Y)
    std_x = X.std()
    std_y = Y.std()
    cor_re = cov / (std_x * std_y)
    return cor_re

cor1 = Cor(X, Y1) # score vs iq
cor2 = Cor(X, Y2) # score vs academy
print(cor1, cor2)
# 0.8763388756493802 0.8902895813918037
