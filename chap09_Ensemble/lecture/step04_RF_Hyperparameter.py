"""  
step04_RF_Hyperparameter.py

Random Forest Hyper parameter
 step02_RandomForest 참고
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, GridSearchCV

# 1. dataset load
wine = load_wine()
names = wine.feature_names # x변수명
wine.target_names

X = wine.data
y = wine.target

X.shape # (178, 13)

# 2. RF model
rf = RandomForestClassifier()
"""  
n_estimators : integer, optional(default = 100) : tree 갯수
criterion : string, optional (default="gini") or "entropy" : 중요변수 선정 기준
max_depth : integer or None, optional (default=None) tree 깊이 ! 모델생성에서 자동 설정
min_samples_split : int, float, optional (default=2) 노드 분할 최소 샘플수
min_samples_leaf : int, float, optional (default=1)  단노드 분할 최소 샘플수
max_features : int, float, string or None, optional (default="auto") 최대 x 변수 사용수
n_jobs : int or None, optional (default=None) cpu 수
random_state : int, RandomState instance or None, optional (default=None)
"""

# 3. GridSearch

# 1) params 설정 : dict
params = {"n_estimators":[100,200,300,400],
"max_depth":[3,6,8,10],
"min_samples_split":[2,3,4,5],
"min_samples_leaf":[1,3,5,7]}

# 2) GridSearchCV
gs =GridSearchCV(rf, param_grid=params, scoring="accuracy", cv=5,n_jobs=-1)

model = gs.fit(X,y)

model.score(X,y)
model.best_params_
model.best_score_