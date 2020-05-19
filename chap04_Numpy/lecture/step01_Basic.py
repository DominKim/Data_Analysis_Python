#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
step01_Basic.py

Numpy 패키지 특징
 - 선형대수(벡터, 행렬) 연산 관련 함수 제공
 - list 보다 이점 : N차원 배열 생성, 선형대수 연산, 고속 처리
 - Series 공통정
     -> 수학 / 통계 함수 지원
      ex) obj.수학 / 통계()
     -> 범위수정, 블럭연산
     -> indexing / slicing
 - 주요모듈과 함수
  1. random : 난수 생성 함수
  2. array 함수 : N차원 배열 생성(array[[[list]]]) * 중첩의 수만큼 n차원
  3. sampling 함수
  4. arange : range() 유사함
  https://www.scipy.org
"""

import numpy as np

# list 자료구조
lst = [1, 2, 3]
lst ** 2 # TypeError

for i in lst:
    print(i ** 2)
    
# list -> numpy
arr = np.array(lst)
arr # array([1, 2, 3])
arr ** 2 # array([1, 4, 9])

# 동일 type
arr = np.array([[1, "two", 3]])
arr # array([['1', 'two', '3']], dtype='<U21')
arr.shape # (1, 3)

# 1. random : 난수 생성 함수
data = np.random.randn(3, 4) # 모듈.모듈.함수()
data
'''
array([[ 0.72125475,  0.57985938,  0.68084901,  1.47461831],
       [ 0.27564635,  1.63000333, -0.79223113, -1.48794495],
       [ 1.53238326,  1.30883657, -0.00871649,  0.69374293]])
'''

for row in data:
    print("행 단위 합계 :", row.sum())
    print("행 단위 평균 :", row.mean())

# 1) 수학 / 통계 함수 지원
type(data) # numpy.ndarray
print("전체 합계 :", data.sum())
print("전체 평균 :", data.mean())
print("전체 분산 :", data.var())
print("전체 표준편차 :", data.std())

dir(data)
data.shape
data.size

# 2) 범위수정, 블럭연산
data + data
data - data

# 3) indexing : R 유사함
data[0, 0] # 1행 1열
data[0, :] # 1행 전체
data[:, 1] # 2열 전체

# 2. array 함수 : N차원 배열 생성

# 1) 단일 list
lst1 = [3, 5.6, 5, 7, 8]
lst1 # [3, 5.6, 5, 7, 8] : 형식 유지
# lst1.var()

# list -> numpy
arr1 = np.array(lst1)
arr1 # array([3. , 5.6, 5. , 7. , 8. ]) : 동일한 형식으로 변경

arr1.var()
arr1.std()

# 2) 중첩 list
lst2 = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
lst2 # [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
lst2[0][2] # 3

arr2 = np.array(lst2)
arr2
'''
array([[1, 2, 3, 4, 5],
       [2, 3, 4, 5, 6]])
'''
arr2.shape # (2, 5)
arr2[0,2] # 3

# index : obj[행index, 열index]
arr2[1,:] # 2행 전체
arr2[:,1] # 2열 전체
arr2[:, 2:4] # box 선택

# broadcast 연산
# - 작은 차원이 큰 차원으로 늘어난 후 연산

# 1) scala(0) vs vector(1)
0.5 * arr1 # [1.5, 2.8, 2.5, 3.5, 4. ]

# 2) scala(0) vs matrix(2)
0.5 * arr2
'''
array([[0.5, 1. , 1.5, 2. , 2.5],
       [1. , 1.5, 2. , 2.5, 3. ]])
'''

# 3) vector(1) vs matrix(2)
print(arr1.shape, arr2.shape)
# (5,) (2, 5)

arr3 = arr1 + arr2
print(arr3)


# 3. sampling 함수
num = list(range(1, 11))
num
help(np.random.choice) # 모듈.모듈.함수()
'''
a : 관측치 길이
size : 임의의 추출 크기
replace : 복원(True) or 비복원(False)
p : 확률
'''
idx = np.random.choice(a = len(num),
size=5, replace=False)
idx

import pandas as pd
import os
os.getcwd()
score = pd.read_csv("../../../data/score_iq.csv")

score.info()
len(score)

idx = np.random.choice(a = len(score), 
size = int(len(score) * 0.3), replace=False)
# 비복원 추출, size는 정숳여만 가능!!
idx
len(idx) # 45

# DataFrame index
score_train = score.iloc[idx, :]
score_train.shape # (45, 6)

score_test = score.drop(idx)
score_test.shape # (105, 6)

# pandas(DF) -> numpy(array)
score_arr = np.array(score)
score_arr.shape # (150, 6)
score_train2 = score_arr[idx, :]
score_train2.shape # (45,6)

# test set 선택
test_idx = [i for i in range(len(score)) if i not in idx]
len(test_idx)
score_test = score_arr[test_idx, :]
score_test.shape # (105, 6)

# 4. arrange : range() 유사함

zero_arr = np.zeros((3,5)) # 영 행렬
zero_arr

cnt = 1
for i in np.arange(3):
    for j in np.arange(5):
        zero_arr[i, j] = cnt
        cnt += 1

zero_arr
'''
array([[ 1.,  2.,  3.,  4.,  5.],
       [ 6.,  7.,  8.,  9., 10.],
       [11., 12., 13., 14., 15.]])
'''

# range(-1.0, 2, 0.1) (start, stop, stpe) : 정수형만 생성가능
np.arange(-1.0, 2, 0.1) # 실수혀으 음수도 생성가능