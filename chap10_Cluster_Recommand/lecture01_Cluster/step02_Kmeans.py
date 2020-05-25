"""  
step02_Kmeans.py

KMeans 알고리즘
 - 비계층적(확인적) 군집분석
 - 군집수(k) 알고 있는 경우 이용
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# 1. dataset

# text file -> numpy
def dataMat(file):
    dataset = []
    f = open(file, mode = "r")
    for line in f.readlines():
        cols = line.split("\t")

        rows = []
        for col in cols:
            rows.append(float(col))
        dataset.append(rows)
    return np.array(dataset)

dataset = dataMat("../../../data/testSet.txt")

dataset.shape # (80, 2)

dataset[:5]

# numpy -> pandas
dataset_df = pd.DataFrame(dataset, columns = ["x", "y"])
dataset_df.info()

# 2. KMean model : k5
kmeans = KMeans(n_clusters=4, algorithm="auto")

model = kmeans.fit(dataset_df)
pred = model.predict(dataset_df)
pred

# 각 cluster의 center
centers = model.cluster_centers_
centers = pd.DataFrame(centers, columns = ["x", "y"])
# 3.시각화
dataset_df["cluster"] = pred

plt.figure(figsize=(10,5))
sns.pairplot(data = dataset_df, x_vars=["x"], y_vars=["y"], hue="cluster")
sns.pairplot(data = centers, x_vars=["x"], y_vars=["y"])

plt.scatter(dataset_df["x"], dataset_df["y"], c = dataset_df["cluster"], marker="o")
plt.scatter(x= centers[:,0], y = centers[:,1],c = "r", marker="D")