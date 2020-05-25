"""  
step01_hierachy.py

계층적 군집분석
 - 상향식(Bottom-up)으로 계층적 군집형성
 - 유클리드안 거리계산식 이용
 - 숫자형 변수만 사용가능
"""

import pandas as pd
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import seaborn as sns

# 1. dataset load
iris = load_iris()
iris.feature_names

X = iris.data
y = iris.target

iris_df = pd.DataFrame(X, columns= iris.feature_names)
sp = pd.Series(y)

# y 변수 추가
iris_df["species"] = sp
iris_df.info()

# 2. 계층적 군집분석
clusters = linkage(iris_df, method = "complete", metric = "euclidean")
"""  
method = "single"   : 단순연결
method = "complete" : 완전연결
method = "average"  : 평균연결
"""

clusters.shape # (149,4)

# 3. 덴드로그램 시각화
plt.figure(figsize=(20,5))
dendrogram(clusters, leaf_font_size=20, leaf_rotation=90,)

# 4. 클러스터 자르기 / 평가 : 덴드로그램으로 판단
from scipy.cluster.hierarchy import fcluster # cluster 자르기

# 1) 클러스터 자르기
cluster = fcluster(clusters, t = 3, criterion="distance")
cluster # 1 ~ 3

# 2) DF 컬럼추가
iris_df["cluster"] = cluster

# 3) 산점도 시각화
iris_df.info()
cols = iris_df.columns[:3]
sns.pairplot(iris_df, hue = "cluster", markers=["o", "s", "D"], x_vars=cols, y_vars=cols)

# 4) 관측치 vs 예측치
tab = pd.crosstab(index = iris_df["species"], columns = iris_df["cluster"])
tab
"""  
cluster	1	2	3
species			
0	50	0	0
1	0	0	50
2	0	34	16
"""