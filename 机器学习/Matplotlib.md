#### Matplotlib

```
基本使用
plt.plot(x,y)
plt.show()

figure参数
figure：
figure(num=1,figsize=(8,5))

设置多个显示区域
plt.figure()   创建figure,画图
plt.plot(x1,y1,color='',linewidth=,linestyle='--'，label='')

plt.figure()
plt.plot(x2,y2)

设置坐标轴
plt.xlim((1,2))
plt.ylim((2,3))
plt.xlabel('')
plt.ylabel('')
plt.xticks()
plt.yticks([-2,3],[r'$a$','b'])

坐标轴修改
#gac='get current axis'
ax=plt.gca()
上边、右边坐标轴消失
ax.spines['right'.set_color('none')]
ax.spines['top'.set_color('none')]
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',-1))

图例
plt.legend(handles=[l1,l2],labels=['xxx','xxx'],loc='best')

注解
plt.scatter(x0,y0,size=,color='')
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)
plt.annotate(r'$xxx$',xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle=''))
plt.text(-3.7,3,r'$xxx$')

坐标轴刻度
ax.get_xticklables()

散点图
t=np.arctan2(Y,X)  设置颜色
plt.scatter(X,Y,s=75,c=t,alpha=0.5)
plt.xlim((-1.5,1.5))

柱状图
plt.bar(X,+Y，facecolor='#999ff',edgecolor='white'[边框颜色])   向上
plt.bar(X,-Y)   向下
for x,y in zip(x,y):  添加数值
    plt.text(x+0.4,y+0.05,'%.2f'%y，ha='center',va='bottom')
    
等高线图
plt.contourf()
plt.counter()

图片
plt.imshow()
plt.colorbar()

3D数据
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=Axes3D(fig)
ax.plot_surface()
ax.contour()

多个显示
plt.figure()
plt.subplot(2,2,1)   plt.subplot(2,1,1)
plt.plot([0,1],[0,1])

plt.subplot(2,2,2)   plt.subplot(2,3,4)
plt.plot([0,1],[0,1])

plt.subplot(2,2,3)   plt.subplot(2,3,5)
plt.plot([0,1],[0,1])

plt.subplot(2,2,4)   plt.subplot(2,2,6)
plt.plot([0,1],[0,1])

plt.show()

分格显示
```