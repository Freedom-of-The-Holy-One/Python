# -*- coding:utf-8 -*-
"""
特征抽取之文本数据处理
"""
from sklearn.datasets import fetch_20newsgroups
data=fetch_20newsgroups(subset='all')

from sklearn.model_selection import  train_test_split
train_x,test_x,train_y,test_y=train_test_split(data.data,data.target,test_size=0.25,random_state=33)

# 使用CountVectorizer并且不去掉停用词的情况下，对文本特征进行量化的朴素贝叶斯分类性能测试
# from sklearn.feature_extraction.text import CountVectorizer
# cv=CountVectorizer()
# train_x=cv.fit_transform(train_x)
# test_x=cv.transform(test_x)

# 使用CountVectorizer并且去掉停用词的情况下，对文本特征进行量化的朴素贝叶斯分类性能测试
# from sklearn.feature_extraction.text import CountVectorizer
# cv=CountVectorizer(analyzer='word',stop_words='english')
# train_x=cv.fit_transform(train_x)
# test_x=cv.transform(test_x)

# 使用TfidfVectorizer并且不去掉停用词的情况下，对文本特征进行量化的朴素贝叶斯分类性能测试
# from sklearn.feature_extraction.text import TfidfVectorizer
# tv=TfidfVectorizer()
# train_x=tv.fit_transform(train_x)
# test_x=tv.transform(test_x)

# 使用TfidfVectorizer并且去掉停用词的情况下，对文本特征进行量化的朴素贝叶斯分类性能测试
from sklearn.feature_extraction.text import TfidfVectorizer
tv=TfidfVectorizer(stop_words='english',analyzer='word')
train_x=tv.fit_transform(train_x)
test_x=tv.transform(test_x)

from sklearn.naive_bayes import  MultinomialNB
nu=MultinomialNB()
nu.fit(train_x,train_y)

nu_predict_data=nu.predict(test_x)

# 0.8397707979626485
# print("Accuracy of MultinomialNB(CountVectorizer并且不去掉停用词):"+str(nu.score(test_x,test_y)))
#0.8463497453310697
# print("Accuracy of MultinomialNB(TfidfVectorizer并且不去掉停用词):"+str(nu.score(test_x,test_y)))
#0.8637521222410866
# print("Accuracy of MultinomialNB(CountVectorizer并且去掉停用词):"+str(nu.score(test_x,test_y)))
#0.8826400679117148
print("Accuracy of MultinomialNB(TfidfVectorizer并且去掉停用词):"+str(nu.score(test_x,test_y)))