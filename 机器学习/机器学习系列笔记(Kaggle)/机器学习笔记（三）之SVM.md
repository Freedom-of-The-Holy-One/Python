### 机器学习笔记（三）之SVM

##### 一、介绍

支持向量机（support vector machine，简称：SVM），监督式学习模型。通过选择核函数确定是线性分类还是非线性分类。

SVM还可以用来对数据进行聚类（非监督学习）。

##### 二、模型及其使用

例子：对手写体数据图片进行分类

```
# -*- coding:utf-8 -*-
"""
SVC实践之对手写体数据图片进行分类
"""

import pandas as pd

from sklearn.datasets import load_digits

data=load_digits()

# print(data.shape)

from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(data.data,data.target,train_size=0.75,random_state=33)

from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
train_x=ss.fit_transform(train_x)
test_x=ss.transform(test_x)

from  sklearn.svm import LinearSVC

ls=LinearSVC()
ls.fit(train_x,train_y)
ls_predict_data=ls.predict(test_x)

print('Accuracy:'+str(ls.score(test_x,test_y)))

```

