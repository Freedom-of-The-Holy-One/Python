### Numpy

##### 列表转数组：

```
array=np.array([[1,2,3],[2,5,6],dtype=np.int32/64,float32/64])
array.ndim 维度
array.shape  行列
array.size   元素个数
```

#####  运算：

dot：矩阵乘法

A=np.arrange(2,14).reshape((3,4))

最小值索引：np.argmin(A)

最大值索引：np.argmax(A)

平均值：np.mean(A)    A.mean

中位数：np.median(A)

逐步累加：np.cumsum(A)

求差：np.diff(A)

非零数：np.nonzero(A)

排序：np.sort(A)

转秩：np.transport(A)

范围赋值：np.clip(A,5,9)

列计算：np.meam(A,axis=0)

行计算：np.meam(A,axis=1)

##### 索引

一维：A[2]

二维：

```
A[3][3] 三行三列
A[2][:] 第二行所有数
```

##### 合并

```
A=np.array([1,1,1])
B=np.array([2,2,2])

上下合并：np.vstack((A,B))  (两行三列)

左右合并：np.hstack((A,B))  (一行六列)

行变列：A[np.newaxis,:]
列变行：A[:,np.newaxis]

多个合并：np.concatenate((A,B,B,A),axis=0)[axis=0:上下合并；axis=1:上下合并]         
```

##### 分割

```
np.split()
np.array_split()
np.vsplit()
```

##### 赋值

```
a=b
a=b.copy()
```

