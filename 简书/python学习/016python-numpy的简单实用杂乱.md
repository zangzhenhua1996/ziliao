>#1. 创建一个2*2的数组
```python
import numpy as np #导包
a=np.zeros((2,2))  #生成一个2*2的
print('a的类型: %s' % type(a))
print('a数组的结果: \n %s' %a)
```
执行的结果:
```python
a的类型: <class 'numpy.ndarray'>
a数组的结果: 
 [[0. 0.]
 [0. 0.]]
```

># 2. random.uniform( ) 函数教程与实例解析
* 1. uniform( ) 函数说明
random.uniform(x, y) 方法将随机生成一个实数，它在 [x,y] 范围内。

* 2. uniform( ) 的语法与参数
###2.1 语法
```python
# _*_ coding: utf-8 _*_
import random
random.uniform(x, y)
```
或
```python

# _*_ coding: utf-8 _*_
from random import uniform
uniform(x, y)
```
>> 提示：uniform 包含在random库中，需要使用时需导入random库。

####2.2 参数
x -- 随机数的最小值，包含该值。
y -- 随机数的最大值，不包含该值。
返回一个浮点数
##在numpy中也是可以进行调用的:
例如:
```python

#2利用numpy的random生成一个随机数
b=np.random.uniform(0,80)  #生成一个0-79的随机数
b=int(b)#将生成的随机数转换成整数
print(b)
```
执行的结果:
```python
55
```

>#3 计算数组某两行(列同理)对应的欧几里得距离
```python
a=np.array([1,2])  #第一行
b=np.array([2,3]) #第二行
print('第一行: ',a)
print('第二行: ',b)
print('两行对应列相减:' ,a-b)
ju_li=np.sqrt(sum((a - b)**2))
print('欧几里得距离为: ',ju_li)
```
执行的结果如下:
```python
第一行:  [1 2]
第二行:  [2 3]
两行对应列相减: [-1 -1]
欧几里得距离为:  1.4142135623730951
```


numpy中产生高斯分布的噪声

一
先看伟大的高斯分布（Gaussian Distribution）的概率密度函数（probability density function）： 
![高斯分布](https://upload-images.jianshu.io/upload_images/14555448-2429579cb3f2991a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


Gaussian Distribution(Normal Distribution)其图形特点为中间高，两头低，是钟形曲线(bell-shaped curve)。在高斯分布中，以数学期望μ表示钟型的中心位置（也即曲线的位置），而标准差（standard deviation）σ表征曲线的离散程度。

随机变量X服从数学期望为μ、方差为σ^2的正态分布，记为： 
X = N ( μ, σ^2 ) 
当数学期望为0，方差为1时，该分布为标准正态分布（standard normal distribution）。

高斯分布曲线的特征： 
关于μ对称；总面积为1；在μ加减σ处为拐点（先内翻后外翻。 
此外，我们通过公式可以看出，σ越大，x位置的概率值就越小，说明曲线越平缓（矮小）；而如果σ小，x的概率就大，说明曲线是瘦高的，概率分布比较集中。 
 
如上图所示，红，蓝，橘黄色曲线的数学期望在0点，但蓝色的方差为0.2，所以其最为陡峭，而橘红色曲线的方差为5.0，证明其分布很广，由于曲线的概率总和为1，所以若其分布广，则高度必然会较低。绿色曲线由于其数学期望为－2，所以，在其他三条曲线的左侧。

二
对应于numpy中：
```python
numpy.random.normal(loc=0.0, scale=1.0, size=None)

参数的意义为：

loc：float
    此概率分布的均值（对应着整个分布的中心centre）
scale：float
    此概率分布的标准差（对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高）
size：int or tuple of ints
    输出的shape，默认为None，只输出一个值
```
我们更经常会用到的`np.random.rand(size)`所谓标准正态分布（μ=0,σ=1），对应于`np.random.normal(loc=0, scale=1, size)`。
