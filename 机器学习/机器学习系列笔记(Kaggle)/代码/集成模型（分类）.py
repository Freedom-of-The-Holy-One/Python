# -*- coding:utf-8 -*-
"""
集成模型（分类）实践之对泰坦尼克号乘客的生还情况预测
"""
import pandas as pd
data=pd.read_csv('泰坦尼克号乘客数据.txt',sep=',')
X=data[['pclass','age','sex']]
Y=data.survived

X['age'].fillna(X['age'].mean(),inplace=True)

from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.25,random_state=33)

from sklearn.feature_extraction import DictVectorizer
dv=DictVectorizer()
train_x=dv.fit_transform(train_x.to_dict(orient='records'))
test_x=dv.transform(test_x.to_dict(orient='records'))

from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier()
rfc.fit(train_x,train_y)
rfc_predict_data=rfc.predict(test_x)

print("Accuracy of RandomForestClassifier"+str(rfc.score(test_x,test_y)))

from sklearn.ensemble import GradientBoostingClassifier
gbc=GradientBoostingClassifier()
gbc.fit(train_x,train_y)
gbc_predict_data=gbc.predict(test_x)

print("Accuracy of GradientBoostingClassifier"+str(gbc.score(test_x,test_y)))