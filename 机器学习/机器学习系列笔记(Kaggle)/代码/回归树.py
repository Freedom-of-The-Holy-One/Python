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

from sklearn.tree import DecisionTreeRegressor
dtr=DecisionTreeRegressor()
dtr.fit(train_x,train_y)
dtr_predict_data=dtr.predict(test_x)

print("Accuracy:"+str(dtr.score(test_x,test_y)))