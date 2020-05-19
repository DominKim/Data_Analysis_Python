# -*- coding: utf-8 -*-
"""
문) california 주택가격을 대상으로 다음과 같은 단계별로 선형회귀분석을 수행하시오.
"""

# california 주택가격 데이터셋 
'''
캘리포니아 주택 가격 데이터(회귀 분석용 예제 데이터)

•타겟 변수
1990년 캘리포니아의 각 행정 구역 내 주택 가격의 중앙값

•특징 변수(8) 
MedInc : 행정 구역 내 소득의 중앙값
HouseAge : 행정 구역 내 주택 연식의 중앙값
AveRooms : 평균 방 갯수
AveBedrms : 평균 침실 갯수
Population : 행정 구역 내 인구 수
AveOccup : 평균 자가 비율
Latitude : 해당 행정 구역의 위도
Longitude : 해당 행정 구역의 경도
'''

from sklearn.datasets import fetch_california_housing # dataset load
import pandas as pd # DataFrame 생성 
from sklearn.linear_model import LinearRegression  # model
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import mean_squared_error, r2_score # model 평가 
import matplotlib.pyplot as plt 

# 캘리포니아 주택 가격 dataset load 
california = fetch_california_housing()
print(california.DESCR)

# 단계1 : 특징변수와 타켓변수(MEDV)를 이용하여 DataFrame 생성하기   
cal_df = pd.DataFrame(california.data, columns=california.feature_names)
cal_df["MEDV"] = california.target
cal_df.tail()
cal_df.info() 
'''
RangeIndex: 20640 entries, 0 to 20639
Data columns (total 9 columns)
'''


# 단계2 : 타켓변수(y)와 가장 상관관계가 높은 특징변수(x) 확인하기  
cal_df.corr()

# 단계3 : california 데이터셋을 대상으로 1만개 샘플링하여 서브셋 생성하기  


# 단계4 : 75%(train) vs 25(test) 비율 데이터셋 split 


# 단계5 : 선형회귀모델 생성


# 단계6 : 모델 검정(evaluation)  : 예측력 검정, 과적합(overfitting) 확인  
# -------------------------------------------------------------------



# 단계7 : 모델 평가(test) 
# 조건1) 단계3의 서브셋 대상으로 30% 샘플링 자료 이용
# 조건2) 평가방법 : MSE, r2_score


# 단계8 : 예측치 100개 vs 정답 100개 비교 시각화 














