'''
step02_indexing.py

indexing / slicing
 - 1차원 indexing : list 동일함
 - 2,3차 indexing
 - boolean indexing
'''

import numpy as np

# 1. indexing
# list <-> numpy : 블럭수정, 원본 수정
'''
1차원 : obj[index]
2차원 : obj[행index, 열index]
3차원 : obj[면index, 행index, 열index]
'''

# 1) list 객체
ldata = [0, 1, 2, 3, 4, 5]
ldata
ldata[:] # 전체 원소
# ldata[:] = 10 TypeError
ldata[2:] # [n:~]
ldata[:3] # [~:n]
ldata[-1]

# 2) numpy 객체
arr1d = np.array(ldata)
arr1d.shape # (6,)
arr1d[2:]
arr1d[:3]
arr1d[-1]

# 2. slicing
arr = np.array(range(1,11))
arr # 원본

arr_sl = arr[4:8]
arr_sl # 사본
# 불럭 수정
arr_sl[:] = 50
arr_sl

arr # 원본 수정

# 2,3차 indexing
arr2d = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
arr2d.shape # (3,3)
arr2d
'''
array([[1, 2, 3],
       [2, 3, 4],
       [3, 4, 5]])
'''
# 행 index : default
arr2d[1]
arr2d[1:]
arr2d[:,1:]
arr2d[2,1]
arr2d[:2,1:]

# [면, 행, 열] : 면index: default
arr3d = np.array([[[1, 2, 3], [2, 3, 4], [3, 4, 5]],
 [[2, 3, 4], [3, 4, 5], [4, 5, 6]]])

arr3d
'''
array([[[1, 2, 3],
        [2, 3, 4],
        [3, 4, 5]],

       [[2, 3, 4],
        [3, 4, 5],
        [4, 5, 6]]])
'''
arr3d.shape # (2, 3, 3)

arr3d[0] # 면 index = 1면
arr3d[1] # 면 index = 2면

# 면 -> 행 index
arr3d[0,2] # [3, 4, 5]

# 면 -> 행 -> 열 index
arr3d[1, 2, 2] # 8
arr3d[1, 1: , 1:]

# 4. boolean indexing
dataset = np.random.randint(1, 10, size = 100) # 1 ~ 10
len(dataset) # 100

dataset

# 5 이상
dataset2 = dataset[dataset >= 5]
len(dataset2) # 48

# 5 ~ 8 자료선택
# dataset[(dataset >= 5) & (dataset <= 8)]
np.logical_and
np.logical_or
np.logical_not

dataset2 = dataset[np.logical_and(dataset >= 5, dataset <= 8)]
dataset2 # 5 ~ 8