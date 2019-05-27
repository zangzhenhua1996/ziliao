# 1.matplotlib基础用法

```python
import matplotlib.pyplot as plt
import numpy as np
```


```python
x = np.linspace(-1,1,100)#从-1到1生成100个点,均匀的
y = 2*x + 1
plt.plot(x,y)
plt.show()
```


![output_1_0.png](https://upload-images.jianshu.io/upload_images/14555448-209d7616c6c88de0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


# 2.matplotlib figure图像

```python
import matplotlib.pyplot as plt
import numpy as np
```


```python
x = np.linspace(-1,1,100)
y1 = 2*x + 1
y2 = x**2

plt.figure()   #默认不传参数则生成的都是新的一副图像,如果在figure()中传入的都是同一个数字1,那么画的图像是在一张图上的
plt.plot(x,y1)

plt.figure()
plt.plot(x,y2)

plt.show()
```


![output_1_0.png](https://upload-images.jianshu.io/upload_images/14555448-c6d25854ba079709.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




![output_1_1.png](https://upload-images.jianshu.io/upload_images/14555448-744ce8c9e15f51ed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
x = np.linspace(-1,1,100)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x,y1)

plt.figure(figsize=(8,5))  #设置figure的大小
plt.plot(x,y2)

plt.show()
```


![output_2_0.png](https://upload-images.jianshu.io/upload_images/14555448-5c1d4ae61ee73ba8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



![output_2_1.png](https://upload-images.jianshu.io/upload_images/14555448-5da5d5147e586b98.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 绘制图像在同一副上
```python
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')  #颜色是red,线的宽度是1.0,线的风格是--虚线
plt.plot(x,y2,color='blue',linewidth=5.0,linestyle='-')  #线的风格是实线
plt.show()
```


![output_3_0.png](https://upload-images.jianshu.io/upload_images/14555448-e29e9e2333ab5370.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 3.matplotlib设置坐标轴1


```python
import matplotlib.pyplot as plt
import numpy as np
```


```python
x = np.linspace(-3,3,100)
y1 = 2*x + 1
y2 = x**2

#xy范围(坐标区域),要显示的区域
plt.xlim((-1,2)) #limit限制
plt.ylim((-2,3))

#xy描述
plt.xlabel('I AM X')  #添加标签
plt.ylabel('I AM Y')

plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.plot(x,y2,color='blue',linewidth=5.0,linestyle='-')
plt.show()
```


![output_1_0.png](https://upload-images.jianshu.io/upload_images/14555448-8992eec96eb900f4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




```python
new_ticks = np.linspace(-2,2,11)
print(new_ticks)
```

    [-2.  -1.6 -1.2 -0.8 -0.4  0.   0.4  0.8  1.2  1.6  2. ]



```python
x = np.linspace(-3,3,100)
y1 = 2*x + 1
y2 = x**2

#xy范围
plt.xlim((-1,2))
plt.ylim((-2,3))

#xy描述
plt.xlabel('I AM X')
plt.ylabel('I AM Y')

plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.plot(x,y2,color='blue',linewidth=5.0,linestyle='-')

plt.xticks(new_ticks)   #x坐标显示的尺度
plt.yticks([-1,0,1,2,3],
           ['level1','level2','level3','level4','level5'])  #y方向坐标的尺度(间隔显示的坐标),可以传入两个列表,一个是数字,另一个是数字代替的汉字
plt.show()
```


![output_3_0.png](https://upload-images.jianshu.io/upload_images/14555448-30d21c54c0cf4b33.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


# 4.matplotlib设置坐标轴2

```python
import matplotlib.pyplot as plt
import numpy as np
```


```python
x = np.linspace(-3,3,100)
y1 = 2*x + 1
y2 = x**2

#xy范围
plt.xlim((-1,2))
plt.ylim((-2,3))

#xy描述
plt.xlabel('I AM X')
plt.ylabel('I AM Y')

plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.plot(x,y2,color='blue',linewidth=5.0,linestyle='-')

new_ticks = np.linspace(-2,2,11)
print(new_ticks)

plt.xticks(new_ticks)
plt.yticks([-1,0,1,2,3],
           ['level1','level2','level3','level4','level5'])

#gca get current axis
ax = plt.gca()   #获取坐标轴保存在ax中
#把右边和上边的边框去掉
ax.spines['right'].set_color('red')   #将右边框的颜色设置为红色
ax.spines['top'].set_color('none')    #将上边框的颜色设置为空,就是没有颜色
#把x轴的刻度设置为‘bottom’
#把y轴的刻度设置为‘left’
ax.xaxis.set_ticks_position('bottom')#把x轴的刻度设置为‘bottom’
ax.yaxis.set_ticks_position('left')#把y轴的刻度设置为‘left’
#设置bottom对应到0点
#设置left对应到0点
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.show()
```

    [-2.  -1.6 -1.2 -0.8 -0.4  0.   0.4  0.8  1.2  1.6  2. ]



![output_1_1.png](https://upload-images.jianshu.io/upload_images/14555448-d4678e8ffe1de4fd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 5.matplotlib legend图例


```python
import matplotlib.pyplot as plt
import numpy as np
```


```python
x = np.linspace(-3,3,100)
y1 = 2*x + 1
y2 = x**2

#xy范围
plt.xlim((-1,2))
plt.ylim((-2,3))

#xy描述
plt.xlabel('I AM X')
plt.ylabel('I AM Y')

l1, = plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')  #首先将绘制的线保存到l1中,需要注意的是需要加上逗号
l2, = plt.plot(x,y2,color='blue',linewidth=5.0,linestyle='-')

plt.legend(handles=[l1,l2],labels=['test1','test2'],loc='best')   #放置图例,放置的曲线,曲线的标签,loc(位置)=best就是位置最好的意思


new_ticks = np.linspace(-2,2,11)
print(new_ticks)

plt.xticks(new_ticks)
plt.yticks([-1,0,1,2,3],
           ['level1','level2','level3','level4','level5'])

plt.show()
```

    [-2.  -1.6 -1.2 -0.8 -0.4  0.   0.4  0.8  1.2  1.6  2. ]



![output_1_1.png](https://upload-images.jianshu.io/upload_images/14555448-7d637a4fae8eeb76.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


# 6.matplotlib 标注


```python
import matplotlib.pyplot as plt
import numpy as np
```


```python
x = np.linspace(-1,1,100)
y1 = 2*x + 1

plt.plot(x,y1,color='red',linewidth=1.0,linestyle='-')

#gca get current axis
ax = plt.gca()
#把右边和上边的边框去掉
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#把x轴的刻度设置为‘bottom’
#把y轴的刻度设置为‘left’
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#设置bottom对应到0点
#设置left对应到0点
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

# 不是很懂的地方快捷键查看描述

x0 = 0.5  #标注的x坐标
y0 = 2*x0 + 1  #标注的y\坐标
#画点
plt.scatter(x0,y0,s=50,color='b')  #使用的是离散点, s=50 就是大小
#画虚线
plt.plot([x0,x0],[y0,0],'k--',lw=2)  # 这里其实就是传入了两个x值两个y值,是一一对应的,按照索引(x0,y0)以及(x0,0)  ,黑色虚线,lw就是线款设置为0

#画描述  首先%s %对应的是后面的y0  , xy位置是(x0,y0),xy的文本位置在在x加30y减30的位置,textcoords='offset points'是以一个点为起点
# arrowprops是加上箭头的意思
plt.annotate(r'$2x+1= %s $' % y0,xy=(x0,y0),xytext=(+30,-30),textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))

plt.text(-1,2,r'$this\ is\ the\ text$',fontdict=dict={'size':'16','color':'r'})  #坐标,文本,空格需要加\进行转yi,字体的设置.

plt.show()  #使用plt.show()的原因就是使得自己所有的设置完成了再显示
```


![output_1_0.png](https://upload-images.jianshu.io/upload_images/14555448-52c8ba759dde3417.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




# 7.matplotlib scatter散点图


```python
import matplotlib.pyplot as plt
import numpy as np
```


```python
plt.scatter(np.arange(5),np.arange(5))
plt.show()
```

![output_1_0.png](https://upload-images.jianshu.io/upload_images/14555448-c07dc056b08a34da.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
x = np.random.normal(0,1,500)
y = np.random.normal(0,1,500)

plt.scatter(x,y,s=50,c='b',alpha=0.5)# c就是颜色,alpha=0.5设置的颜色的透明度

plt.xlim((-2,2))
plt.ylim((-2,2))

plt.xticks(())    #取消显示边框的尺度,什么参数不传入就可以取消
plt.yticks(())

plt.show()
```


![output_2_0.png](https://upload-images.jianshu.io/upload_images/14555448-f4834714866be2eb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 8.matplotlib bar直方图


```python
import matplotlib.pyplot as plt
import numpy as np
```


```python
x = np.arange(10)
y = 2**x + 10
plt.bar(x,y)
plt.show()
```


![output_1_0.png](https://upload-images.jianshu.io/upload_images/14555448-5fee7bde3a44e46c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




```python
x = np.arange(10)
y = 2**x + 10
plt.bar(x,-y)
plt.show()
```


![output_2_0.png](https://upload-images.jianshu.io/upload_images/14555448-cd0a996fe098cdaa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




```python
x = np.arange(10)
y = 2**x + 10
plt.bar(x,y,facecolor='#9999ff',edgecolor='white')  #facecolor设置的柱子里面的颜色,edgecolor设置的是柱子边框的颜色
plt.show()
```


![output_3_0.png](https://upload-images.jianshu.io/upload_images/14555448-145d342265fba41c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




```python
x = np.arange(10)
y = 2**x + 10
plt.bar(x,y,facecolor='#9999ff',edgecolor='white')
for x,y in zip(x,y):  #使用for循环给柱子上加上值,zip的意思是将x和y打包成一个整体,每次循环可以同时读取一个x和y
    plt.text(x+0.4,y,'%.2f' % y,ha='center',va='bottom')  #ha代表显示在柱子中心,va=bottom表示柱子在数字的下面

plt.show()
```

![output_4_0.png](https://upload-images.jianshu.io/upload_images/14555448-a4bed52b80ef2339.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 9.matplotlib contours等高线图


```python
import matplotlib.pyplot as plt
import numpy as np
```


```python
def f(x, y):   #定义的是xy对应的高度
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2) 

x = np.linspace(-3,3,100)  #横坐标
y = np.linspace(-3,3,100)  #纵坐标

X,Y = np.meshgrid(x,y)  #生成一个网格
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)  #X,Y,高度函数, 8是线的个数  ,alpha是透明度,cmap是颜色,plt.cm.hot是热力图颜色
# 给等高线加上框
C = plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=.5)
plt.clabel(C,inline=True,fontsize=10)  #等高线的描述
 
plt.xticks(())
plt.yticks(())
plt.show()
```

    /home/dlut/anaconda3/lib/python3.6/site-packages/matplotlib/contour.py:960: UserWarning: The following kwargs were not used by contour: 'linewidth'
      s)



![output_1_1.png](https://upload-images.jianshu.io/upload_images/14555448-c33523974270cd1a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



# 10.matplotlib 3D图


```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  #导入绘制3D图的包
```


```python
fig = plt.figure()  # 
ax = Axes3D(fig)  #建立一个3d的视图

x = np.arange(-4,4,0.25)
y = np.arange(-4,4,0.25)

X,Y = np.meshgrid(x,y)  #XY的坐标网格
R = np.sqrt(X**2 + Y**2)  
Z = np.sin(R)  #Z坐标

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow')) #绘制3D图，X，Y，Z，x方向，y方向的色块大小   ，颜色是彩虹色
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')  # 需要映射的方向是z方向（也可以自己定义），offset映射的位置是-2
ax.set_zlim(-2,2)

plt.show()
```

![output_1_0.png](https://upload-images.jianshu.io/upload_images/14555448-b074af592ce502f3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 11.matplotlib subplot 子图像


```python
import matplotlib.pyplot as plt
import numpy as np
```


```python
plt.figure()
plt.subplot(2,2,1)  #绘制同等大小的子图像
plt.plot([0,1],[0,1])

plt.subplot(2,2,2)
plt.plot([0,1],[0,1])

plt.subplot(223)
plt.plot([0,1],[0,1])

plt.subplot(224)
plt.plot([0,1],[0,1])

plt.show()
```


![output_1_0.png](https://upload-images.jianshu.io/upload_images/14555448-d89a6d098136a700.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




```python
plt.figure()  #绘制不同大小的子图
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])

plt.subplot(2,3,4)
plt.plot([0,1],[0,1])

plt.subplot(235)
plt.plot([0,1],[0,1])

plt.subplot(236)
plt.plot([0,1],[0,1])

plt.show()
```


![output_2_0.png](https://upload-images.jianshu.io/upload_images/14555448-03b37c6350497439.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



# 12.matplotlib 动态图


```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation  #导入绘制动态图的包
```


```python
# 需要使用ipython观看
fig,ax = plt.subplots()

x = np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))  #画一条线，一定注意这样的一定要加逗号

def animate(i):  
    line.set_ydata(np.sin(x+i/10))
    return line,

def init():  #初始化的函数
    line.set_ydata(np.sin(x))
    return line,

ani = animation.FuncAnimation(fig=fig,func=animate,init_func=init,interval=200)    #interval=200间隔的改变是200ms
plt.show()
```


![output_1_0.png](https://upload-images.jianshu.io/upload_images/14555448-1683aaf1bcac5a97.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)