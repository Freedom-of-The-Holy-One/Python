# -*- coding:utf-8 -*-
"""
决策树实践之对泰坦尼克号乘客的生还情况预测
"""
import pandas as pd
data=pd.read_csv('泰坦尼克号乘客数据.txt',sep=',')
# print(data.head())
# print(data.info())

X=data[['pclass','age','sex']]
Y=data.survived
# print(X.info())

# 缺失值处理：均值 中位数等
X['age'].fillna(X['age'].mean(),inplace=True)

from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(X,Y,train_size=0.75,random_state=33)

from sklearn.feature_extraction import DictVectorizer
dv=DictVectorizer(sparse=False)

train_x=dv.fit_transform(train_x.to_dict(orient='records'))
# print(dv.feature_names_)
test_x=dv.transform(test_x.to_dict(orient='records'))

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(train_x,train_y)
dt_predict_data=dt.predict(test_x)

print("Accuary:"+str(dt.score(test_x,test_y)))
