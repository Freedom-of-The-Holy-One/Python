# -*- coding:utf-8 -*-
"""
线性模型（回归）实践之对波士顿房价数据预测
"""
from sklearn.datasets import load_boston
import numpy as np
data=load_boston()
# print(data.DESCR)
# print(data)

from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(data.data,data.target,test_size=0.25,random_state=33)

# print(train_y)

from sklearn.preprocessing import StandardScaler
ss1=StandardScaler()
ss2=StandardScaler()
# print(train_x.shape)
# print(test_x.shape)
train_x=ss1.fit_transform(train_x)
test_x=ss1.transform(test_x)
# print(train_y.shape)
# print(test_y.shape)
train_y=ss2.fit_transform(train_y.reshape(-1,1))
test_y=ss2.transform(test_y.reshape(-1,1))

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(train_x,train_y)
lr_predict_data=lr.predict(test_x)

print("Accuracy of LinearRegression:"+str(lr.score(test_x,test_y)))
print("MAE:"+str(mean_absolute_error(test_y,lr_predict_data)))
print("MSE:"+str(mean_squared_error(test_y,lr_predict_data)))
print("----------------------------------------------------------")
from sklearn.linear_model import SGDRegressor
sr=SGDRegressor()
sr.fit(train_x,train_y)
sr_predict_data=sr.predict(test_x)

print("Accuracy of SGDRegressor:"+str(sr.score(test_x,test_y)))
print("MAE"+str(mean_absolute_error(test_y,sr_predict_data)))
print("MSE"+str(mean_squared_error(test_y,sr_predict_data)))



