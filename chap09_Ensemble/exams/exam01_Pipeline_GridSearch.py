'''
 문) digits 데이터 셋을 이용하여 다음과 단계로 Pipeline 모델을 생성하시오.
  <단계1> dataset load
  <단계2> Pipeline model 생성
          - scaling : StndardScaler 클래스, modeing : SVC 클래스    
  <단계3> GridSearch model 생성
          - params : 10e-2 ~ 10e+2, 평가방법 : accuracy, 교차검정 : 5겹
          - CPU 코어 수 : 2개 
  <단계4> best score, best params 출력 
'''

from sklearn.datasets import load_digits # dataset 
from sklearn.svm import SVC # model
from sklearn.model_selection import GridSearchCV # gride search model
from sklearn.pipeline import Pipeline # pipeline
from sklearn.preprocessing import StandardScaler # dataset scaling


# 1. dataset load
digits = load_digits()


# 2. pipeline model : data 표준화 -> model 


# 3. gride search model 


# 4. best score, best params



