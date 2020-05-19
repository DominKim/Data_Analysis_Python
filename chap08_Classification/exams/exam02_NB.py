'''
문) weatherAUS.csv 파일을 시용하여 NB 모델을 생성하시오
  조건1> NaN 값을 가진 모든 row 삭제 
  조건2> 1,2,8,10,11,22,23 칼럼 제외 
  조건3> 7:3 비율 train/test 데이터셋 구성 
  조건4> formula 구성  = RainTomorrow ~ 나머지 변수(16개)
  조건5> GaussianNB 모델 생성 
  조건6> model 평가 : accuracy, confusion matrix, f1 score
'''
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score


data = pd.read_csv('C:/ITWILL/4_Python-II/data/weatherAUS.csv')
print(data.head())
print(data.info())

# 조건1> NaN 값을 가진 모든 row 삭제
data=data.dropna()
print(data.head())

# 조건2> 1,2,8,10,11,22,23 칼럼 제외 
col = list(data.columns)
for i in [1,2,8,10,11,22,23] :    
    col.remove(list(data.columns)[i-1])
print(col)


# dataset 생성 
new_data = data[col]
print(new_data.head())

# 조건3> 7:3 비율 train/test 데이터셋 구성
train_set, test_set = train_test_split(
new_data, test_size=0.3, random_state=0) # seed값 

# 조건4> formula 구성  = RainTomorrow ~ 나머지 변수(16개)
y_col = col[-1]
y_col 
x_col = col[:16]
x_col

# 조건5> GaussianNB 모델 생성 
nb = GaussianNB()
nb.fit(train_set[x_col], train_set[y_col])

# 조건6> model 평가 : accuracy, confusion matrix, f1 score
y_pred = nb.predict(test_set[x_col])
y_true = test_set[y_col]

acc = accuracy_score(y_true, y_pred)
acc # 0.8051400076716533
con_mat = confusion_matrix(y_true, y_pred)
con_mat
'''
[[3391,  676],
[ 340,  807]]
'''
f1_score = f1_score(y_true, y_pred, average = "micro")
f1_score # 0.8051400076716534








