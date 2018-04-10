### 时间序列分析之Prophect

##### 一、安装

```
pip install fbprophet
```

##### 二、使用

​        输入：ds 和y

​         ds：包含date或者datetime

​          y：需要预测的东西

​      

```
# -*- coding: utf-8 -*-

import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt
# 创建数据
cnt=[10930,10318,10595,10972,7706,6756,9092,10551,9722,10913,11151,8186,6422,
6337,11649,11652,10310,12043,7937,6476,9662,9570,9981,9331,9449,6773,6304,9355,
10477,10148,10395,11261,8713,7299,10424,10795,11069,11602,11427,9095,7707,10767,
12136,12812,12006,12528,10329,7818,11719,11683,12603,11495,13670,11337,10232,
13261,13230,15535,16837,19598,14823,11622,19391,18177,19994,14723,15694,13248,
9543,12872,13101,15053,12619,13749,10228,9725,14729,12518,14564,15085,14722,
11999,9390,13481,14795,15845,15271,14686,11054,10395]
date=pd.date_range('1/1/2010',periods=90,freq='D')
# data=pd.DataFrame({"date":date,"data":cnt})
# data=pd.DataFrame({"data":cnt,"date":date})
d={'ds':date,'y':cnt}
data=pd.DataFrame(data=d)

#更改顺序
cols=list(data)
cols.insert(0,cols.pop(cols.index('ds')))
data=data.ix[:,cols]
#显示数据
# plt.plot(date,cnt)
# plt.show()

#模型拟合
pm=Prophet()
pm.fit(data)

#构建预测时间
future=pm.make_future_dataframe(periods=365)
future.tail()

#预测
forecast=pm.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

#结果显示
# pm.plot(forecast)
# plt.show()

pm.plot_components(forecast)
plt.show()
```

#####  三、注意

​          Prophet模型默认使用线性模型进行预测

​          通过future['cap']=xxx指定预测列最大值 

​          通过future['floor']=xxx指定预测列最小值

​          变化幅度控制： 

```
m = Prophet(changepoints=['2014-01-01'])

m = Prophet(changepoint_prior_scale=0.001)
```

季节性影响与假期影响

```
m=Prophet(weekly_seasonality=False)
m.add_seasonality(name='monthly',period=30.5,fourier_order=5)
```