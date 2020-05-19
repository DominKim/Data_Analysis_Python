'''
step03_reshape.py

1. image shape : 3차원(세로, 가로, 컬러)
2. reshape
'''

import numpy as np
from matplotlib.image import imread # image 읽기
import matplotlib.pyplot as plt
import os

os.getcwd()

# 1. image shape
file_path = "../images/test1.jpg"
image = imread(file_path)
type(image) # numpy.ndarray

image.shape # (360, 540, 3) -> (세로, 가로, 컬러)
print(image)

plt.imshow(image) # 이미지 보기

# RGB 색상 분류
r = image[:,:,0] # R
g = image[:,:,1] # G
b = image[:,:,2] # B
r.shape # (360,540)

# 2. image data reshape
from sklearn.datasets import load_digits # 데이터셋 제공

digit = load_digits() # dataset loading
digit.DESCR # 설명보기

X = digit.data   # x변수(입력변수) : image
y = digit.target # y변수(정답 = 정수)

X.shape # (1797, 64) 64 = 8 * 8
y.shape # (1797,)

img_0 = X[0].reshape(8,8)
img_0
plt.imshow(img_0)
y[0]

X_3d = X.reshape(-1, 8, 8)
X_3d.shape # (1797, 8, 8) -> (전체이미지, 세로, 가로, [컬러])

# (1797, 8, 8, 1)
X_4d = X_3d[:,:,:,np.newaxis] # 4번 축 추가
# np.newaxis : 새로운 축을 추가할때 사용
X_4d.shape # (1797, 8, 8, 1)

# 3. reshape
'''
전치행렬 : T
swapaxis = 전치행렬
transpose() : 3차원 이상 모양 변경
'''

# 1) 전치행렬
data = np.arange(10).reshape(2,5)
data
'''
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
'''

print(data.T)

# 2) transpose()
'''
1차원 : 효과없음
2차원 : 전채행렬 동일함
3차원 : (0, 1, 2) -> (2, 1, 0)
'''
arr3d = np.arange(1,25).reshape(4, 2, 3)
arr3d.shape # (4, 2, 3)
arr3d

# (0, 1, 2) -> (2, 1, 0)
arr3d_tran = arr3d.transpose() # (2, 1, 0) : default
arr3d_tran.shape

