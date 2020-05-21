'''
외식업종 관련 data set 분석

문) food_df를 대상으로 다음과 같이 xgboost 모델을 생성하시오.
   <조건1> 6:4 비율 train/test set 생성 
   <조건2> y변수 ; 폐업_2년, x변수 ; 나머지 20개 
   <조건3> 중요변수에 대한  f1 score 출력
   <조건4> 중요변수 시각화  
   <조건5> accuracy와 model report 출력 
'''

import pandas as pd
from sklearn import model_selection, metrics
from sklearn.preprocessing import minmax_scale # 정규화 함수 
from xgboost import XGBClassifier # xgboost 모델 생성 
from xgboost import plot_importance # 중요변수 시각화  

# 중요변수 시각화 
from matplotlib import pyplot
from matplotlib import font_manager, rc # 한글 지원
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 외식업종 관련 data set
food = pd.read_csv("food_dataset.csv",encoding="utf-8",thousands=',')

# 결측치 제거
food=food.dropna()  
print(food.info())

 


