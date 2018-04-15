# -*- coding:utf-8 -*-
"""
线性分类器(分类)实践之良/恶性乳腺癌肿瘤预测
"""
import pandas as pd
import numpy as np
#指定数据列名
col_name=['code number','clump thickness','size','shape','adhesion','single size','nuclei','chromatin','nucleoli','mitoses','class']
# 读取数据
data=pd.read_csv('良恶性乳腺癌肿瘤预测.txt',sep=',',header=None,names=col_name)
# 查看数据
# print(data.head())
# 查看数据相关信息
# print(data.describe())
#对数据中缺失值替换为标准缺失值
data=data.replace(to_replace='?',value=np.NaN)
# 删除有缺失值的数据
data=data.dropna(how='any')
# 查看数据维度和数据量
# print(data.shape)

# 将数据划分为训练集与测试集
from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(data[col_name[1:10]],data[col_name[10]],test_size=0.2,random_state=13)

# 数据标准化
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
train_x=ss.fit_transform(train_x)
test_x=ss.transform(test_x)
# 模型建立
# 逻辑斯蒂回归
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(train_x,train_y)
lr_predict_data=lr.predict(test_x)
# 逻辑斯蒂回归精度评价
print("Accuracy of LR Classifier:"+str(lr.score(test_x,test_y)))

# 随机梯度参数估计
from sklearn.linear_model import SGDClassifier
sl=SGDClassifier()
sl.fit(train_x,train_y)
sl_predict_data=sl.predict(test_x)

# 随机梯度参数估计模型精度评价
print("Accuracy of SGD Classifier:"+str(sl.score(test_x,test_y)))