'''
step04_axis_dot.py

1. 축(aixs) : 행축, 열축
2. 행렬곱 연산 : np.dot()
    - 회귀방정식 행렬곱 예
    X1, X2 -> a1, a2
    model = X1 * a1 + X2 * a2 + b
    model = np.dot(X,a) + b

    - 신경망에서 행렬곱 예
     [X * w] + b
'''

import numpy as np

# 1. 축(axis) : 행축, 열축
'''
행 축 : 동일한 열의 모음(axis = 0) -> 열 단위
열 축 : 동일한 행의 모음(aixs = 1) -> 행 단위
'''

arr2d = np.random.randn(5, 4)
arr2d

print("전체 원소 합계 :", arr2d.sum())
print("행 단위 합계 :", arr2d.sum(axis = 1))
print("열 단위 합계 :", arr2d.sum(axis = 0))


# 2. 행렬곱 연산 : np.dot()
# 입력의 열과 기울기의 행은 수일치가 되어야 한다.
X = np.array([[2, 3], [2.5, 3]])
X # 입력 x
'''
array([[2. , 3. ],
       [2.5, 3. ]])
'''
X.shape # (2, 2)

a = np.array([[0.1], [0.05]]) # (2, 1) 기울기
a.shape
a
'''
array([[0.1 ],
       [0.05]])
'''

# b = 0.1 절편
y_pred = np.dot(X,a)
'''
np.dot(X, a) 전제조건
1. X, a : 행렬 구조
2. 수일치 : X열 차수 = a의 행차수
'''
y_pred
'''
array([[0.35],
       [0.4 ]])
'''