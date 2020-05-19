"""  
step05_sklearn_LogisticRegression.py

sklearn 로지스틱 회귀모델
 - y변수가 범주형인 경우
"""

from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt

##################
### 1. 이항분류 모델
##################

# 1. dataset load
breast = load_breast_cancer()

x = breast.data
y = breast.target
x.shape # (569, 30)
y.shape # (569,)

# 2. model 생성
help(LogisticRegression)
"""  
random_state=None, solver='lbfgs', max_iter=100, multi_class='warn'

random_state       : 난수 seed값 지정
solver='lbfgs'     : 알고리즘
 - solver : {'newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'}
max_iter=100       : 반복학습 횟수
multi_class='auto' : 다항분류
 - multi_class : {'ovr', 'multinomial', 'auto'}

적용 예)
일반 데이터, 이항분류 : default
일반 데이터, 다항분류 : solver = 'lbfgs', multi_class = 'multinomial'
빅 데이터, 이항분류  : solver = 'saga' or 'sag'
빅 데이터, 다항분류  : solver = 'saga' or 'sag', multi_class = 'multinomial'
"""
lr = LogisticRegression(random_state=123)
model = lr.fit(X=x, y=y)
model # multi_class = 'auto' -> sigimoid 활용함수 -> 이항분류

# 3. model 평가
acc = model.score(X = x, y = y)
print("accuracy =", acc) # accuracy = 0.9595782073813708

y_pred = model.predict(x)

acc = accuracy_score(y,y_pred)
print("accuracy =", acc) # accuracy = 0.9595782073813708

con_mat = confusion_matrix(y, y_pred)
print(con_mat)
"""  
[[198  14]
 [  9 348]]
"""
acc = (con_mat[0,0] + con_mat[1,1]) / con_mat.sum()
print("accuracy =", acc) # accuracy = 0.9595782073813708

##################
### 2. 다항분류 모델
##################

# 1. dataset load
iris = load_iris()
iris.target_names # ['setosa', 'versicolor', 'virginica']

X, y = load_iris(return_X_y=True)

X.shape
y.shape
y # 0 ~ 2

# 2. model
# 일반 데이터, 다항분류 : solver="lbfgs", multi_class = "multinomial"

lr = LogisticRegression(solver="lbfgs", multi_class = "multinomial", random_state=123)

# multi_class = 'multinomial' : softmax 활용함수 이용 -> 다항분류
"""  
활성함수
sigmoid function : 0 ~ 1 확률값 -> cutoff = 0.5 -> 이항분류
softmax function : 0 ~ 1 확률값 -> 전체합 = 1(c:0.1, c1:0.1, c2:0.8) -> 다항분류
"""

model = lr.fit(X,y)

acc =model.score(X,y)
acc

y_pred = model.predict(X)        # class
y_pred2 = model.predict_proba(X) # 확률값

y_pred  # 0 ~ 2
y_pred2.shape # (150, 3)

# 3. 모델평가
acc = accuracy_score(y, y_pred) # 0.9733333333333334

con_mat = confusion_matrix(y, y_pred)
con_mat
"""  
array([[50,  0,  0],
       [ 0, 47,  3],
       [ 0,  1, 49]])
"""

# 히트맵 : 시각화
import seaborn as sn # heatmap - Accuracy Score

# confusion matrix heatmap 
plt.figure(figsize=(6,6)) # chart size
sn.heatmap(con_mat, annot=True, fmt=".3f", linewidths=.5, square = True);# , cmap = 'Blues_r' : map 색상 
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Accuracy Score: {0}'.format(acc)
plt.title(all_sample_title, size = 18)
plt.show()

#########################
### digits : multi class
#########################

from sklearn.datasets import load_digits

# 1. dataset load
digits = load_digits()
a = digits.target_names # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

X = digits.data
y = digits.target
X.shape # (1797, 64) -> 1797장 images
y.shape # 1797장 images 10진수 정답

# 2. split
img_train, img_test, label_train, label_test = train_test_split(X,y, test_size = 0.25)
img2d = img_train.reshape(-1,8,8) # (전체 image(-1), 세로, 가로)
img2d.shape # (1347, 8, 8)
plt.imshow(img2d[0])

# 3. model 생성
lr = LogisticRegression(solver="lbfgs", multi_class="multinomial")
model = lr.fit(img_train, label_train)

y_pred = model.predict(img_test)

# 4. model 평가
acc = accuracy_score(label_test, y_pred)

result = label_test == y_pred
result
result.mean()

len(result) # 450

# 틀린 image
false_img = img_test[result == False]
false_img.shape # (15,64)