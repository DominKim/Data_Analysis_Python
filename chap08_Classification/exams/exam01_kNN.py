'''
문) 다음과 같은 3개의 범주를 갖는 6개의 데이터 셋을 대상으로 kNN 알고리즘을 적용하여 
      특정 품목을 분류하시오.
   (단계1 : 함수 구현  -> 단계2 : 클래스 구현)  
      
    <조건1> 데이터 셋  
    -------------------------
          품목     단맛 아삭거림 분류범주
    -------------------------
    grape   8   5     과일
    fish    2   3     단백질 
    carrot  7   10    채소
    orange  7   3     과일 
    celery  3   8     채소
    cheese  1   1     단백질 
    ------------------------
    
   <조건2> 분류 대상과 k값은 키보드 입력  
   
  <<출력 예시 1>> k=3인 경우
  -----------------------------------
    단맛 입력(1~10) : 8
    아삭거림 입력(1~10) : 4
  k값 입력(1 or 3) : 3
  -----------------------------------
  calssCount: {'과일': 2, '단백질': 1}
   분류결과: 과일
  -----------------------------------
  
  <<출력 예시 2>> k=1인 경우
  -----------------------------------
   단맛 입력(1~10) : 2
   아삭거림 입력(1~10) :3
  k값 입력(1 or 3) : 1
  -----------------------------------
  calssCount: {'단백질': 1}
   분류결과 : 단백질
  -----------------------------------
'''

import numpy as np
grape = [8, 5]
fish = [2, 3]
carrot = [7, 10]
orange = [7, 3]
celery = [3, 8]
cheese = [1, 1]
class_category = ['과일', '단백질', '채소', '과일', '채소', '단백질']

# data 생성 함수 정의
def data_set():
    # 선형대수 연산 : numy형 연산
    know_group = np.array([grape, fish, carrot, orange, celery, cheese])
    class_cate = np.array(class_category)
    return know_group, class_category

know, cate = data_set()
know
cate

def classify(know, cate, k):
    sweet = int(input("단맛 입력 :"))
    crispy = int(input("아삭거림 입력 :"))
    not_know = [sweet, crispy]
    
    # 단계1 유클리드 거리
    diff = know - not_know
    diff_square = diff ** 2
    diff_square_sum = diff_square.sum(axis = 1)
    sqrt = np.sqrt(diff_square_sum)
    
    sqrt_agrs = sqrt.argsort()
    
    fruit_dict = {}
    
    # 단계2 빈도수 추출
    for i in range(k):
        key = cate[sqrt_agrs[i]]
        fruit_dict[key] = fruit_dict.get(key, 0) + 1
        
    
    
    return fruit_dict
    
a = classify(know,cate,k=3)    

import pandas as pd

print(max(a))
