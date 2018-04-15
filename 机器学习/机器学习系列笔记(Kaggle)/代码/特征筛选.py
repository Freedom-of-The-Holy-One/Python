# -*- coding:utf-8 -*-
"""
特征筛选之对泰坦尼克号数据进行分析
"""
import pandas as pd

data=pd.read_csv('泰坦尼克号乘客数据.txt',sep=',')

# 分离特征与预测目标
y=data.survived
x=data.drop(['row.names','name','survived'],axis=1)
# print(x.info())
x['age'].fillna(x['age'].mean(),inplace=True)
x.fillna('unkonow',inplace=True)

# 数据分割
from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.25,random_state=33)

# 类别型特征向量化
from sklearn.feature_extraction import DictVectorizer
dv=DictVectorizer()
train_x=dv.fit_transform(train_x.to_dict(orient='records'))
test_x=dv.transform(test_x.to_dict(orient='records'))
# print(len(dv.feature_names_))
# print(train_x.head())

# 特征筛选
from sklearn import feature_selection
#筛选前20%的特征
# fs=feature_selection.SelectPercentile(feature_selection.chi2,percentile=3)
# train_x=fs.fit_transform(train_x,train_y)
# test_x=fs.transform(test_x)

# 决策树
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier(criterion='entropy')
dtc.fit(train_x,train_y)

# dtc_predict_data=dtc.predict(test_x)

# 通过交叉验证，按照固定间隔的百分比筛选特征
from sklearn.model_selection import cross_val_score
import numpy as np

percent=range(1,100,2)
results=[]

for i in percent:
    fs=feature_selection.SelectPercentile(feature_selection.chi2,percentile=i)
    train_x_fs=fs.fit_transform(train_x,train_y)
    score=cross_val_score(dtc,train_x_fs,train_y,cv=5)
    results=np.append(results,score.mean())
print(results)
# 找到最佳百分比
opt=np.where(results==results.max())[0]
print(opt)
# 图示
import matplotlib.pyplot as plt
plt.plot(percent,results)
plt.xlabel('percent of features')
plt.ylabel('accuracy')
plt.show()





# 0.8267477203647416
# print("Accuracy of DecisionTreeClassifier(未进行特征筛选):"+str(dtc.score(test_x,test_y)))

#0.817629179331307
# print("Accuracy of DecisionTreeClassifier(进行特征筛选[20%]):"+str(dtc.score(test_x,test_y)))

# 0.8328267477203647
# print("Accuracy of DecisionTreeClassifier(进行特征筛选[3%]):"+str(dtc.score(test_x,test_y)))