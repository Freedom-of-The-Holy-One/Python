# -*- coding:utf-8 -*-
"""
朴素贝叶斯实践之对新闻文本数据分类
"""
from sklearn.datasets import fetch_20newsgroups
data=fetch_20newsgroups(subset='all')
# print(data.data[0])

from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(data.data,data.target,train_size=0.75,random_state=33)

# 文本向量特征转换
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
train_x=cv.fit_transform(train_x)
test_x=cv.transform(test_x)

from sklearn.naive_bayes import MultinomialNB
mn=MultinomialNB()
mn.fit(train_x,train_y)
mn_predict_data=mn.predict(test_x)

print("Accuracy:"+str(mn.score(test_x,test_y)))
