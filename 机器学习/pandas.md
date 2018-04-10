#### pandas

```
s=pd.Series([1,3,6,np.nan])

dates=pd.data_range('20160101',periods=6)

df=pd.DataFrame(mp.random.randn(6,4),index=dates[行名],columns=['a','b','c','d'][列名])

df=pd.DataFrame({'A':1,'B':pd.Timestamp('20030101')})
df.dtypes
df.index
df.columns
df.describe()
df['A']/df.A：获取某一列数据
df[0:3]/df['20130101':'20130104']:选取某几列数据

数据筛选：
df.loc['20120102']:以标签选择
df.loc[:,['A','B']]：所有行，A、B列
df.iloc[3,1]：根据index选择
df.ix[]：标签，序列混合
df[df.A>8]
df.B[df.A>4]=0
df['f']=np.nan
df['e']=pd.series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6))

导入导出数据
csv数据：pd.read_csv()    sep:(',':csv) ('\t':table)

合并多个DataFrame
concatenating
pd.concat([df1,df2,df3],axis=0,ignore_index=true)
pd.concat([df1,df2,df3],axis=1)
pd.concat([df1,df2],join='inner'/'outer',ignore_index=true)

join_axes：纵向
append：横向

merge：合并

plot：图表
data.plot()
plt.show()
plt.scatter(x=,y=)
plot('bar','box','pie'......)

ax=data.plot.scatter(x='',y='',color='',label='')
data.plot.scatter(x='',y='',color='',label='',ax=ax)



```

