"""  
step04_DT_model.py

Decision Tree 모델
 - 중요변수 선정 기준 : GINI, Entropy
 - GINI : 불확실성을 개선하는데 기여하는 척도
 - Entropy : 불확실성을 나타내는 척도
"""

from sklearn.model_selection import train_test_split # split
from sklearn.datasets import load_iris, load_wine
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score, confusion_matrix

# tree 시각화 관련
from sklearn.tree.export import export_text # tree 구조 텍스트
from sklearn import tree

iris = load_iris()
iris.target_names # ['setosa', 'versicolor', 'virginica']

X = iris.data
y = iris.target

names = iris.feature_names

X.shape # (150, 4)

x_train, x_test, y_train, y_test = train_test_split(X,y, test_size = 0.3)

dtc = DecisionTreeClassifier(criterion="gini",random_state=123, max_depth=3)

dtc2 = DecisionTreeClassifier(criterion="entropy")

model = dtc.fit(x_train, y_train)
model2 = dtc2.fit(x_train, y_train)

# tree 시각화
tree.plot_tree(model)
tree.plot_tree(model2)

print(export_text(model, feature_names=names))
"""  
|--- petal length (cm) <= 2.60
|   |--- class: 0
|--- petal length (cm) >  2.60
|   |--- petal width (cm) <= 1.75
|   |   |--- petal length (cm) <= 4.90
|   |   |   |--- class: 1
|   |   |--- petal length (cm) >  4.90
|   |   |   |--- class: 1
|   |--- petal width (cm) >  1.75
|   |   |--- petal length (cm) <= 4.85
|   |   |   |--- class: 2
|   |   |--- petal length (cm) >  4.85
|   |   |   |--- class: 2
"""

y_pred = model.predict(x_test)
y_true = y_test

acc = accuracy_score(y_true, y_pred)
acc # 0.9333333333333333

confusion_matrix(y_true, y_pred)
"""  
confusion_matrix(y_true, y_pred)
array([[13,  0,  0],
       [ 0, 16,  0],
       [ 0,  3, 13]])
"""


#################
## over fitting
#################

wine = load_wine()
x_name = wine.feature_names # x변수명
X = wine.data
y = wine.target

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.3, random_state = 123
)

dt = DecisionTreeClassifier() # default
model = dt.fit(x_train, y_train)

train_score = model.score(x_train, y_train)
train_score # 1.o
test_score = model.score(x_test, y_test)
test_score  # 0.9629629629629629

tree.plot_tree(model) # max_dept = 5

# max_depth = 3
dt = DecisionTreeClassifier(max_depth=3) # default
model = dt.fit(x_train, y_train)

train_score = model.score(x_train, y_train)
train_score # 0.9838709677419355
test_score = model.score(x_test, y_test)
test_score  # 0.9629629629629629

tree.plot_tree(model)

export_graphviz(model, out_file = "DT_tree_graph.dot",
feature_names=x_name, max_depth=3, class_names=True)