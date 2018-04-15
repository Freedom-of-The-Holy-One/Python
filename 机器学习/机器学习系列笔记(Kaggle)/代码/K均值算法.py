# -*- coding:utf-8 -*-
"""
K均值（无监督）实践之对手写体数字图像分析
"""
from sklearn.datasets import load_digits
data=load_digits()

from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(data.data,data.target,test_size=0.25,random_state=33)

from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=10)
kmeans.fit(train_x)

kmeans_predict_data=kmeans.predict(test_x)

from sklearn.metrics import adjusted_rand_score

print("Accuracy:"+str(adjusted_rand_score(test_y,kmeans_predict_data)))

