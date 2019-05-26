

> ### Sklearn 简介

Scikit learn 也简称 [sklearn](https://link.jianshu.com?t=http://scikit-learn.org/stable/), 是机器学习领域当中最知名的 python 模块之一.

Sklearn 包含了很多种机器学习的方式:

*   Classification 分类
*   Regression 回归
*   Clustering 非监督分类
*   Dimensionality reduction 数据降维
*   Model Selection 模型选择
*   Preprocessing 数据预处理

> ### 选择模型流程

学习 Sklearn 时，不要直接去用，先了解一下都有什么模型方法，然后选择适当的方法，来达到你的目标。

Sklearn 官网提供了一个流程图(英文)，这里找了一张中文的.蓝色圆圈内是判断条件，绿色方框内是可以选择的算法：
![sklearn方法的选择.png](https://upload-images.jianshu.io/upload_images/14555448-630afae65c27847b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

从 开始位置 开始，首先看数据的样本是否 >50，小于则需要收集更多的数据。

由图中，可以看到算法有四类，分类，回归，聚类，降维。
* 其中 分类和回归是监督式学习，即每个数据对应一个 label。
* 聚类 是非监督式学习，即没有 label。
* 另外一类是 降维，当数据集有很多很多属性的时候，可以通过 降维 算法把属性归纳起来。例如 20 个属性只变成 2 个，注意，这不是挑出 2 个，而是压缩成为 2 个，它们集合了 20 个属性的所有特征，相当于把重要的信息提取的更好，不重要的信息就不要了。
然后看问题属于哪一类问题，是分类还是回归，还是聚类，就选择相应的算法。
当然还要考虑数据的大小，例如 100K 是一个阈值。
* 可以发现有些方法是既可以作为分类，也可以作为回归，例如 SGD。


> ### 应用模型(鸢尾花的例子)

Sklearn 把所有机器学习的模式整合统一起来了，学会了一个模式就可以通吃其他不同类型的学习模式。
例如:分类器，
Sklearn 本身就有很多数据库，可以用来练习。
我们用其中 Iris 的数据为例，这种花有四个属性，花瓣的长宽，茎的长宽，根据这些属性把花分为三类。
我们要用 分类器 去把四种类型的花分开。

![鸢尾花](https://upload-images.jianshu.io/upload_images/14555448-d8d947bed9886f27.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

今天用 KNN classifier，就是选择几个临近点，综合它们做个平均来作为预测值。

> ###使用模型的步骤：
* 导入模块
* 创建数据
* 建立模型－训练－预测
整体的代码:
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:02:03 2019

@author: zzh
"""
#导入模块
import numpy as np
#从sklearn中倒入数据集
from sklearn import datasets 
#切分训练集测试集的模块
#from sklearn.cross_validation import train_test_split 
from sklearn.model_selection import train_test_split 
#scikit-learn K最近邻分类器(KNN算法) KNeighborsClassifier 使用
from sklearn.neighbors import KNeighborsClassifier  

#导入数据
#使用的鸢尾花的数据集
iris =datasets.load_iris()  
iris_X=iris.data  #数据的特征(4个属性)
iris_Y=iris.target#数据的标签(3个分类,0,1,2)

print(iris_X[:2,:])
print(iris_Y[0:2])

#数据的切割(7:3),数据会被打乱
X_train,X_test,y_train,y_test=train_test_split(iris_X,iris_Y,test_size=0.3)
#print(y_train)

#创建KNN模型对象
knn = KNeighborsClassifier()
#利用knn模型进行训练
knn.fit(X_train, y_train)  #传如的是训练数据及标签
#用训练好的model进行预测使用的是predict函数
print(knn.predict(X_test)) #预测出的标签
print(y_test)  #实际的标签
```
> ### Sklearn中的数据集:

sklearn 的数据集有好多个种

* 自带的小数据集（packaged dataset）：sklearn.datasets.load_<name>
* 可在线下载的数据集（Downloaded Dataset）：sklearn.datasets.fetch_<name>
* 计算机生成的数据集（Generated Dataset）：sklearn.datasets.make_<name>
* svmlight/libsvm格式的数据集:sklearn.datasets.load_svmlight_file(...)
* 从买了data.org在线下载获取的数据集:sklearn.datasets.fetch_mldata(...)

①自带的数据集

其中的自带的小的数据集为：sklearn.datasets.load_<name>
![自带的小的数据集](https://upload-images.jianshu.io/upload_images/14555448-9fbc94beb63a2dc9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

* 手写数字数据集load_digits()：用于多分类任务的数据集
* 乳腺癌数据集load-barest-cancer（）：简单经典的用于二分类任务的数据集

* 糖尿病数据集：load-diabetes（）：经典的用于回归认为的数据集，值得注意的是，这10个特征中的每个特征都已经被处理成0均值，方差归一化的特征值，

* 波士顿房价数据集：load-boston（）：经典的用于回归任务的数据集

* 体能训练数据集：load-linnerud（）：经典的用于多变量回归任务的数据集，其内部包含两个小数据集：Excise是对3个训练变量的20次观测（体重，腰围，脉搏），physiological是对3个生理学变量的20次观测（引体向上，仰卧起坐，立定跳远）

* svmlight/libsvm的每一行样本的存放格式：

  <label><feature-id>:<feature-value> <feature-id>:<feature-value> ....

这种格式比较适合用来存放稀疏数据，在sklearn中，用scipy sparse CSR矩阵来存放X，用numpy数组来存放Y

②生成数据集

生成数据集：可以用来分类任务，可以用来回归任务，可以用来聚类任务，用于流形学习的，用于因子分解任务的

用于分类任务和聚类任务的：这些函数产生样本特征向量矩阵以及对应的类别标签集合

* make_blobs：多类单标签数据集，为每个类分配一个或多个正太分布的点集

* make_classification：多类单标签数据集，为每个类分配一个或多个正太分布的点集，提供了为数据添加噪声的方式，包括维度相关性，无效特征以及冗余特征等

* make_gaussian-quantiles：将一个单高斯分布的点集划分为两个数量均等的点集，作为两类

* make_hastie-10-2：产生一个相似的二元分类数据集，有10个维度

* make_circle和make_moom产生二维二元分类数据集来测试某些算法的性能，可以为数据集添加噪声，可以为二元分类器产生一些球形判决界面的数据

例子:用到了再说
```python
#生成多类单标签数据集
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
center=[[1,1],[-1,-1],[1,-1]]
cluster_std=0.3
X,labels=make_blobs(n_samples=200,centers=center,n_features=2,
                    cluster_std=cluster_std,random_state=0)
print('X.shape',X.shape)
print("labels",set(labels))

unique_lables=set(labels)
colors=plt.cm.Spectral(np.linspace(0,1,len(unique_lables)))
for k,col in zip(unique_lables,colors):
    x_k=X[labels==k]
    plt.plot(x_k[:,0],x_k[:,1],'o',markerfacecolor=col,markeredgecolor="k",
             markersize=14)
plt.title('data by make_blob()')
plt.show()

#生成用于分类的数据集
from sklearn.datasets.samples_generator import make_classification
X,labels=make_classification(n_samples=200,n_features=2,n_redundant=0,n_informative=2,
                             random_state=1,n_clusters_per_class=2)
rng=np.random.RandomState(2)
X+=2*rng.uniform(size=X.shape)

unique_lables=set(labels)
colors=plt.cm.Spectral(np.linspace(0,1,len(unique_lables)))
for k,col in zip(unique_lables,colors):
    x_k=X[labels==k]
    plt.plot(x_k[:,0],x_k[:,1],'o',markerfacecolor=col,markeredgecolor="k",
             markersize=14)
plt.title('data by make_classification()')
plt.show()

#生成球形判决界面的数据
from sklearn.datasets.samples_generator import make_circles
X,labels=make_circles(n_samples=200,noise=0.2,factor=0.2,random_state=1)
print("X.shape:",X.shape)
print("labels:",set(labels))

unique_lables=set(labels)
colors=plt.cm.Spectral(np.linspace(0,1,len(unique_lables)))
for k,col in zip(unique_lables,colors):
    x_k=X[labels==k]
    plt.plot(x_k[:,0],x_k[:,1],'o',markerfacecolor=col,markeredgecolor="k",
             markersize=14)
plt.title('data by make_moons()')
plt.show()
```


小例子:波士顿房价,以及生成一些线性的点
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import print_function
from sklearn import datasets
#使用线性回归
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#加载数据使用的是load,这里使用的是boston房价的数据
loaded_data = datasets.load_boston() 

data_X = loaded_data.data #数据特征

data_y = loaded_data.target #数据标签

#创建模型
model = LinearRegression()  
#训练模型
model.fit(data_X, data_y)

print(model.predict(data_X[:4, :]))  #预测前四个数据
print(data_y[:4])

#自己生成数据_线性的100个有一个特征,1个标签,噪声为10(方差吧)的数据
X, y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=10)
plt.scatter(X, y)  #散点图
plt.show()
```
执行的结果:

![image.png](https://upload-images.jianshu.io/upload_images/14555448-87d22e3638050535.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ### sklearn中model常用的属性和功能
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import print_function
from sklearn import datasets
from sklearn.linear_model import LinearRegression#(线性回归)

loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target

model = LinearRegression()
model.fit(data_X, data_y)

print(model.predict(data_X[:4, :])) #预测
print("参数w1-wn: \n",model.coef_)  #假设拟合曲线方程y=0.1x+0.3  ,则输出的参数是0.1  
print("截距w0: \n",model.intercept_) #假设拟合曲线方程y=0.1x+0.3  ,则输出的参数是0.3(截距)
print(model.get_params())  #返回的给model定义的参数,没有定义则是默认值

#model学到的东西进行一个打分(用data_X作预测,与data_y作对比看一下跟结果有多吻合)
#使用的是 coefficient of determination (决定系数) 来判断 回归方程 拟合的程度
#决定系数也就是说: 通过回归方程得出的 dependent variable 有 number% 能被 independent variable 所解释. 判断拟合的程度
print(model.score(data_X, data_y)) # R^2 coefficient of determination

```
>  ### 预处理数据

当我们拿到一批原始的数据

* 首先要明确有多少特征，哪些是连续的，哪些是类别的。
* 检查有没有缺失值，对缺失的特征选择恰当方式进行弥补，使数据完整。
* 对连续的数值型特征进行标准化，使得均值为0，方差为1。
* 对类别型的特征进行one-hot编码。
* 将需要转换成类别型数据的连续型数据进行二值化。
* 为防止过拟合或者其他原因，选择是否要将数据进行正则化。
* 在对数据进行初探之后发现效果不佳，可以尝试使用多项式方法，寻找非线性的关系。
* 根据实际问题分析是否需要对特征进行相应的函数转换。

1. 标准化：去均值，方差规模化
Standardization标准化:将特征数据的分布调整成标准正太分布，也叫高斯分布，也就是使得数据的均值为0，方差为1.

标准化的原因在于如果有些特征的方差过大，则会主导目标函数从而使参数估计器无法正确地去学习其他特征。

标准化的过程为两步：去均值的中心化（均值变为0）；方差的规模化（方差变为1）。

在sklearn.preprocessing(预处理)中提供了一个scale的方法，可以实现以上功能
例:
```python
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:44:39 2019

@author: zangz
"""


# 预处理数据的方法总结（使用sklearn-preprocessing）
from sklearn import preprocessing
import numpy as np
# 1. 标准化：去均值，方差规模化
 
# 创建一组特征数据，每一行表示一个样本，每一列表示一个特征
# Standardization标准化:将特征数据的分布调整成标准正太分布，也叫高斯分布，也就是使得数据的均值维0，方差为1.
# 标准化的原因在于如果有些特征的方差过大，则会主导目标函数从而使参数估计器无法正确地去学习其他特征。
# 标准化的过程为两步：去均值的中心化（均值变为0）；方差的规模化（方差变为1）。
# 在sklearn.preprocessing中提供了一个scale的方法，可以实现以上功能。
x = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])
# 将每一列特征标准化为标准正太分布，注意，标准化是针对每一列而言的
x_scale = preprocessing.scale(x)
print("未标准化的数据: \n", x)
print('标准化后的数据: \n',x_scale)

print("矩阵的维度: \n",x_scale.shape)

# 可以查看标准化后的数据的均值与方差，已经变成0,1了
# axis=0 表示对每一列

# axis=1表示对每一行去做这个操作，axis=0表示对每一列做相同的这个操作

print("矩阵每一列的均值: \n",x_scale.mean(axis=0))

# 同理，看一下标准差
print("矩阵每一列的标准差: \n",x_scale.std(axis=0))


```
执行结果:
```python
未标准化的数据: 
 [[ 1. -1.  2.]
 [ 2.  0.  0.]
 [ 0.  1. -1.]]
标准化后的数据: 
 [[ 0.         -1.22474487  1.33630621]
 [ 1.22474487  0.         -0.26726124]
 [-1.22474487  1.22474487 -1.06904497]]
矩阵的维度: 
 (3, 3)
矩阵每一列的均值: 
 [0. 0. 0.]
矩阵每一列的标准差: 
 [1. 1. 1.]

```

 preprocessing这个模块还提供了一个实用类StandarScaler，它可以在训练数据集上做了标准转换操作之后，把相同的转换应用到测试训练集中。

这是相当好的一个功能。可以对训练数据，测试数据应用相同的转换，以后有新的数据进来也可以直接调用，不用再重新把数据放在一起再计算一次了。
```python

# preprocessing这个模块还提供了一个实用类StandarScaler，它可以在训练数据集上做了标准转换操作之后，把相同的转换应用到测试训练集中。
# 这是相当好的一个功能。可以对训练数据，测试数据应用相同的转换，以后有新的数据进来也可以直接调用，不用再重新把数据放在一起再计算一次了。
# 调用fit方法，根据已有的训练数据创建一个标准化的转换器
# 另外，StandardScaler()中可以传入两个参数：with_mean,with_std.这两个都是布尔型的参数，
# 默认情况下都是true,但也可以自定义成false.即不要均值中心化或者不要方差规模化为1.
scaler = preprocessing.StandardScaler().fit(x)  #实例化对象
 
scaler
```
执行结果:
```python
StandardScaler(copy=True, with_mean=True, with_std=True)
```
```python
# 使用上面这个转换器去转换训练数据x,调用transform方法
x_tran=scaler.transform(x)  #x数据时不会变的,只能把变化的数据赋值给新的变量
print(x_tran)
########################################
# 好了，比如现在又来了一组新的样本，也想得到相同的转换
new_x = [[-1., 1., 0.]]
scaler.transform(new_x)
##################################

```
执行结果:
```python
[[ 0.         -1.22474487  1.33630621]
 [ 1.22474487  0.         -0.26726124]
 [-1.22474487  1.22474487 -1.06904497]]
Out[18]: array([[-2.44948974,  1.22474487, -0.26726124]])
```


```python
# MinMaxScaler
# 在MinMaxScaler中是给定了一个明确的最大值与最小值。它的计算公式如下：
# X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
# X_scaled = X_std / (max - min) + min
# 以下这个例子是将数据规与[0,1]之间，每个特征中的最小值变成了0，最大值变成了1，请看：
min_max_scaler = preprocessing.MinMaxScaler()
x_minmax = min_max_scaler.fit_transform(x)
print(x_minmax)
################################################################################
# 同样的，如果有新的测试数据进来，也想做同样的转换咋办呢？请看：
x_test = np.array([[-3., -1., 4.]])
x_test_minmax = min_max_scaler.transform(x_test)
x_test_minmax
################################################################################
```
执行结果:
```python
[[0.5        0.         1.        ]
 [1.         0.5        0.33333333]
 [0.         1.         0.        ]]
Out[23]: array([[-1.5       ,  0.        ,  1.66666667]])
```

```python
 MaxAbsScaler

原理与上面的很像，只是数据会被规模化到[-1,1]之间。也就是特征中，所有数据都会除以最大值。这个方法对那些已经中心化均值维0或者稀疏的数据有意义。
```
莫凡python的标准化例子:(使用标准化scale)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:29:57 2019

@author: zzh
"""

from __future__ import print_function
from sklearn import preprocessing  #(预处理)
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC  #svm中的一种方法
import matplotlib.pyplot as plt

a = np.array([[10, 2.7, 3.6],
              [-100, 5, -2],
              [120, 20, 40]], dtype=np.float64)
print(a)
print(preprocessing.scale(a))

X, y = make_classification(n_samples=300, n_features=2 , n_redundant=0, n_informative=2,
                           random_state=22, n_clusters_per_class=1, scale=100)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()
X = preprocessing.scale(X)    # normalization step
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)
clf = SVC() #建模
clf.fit(X_train, y_train) #训练
print(clf.score(X_test, y_test)) #评价得分
```

执行结果:评价得分

```python
0.9555555555555556
```

不使用scale:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:29:57 2019

@author: zzh
"""

from __future__ import print_function
from sklearn import preprocessing  #(预处理)
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC  #svm中的一种方法
import matplotlib.pyplot as plt

a = np.array([[10, 2.7, 3.6],
              [-100, 5, -2],
              [120, 20, 40]], dtype=np.float64)
print(a)
print(preprocessing.scale(a))

X, y = make_classification(n_samples=300, n_features=2 , n_redundant=0, n_informative=2,
                           random_state=22, n_clusters_per_class=1, scale=100)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()
#X = preprocessing.scale(X)    # normalization step
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)
clf = SVC()
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
```

执行结果:评价得分

```python
0.4888888888888889
```
