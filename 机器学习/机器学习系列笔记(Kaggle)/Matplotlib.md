### 机器学习（十）之K近邻（回归）

##### 一、介绍

KNeighborRegressor()

预测方式（weights）:

1. 平均回归：uniform
2. 根据距离加权回归：distance

##### 二、模型介绍及其使用

```
# -*- coding:utf-8 -*-
"""
K近邻（回归）实践之对波士顿房价数据预测
"""
from sklearn.datasets import load_boston
data=load_boston()

from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(data.data,data.target,test_size=0.25,random_state=33)

from sklearn.preprocessing import StandardScaler
ss1=StandardScaler()
ss2=StandardScaler()
train_x=ss1.fit_transform(train_x)
test_x=ss1.transform(test_x)
train_y=ss2.fit_transform(train_y.reshape(-1,1))
test_y=ss2.transform(test_y.reshape(-1,1))

from sklearn.neighbors import KNeighborsRegressor
uniform_knr=KNeighborsRegressor(weights='uniform')
uniform_knr.fit(train_x,train_y)
uniform_knr_predict_data=uniform_knr.predict(test_x)

print("Accuracy(uniform):"+str(uniform_knr.score(test_x,test_y)))

distance_knr=KNeighborsRegressor(weights='distance')
distance_knr.fit(train_x,train_y)
distance_knr_predict_data=distance_knr.predict(test_x)

print("Accuracy(distance):"+str(distance_knr.score(test_x,test_y)))
```

