# Data_Analysis_Python
~~~python3
"Data Analysis for Python"
~~~
1. Pandas
> **lecture01_ds(데이터 구조)**
>> [step01_Series](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap01_Pandas/lecture01_ds/step01_Series.py)
>
~~~python3
# 4. 결측치 처리 방법(평균, 0, 제거)
print(type(p3))
# <class 'pandas.core.series.Series'>

# 1) 평균 대체
p4 = p3.fillna(p3.mean())
print(p4)

# 2) 0 대체
p5 = p3.fillna(0)
print(p5)

# 3) 결측치 제거
p6 = p3[pd.notnull(p3)] # subset
print(p6)
~~~
>> [step02_DataFrame](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap01_Pandas/lecture01_ds/step02_DataFrame.py)
>
~~~python3
# 3) 조건식으로 행 선택, 여러 조건 각 조건 맏 ()부여 후 &, |, ==, !=
subset3 = emp[emp["Pay"] >= 350] # or emp[emp.Pay >= 350]
subset3 = emp[(emp["Pay"] > = 350) & (emp["Name"] == "Hong")]

df[slicing], df[boolena] : raw 선택
df[column] : 컬럼 선택

# 조건식으로 제거
df = df.drop(df[<some boolean condition>].index)
~~~
>> [step03_Descriptive](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap01_Pandas/lecture01_ds/step03_Descriptive.py)
>
> **lecture02_handling**
>> [step01_DF_merge](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap01_Pandas/lecture02_handling/step01_DF_merge.py)
~~~python3
병합, 결합의 차이숙지 필요!!
병합은 공통된 컬럼(열)이 필요하다.
~~~
>> [step02_reshape](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap01_Pandas/lecture02_handling/step02_reshape.py)
2. Matplot
>> [step01_Matplot](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap02_Matplot/lecture/step01_Matplot.py)
>
>> [step02_Pandasplot](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap02_Matplot/lecture/step02_PandasPlot.py)
>
>> [step03_Multi_line](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap02_Matplot/lecture/step03_multi_line.py)
>
3. GroupbyApply
>> [step01_groupby](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap03_GroupbyApply/lecture/step01_groupby.py)
>
>> [step02_groupby_plot](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap03_GroupbyApply/lecture/step02_groupby_plot.py)
>
>> [step03_apply](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap03_GroupbyApply/lecture/step03_apply.py)
>
~~~python3
# apply() : 판다스의 객체에 외부함수를 적용할때 사용
~~~
>> [step04_pivot_table](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap03_GroupbyApply/lecture/step04_pivot_table.py)
>
~~~python3
피벗테이블(pivot table)
 - 사용자가 행, 열 그리고 교차셀에 변수를 지정하여 사용자 정의 테이블 생성
~~~
4. Numpy
>> [step01_Basic](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap04_Numpy/lecture/step01_Basic.py)
>
>> [step02_indexing](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap04_Numpy/lecture/step02_indexing.py)
>
>> [step03_reshape](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap04_Numpy/lecture/step03_reshape.py)
>
>> [step04_axis_dot](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap04_Numpy/lecture/step04_axis_dot.py)
>
>> [step05_dot_example](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap04_Numpy/lecture/step05_dot_example.py)
>
>> [step06_image_resize](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap04_Numpy/lecture/step06_image_resize.py)
>
5. Stats_Scipy
>> [step01_stats_test](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap05_Stats_Scipy/lecture/step01_stats_test.py)
>
>> [step02_chisquare_test](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap05_Stats_Scipy/lecture/step02_chisquare_test.py)
>
>> [step03_t_test](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap05_Stats_Scipy/lecture/step03_t_test.py)
>
>> [step04_correlation](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap05_Stats_Scipy/lecture/step04_correlation.py)
>
>> [step05_regression](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap05_Stats_Scipy/lecture/step05_regression.py)
>
>> [step06_timeSeries](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap05_Stats_Scipy/lecture/step06_timeSeries.py)
>
6. Regression
~~~python3
# 선형모델은 샘플에 비해 특성이 많을때 잘 작동한다.(고차원)
# 특성이 적을때는 다른 모델들의 일반화 성능이 더 좋다.
# 리지회귀 : 선형회귀가 과적합일때 대신 사용
# alpha : 과적합이 되지 않게 모델을 제한 값이 클수록 규제가 강해지고 회귀계수는 0에 가까워짐
from sklearn.linear_model import Ridge
model = Ridge(alpha).fit(x,y)

# 라쏘회귀 : 리지와 비슷 차이점 : 특성이 많고 그 중 일부만 중요할때

# 선형서포트 벡터머신(다중 분류모델)
from sklearn.svm import LinearSVC

# alpha, c 는 로그 스케일로 최적치 선성
# penalty = "l1" 중요 특성변수가 적다고 생각할떄, 모델의 해석이 중요할때
# penalty = "l2" 중요 특성변수가 많을때
~~~
>> [step01_regression](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap06_Regression/lecture/step01_regression.py)
>
>> [step02_dot_regression](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap06_Regression/lecture/step02_dot_regression.py)
>
>> [step03_sklearn_Regression](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap06_Regression/lecture/step03_sklearn_Regression.py)
>
>> [step04_normal_Regression](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap06_Regression/lecture/step04_normal_Regression.py)
>
>> [step05_sklearn_LogisticRegression](https://github.com/DominKim/Data_Analysis_Python/blob/master/chap06_Regression/lecture/step05_sklearn_LogisticRegression.py)
>



semi_project
>> [semi_filio](https://github.com/DominKim/Data_Analysis_Python/blob/master/semi_project/semi_fileio.py)
>
>> [pre_processing](https://github.com/DominKim/Data_Analysis_Python/blob/master/semi_project/pre_processing.py)
>
