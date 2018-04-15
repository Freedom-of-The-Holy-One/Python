### 机器学习（五）之K近邻（分类）

##### 一、介绍

##### 二、模型及其使用

例子：生物物种分类

```
# -*- coding:utf-8 -*-
"""
K近邻实践之对生物物种分类
"""
from sklearn.datasets import load_iris
data=load_iris()
# print(data.DESCR)

from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(data.data,data.target,train_size=0.75,random_state=33)

from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
train_x=ss.fit_transform(train_x)
test_x=ss.transform(test_x)

from sklearn.neighbors import KNeighborsClassifier
kc=KNeighborsClassifier()
kc.fit(train_x,train_y)
kc_predict_data=kc.predict(test_x)

print("Accuracy:"+str(kc.score(test_x,test_y)))
```

备注：

计算量与内存消耗巨大