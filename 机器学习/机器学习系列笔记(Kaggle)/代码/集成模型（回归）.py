# -*- coding:utf-8 -*-
"""
集成模型（回归）实践之对波士顿房价数据预测
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

from sklearn.ensemble import RandomForestRegressor
rfr=RandomForestRegressor()
rfr.fit(train_x,train_y)
rfr_predict_data=rfr.predict(test_x)

print("Accuracy of RandomForestRegressor："+str(rfr.score(test_x,test_y)))

from sklearn.ensemble import ExtraTreesRegressor
etr=ExtraTreesRegressor()
etr.fit(train_x,train_y)
etr_predict_data=etr.predict(test_x)

print("Accuracy of ExtraTreesRegressor："+str(etr.score(test_x,test_y)))

from sklearn.ensemble import GradientBoostingRegressor
gbr=GradientBoostingRegressor()
gbr.fit(train_x,train_y)
gbr_predict_data=gbr.predict(test_x)

print("Accuracy of GradientBoostingRegressor："+str(gbr.score(test_x,test_y)))
