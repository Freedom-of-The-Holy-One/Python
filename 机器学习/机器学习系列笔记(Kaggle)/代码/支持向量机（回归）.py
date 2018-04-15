# -*- coding:utf-8 -*-
"""
支持向量机（回归）实践之对波士顿房价数据预测
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

from sklearn.svm import SVR

# 线性核函数
linear_svr=SVR(kernel='linear')
linear_svr.fit(train_x,train_y)
linear_svr_predict_data=linear_svr.predict(test_x)
print("Accuracy of SVR(linear):"+str(linear_svr.score(test_x,test_y)))

# 多项式核函数
poly_svr=SVR(kernel='poly')
poly_svr.fit(train_x,train_y)
poly_svr_predict_data=poly_svr.predict(test_x)
print("Accuracy of SVR(poly):"+str(poly_svr.score(test_x,test_y)))

# 径向基核函数
rbf_svr=SVR(kernel='rbf')
rbf_svr.fit(train_x,train_y)
rbf_svr_predict_data=rbf_svr.predict(test_x)
print("Accuracy of SVR(rbf):"+str(rbf_svr.score(test_x,test_y)))
