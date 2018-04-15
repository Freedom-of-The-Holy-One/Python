### 机器学习（十三）之K均值算法

##### 一、介绍

模型评价方式：

轮廓系数：凝聚度和分离度

范围：[-1,1] 越大聚类效果越好

##### 二、模型使用

例子：对手写体数字图像分析

```
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

```

缺点：

1. 容易收敛到局部最优解
2. 需要预先设定簇的数量

##### 