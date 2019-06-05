# numpy的属性

```python
import numpy as np
```


```python
array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(array)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]



```python
print(array.ndim)#维度
```

    2



```python
print(array.shape)#形状
```

    (3, 3)



```python
print(array.size)#大小
```

    9



```python
print(array.dtype)#元素类型
```

    int32



# 创建array


```python
import numpy as np
```


```python
a = np.array([1,2,3],dtype=np.int32)  #创建array的同时给定类型
print(a.dtype)
```

    int32



```python
b = np.array([1,2,3],dtype=np.float)
print(b.dtype)
```

    float64



```python
c = np.array([1,2,3])#一维数据
print(c)
```

    [1 2 3]



```python
d = np.array([[1,2,3],   #2维矩阵
              [4,5,6]])
print(d)
```

    [[1 2 3]
     [4 5 6]]



```python
zero = np.zeros((2,3)) #生成2行3列全为0的矩阵  zeros矩阵
print(zero)
```

    [[ 0.  0.  0.]
     [ 0.  0.  0.]]



```python
one = np.ones((3,4)) #生成3行4列全为1的矩阵 ones矩阵
print(one)
```

    [[ 1.  1.  1.  1.]
     [ 1.  1.  1.  1.]
     [ 1.  1.  1.  1.]]



```python
empty = np.empty((3,2))#生成3行2列全都接近于0（不等于0）的矩阵
print(empty)
```

    [[ 0.  0.]
     [ 0.  0.]
     [ 0.  0.]]



```python
e = np.arange(10)   #arange的使用
print(e)
```

    [0 1 2 3 4 5 6 7 8 9]



```python
f = np.arange(4,12)
print(f)
```

    [ 4  5  6  7  8  9 10 11]



```python
g = np.arange(1,20,3)
print(g)
```

    [ 1  4  7 10 13 16 19]



```python
h = np.arange(8).reshape(4,2)#重新定义矩阵的形状
print(h)
```

    [[0 1]
     [2 3]
     [4 5]
     [6 7]]

# numpy的运算


```python
import numpy as np
```


```python
arr1 = np.array([[1,2,3],
                 [4,5,6]])
arr2 = np.array([[1,1,2],
                 [2,3,3]])
print(arr1)
print(arr2)
```

    [[1 2 3]
     [4 5 6]]
    [[1 1 2]
     [2 3 3]]



```python
print(arr1 + arr2)   #数组的加法,按位加
```

    [[2 3 5]
     [6 8 9]]



```python
print(arr1 - arr2)  #数组减法,按位减
```

    [[0 1 1]
     [2 2 3]]



```python
print(arr1 * arr2)    #数组乘法,按位乘
```

    [[ 1  2  6]
     [ 8 15 18]]



```python
print(arr1 ** arr2)   #数组双乘号求幂
```

    [[  1   2   9]
     [ 16 125 216]]



```python
print(arr1 / arr2)    #数组除法,按位除
```

    [[ 1.          2.          1.5       ]
     [ 2.          1.66666667  2.        ]]



```python
print(arr1 % arr2)   #数组求余
```

    [[0 0 1]
     [0 2 0]]



```python
print(arr1 // arr2)
```

    [[1 2 1]
     [2 1 2]]



```python
print(arr1+2) #数组所有的元素加2
```

    [[3 4 5]
     [6 7 8]]



```python
print(arr1*10)#数组所有的元素乘以10
```

    [[10 20 30]
     [40 50 60]]



```python
arr3 = arr1 > 3 #判断哪些元素大于3,返回的是布尔类型
print(arr3)
```

    [[False False False]
     [ True  True  True]]



```python
arr4 = np.ones((3,5))
print(arr4)
```

    [[ 1.  1.  1.  1.  1.]
     [ 1.  1.  1.  1.  1.]
     [ 1.  1.  1.  1.  1.]]



```python
print(arr1)
```

    [[1 2 3]
     [4 5 6]]



```python
np.dot(arr1,arr4)#矩阵乘法AB
```




    array([[  6.,   6.,   6.,   6.,   6.],
           [ 15.,  15.,  15.,  15.,  15.]])




```python
arr1.dot(arr4)#矩阵乘法
```




    array([[  6.,   6.,   6.,   6.,   6.],
           [ 15.,  15.,  15.,  15.,  15.]])




```python
print(arr1)
print(arr1.T)#矩阵转置
print(np.transpose(arr1))#矩阵转置
```

    [[1 2 3]
     [4 5 6]]
    [[1 4]
     [2 5]
     [3 6]]
    [[1 4]
     [2 5]
     [3 6]]

# 随机数生成及矩阵的运算2


```python
import numpy as np
```


```python
sample1 = np.random.random((3,2))#生成3行2列从0到1的随机数,调用的是numpy中random的random函数
print(sample1)
```

    [[ 0.42548654  0.60831272]
     [ 0.48034909  0.70289579]
     [ 0.96871932  0.33469266]]



```python
sample2 = np.random.normal(size=(3,2))#生成3行2列符合标准正态分布的随机数,使用的是random中的normal函数(标准正态分布)
print(sample2)
```

    [[ 0.82645622 -0.63300866]
     [ 0.18604463 -0.30988056]
     [-1.50301955 -0.51466896]]



```python
sample3 = np.random.randint(0,10,size=(3,2))#生成3行2列从0到10的随机整数  ,ranint(随机整数)
print(sample3)
```

    [[2 4]
     [3 1]
     [0 3]]



```python
np.sum(sample1)#求和sum
```




    3.5204561139867017




```python
np.min(sample1)#求最小值min
```




    0.33469265548836047




```python
np.max(sample1)#求最大值max
```




    0.96871931960307933




```python
np.sum(sample1,axis=0)#对列求和,关键字axis0就是列,1就是行
```




    array([ 1.87455495,  1.64590117])




```python
np.sum(sample1,axis=1)#对行求和
```




    array([ 1.03379926,  1.18324488,  1.30341198])




```python
print(sample1)
```

    [[ 0.42548654  0.60831272]
     [ 0.48034909  0.70289579]
     [ 0.96871932  0.33469266]]



```python
np.argmin(sample1)#求最小值的索引  argmin(逐行从0开始的,将整个数组看展开成一维的)
```




    5




```python
np.argmax(sample1)#求最大值的索引
```




    4




```python
print(np.mean(sample1))#求平均值
print(sample1.mean())#求平均值
```

    0.586742685664
    0.586742685664



```python
np.median(sample1)#求中位数median
```




    0.5443309058371042




```python
np.sqrt(sample1)#开方
```




    array([[ 0.65229329,  0.77994405],
           [ 0.69307221,  0.8383888 ],
           [ 0.9842354 ,  0.57852628]])




```python
sample4 = np.random.randint(0,10,size=(1,10))
print(sample4)
```

    [[9 2 3 0 2 8 1 3 2 8]]



```python
np.sort(sample4)#排序
```




    array([[0, 1, 2, 2, 2, 3, 3, 8, 8, 9]])




```python
np.sort(sample1)
```




    array([[ 0.42548654,  0.60831272],
           [ 0.48034909,  0.70289579],
           [ 0.33469266,  0.96871932]])




```python
np.clip(sample4,2,7)#小于2就变成2，大于7就变为7  ,数据阈值改变
```




    array([[7, 2, 3, 2, 2, 7, 2, 3, 2, 7]])



# numpy的索引


```python
import numpy as np
```


```python
arr1 = np.arange(2,14)
print(arr1)
```

    [ 2  3  4  5  6  7  8  9 10 11 12 13]



```python
print(arr1[2])#第二个位置的数据,一维
```

    4



```python
print(arr1[1:4])#第一到第四个位置的数据
```

    [3 4 5]



```python
print(arr1[2:-1])#第二到倒数第一个位置的数据
```

    [ 4  5  6  7  8  9 10 11 12]



```python
print(arr1[:5])#前五个数据
```

    [2 3 4 5 6]



```python
print(arr1[-2:])#最后两个数据
```

    [12 13]



```python
arr2 = arr1.reshape(3,4)
print(arr2)
```

    [[ 2  3  4  5]
     [ 6  7  8  9]
     [10 11 12 13]]



```python
print(arr2[1])
```

    [6 7 8 9]



```python
print(arr2[1][1])
```

    7



```python
print(arr2[1,2])
```

    8



```python
print(arr2[:,2])
```

    [ 4  8 12]



```python
for i in arr2: #迭代行
    print(i)
```

    [2 3 4 5]
    [6 7 8 9]
    [10 11 12 13]



```python
for i in arr2.T:#迭代列,转置一下再进行迭代
    print(i)
```

    [ 2  6 10]
    [ 3  7 11]
    [ 4  8 12]
    [ 5  9 13]



```python
for i in arr2.flat:#一个一个元素迭代flat
    print(i)
```

    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13

# array合并


```python
import numpy as np
```


```python
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.vstack((arr1,arr2))#垂直合并vertical(垂直)stack(堆放)
print(arr3)
print(arr3.shape)
```

    [[1 2 3]
     [4 5 6]]
    (2, 3)



```python
arr4 = np.hstack((arr1,arr2))#水平合并horizontal(水平)
print(arr4)
print(arr4.shape)
```

    [1 2 3 4 5 6]
    (6,)



```python
arrv = np.vstack((arr1,arr2,arr3))
print(arrv)
```

    [[1 2 3]
     [4 5 6]
     [1 2 3]
     [4 5 6]]



```python
arrh = np.hstack((arr1,arr2,arr4))
print(arrh)
```

    [1 2 3 4 5 6 1 2 3 4 5 6]



```python
arr = np.concatenate((arr1,arr2,arr1))
print(arr)
```

    [1 2 3 4 5 6 1 2 3]



```python
arr = np.concatenate((arr3,arrv),axis=0)#合并的array维度要相同，array形状要匹配，axis=0纵向合并
print(arr)
```

    [[1 2 3]
     [4 5 6]
     [1 2 3]
     [4 5 6]
     [1 2 3]
     [4 5 6]]



```python
arr = np.concatenate((arr3,arr3),axis=1)#合并的array维度要相同，array形状要匹配，axis=1横向合并
print(arr)
```

    [[1 2 3 1 2 3]
     [4 5 6 4 5 6]]



```python
arr1.T 
print(arr1.T) #一维的array不能转置
```

    [1 2 3]



```python
print(arr1.shape)
```

    (3,)



```python
arr1_1 = arr1[np.newaxis,:]  #添加一个维度到行
print(arr1_1)
print(arr1_1.shape)
```

    [[1 2 3]]
    (1, 3)



```python
print(arr1_1.T)
```

    [[1]
     [2]
     [3]]



```python
arr1_2 = arr1[:,np.newaxis]  #添加维度到列
print(arr1_2)
print(arr1_2.shape)
```

    [[1]
     [2]
     [3]]
    (3, 1)



```python
arr1_3 = np.atleast_2d(arr1)   #atleast_2d  将数据变成2维,维度比他高的不发生改变
print(arr1_3)
print(arr1_3.T)
```

    [[1 2 3]]
    [[1]
     [2]
     [3]]


# array的分割


```python
import numpy as np
```


```python
arr1 = np.arange(12).reshape((3,4))
print(arr1)
```

    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]



```python
arr2,arr3 = np.split(arr1,2,axis=1)#水平方向分割，分成2份split(分割)  将arr1切隔成2个arr2和arr3,在水平方向
print(arr2)
print(arr3)
```

    [[0 1]
     [4 5]
     [8 9]]
    [[ 2  3]
     [ 6  7]
     [10 11]]



```python
arr4,arr5,arr6 = np.split(arr1,3,axis=0)#垂直方向分割，分成3份
print(arr4)
print(arr5)
print(arr6)
```

    [[0 1 2 3]]
    [[4 5 6 7]]
    [[ 8  9 10 11]]



```python
arr2,arr3,arr4 = np.split(arr1,3,axis=1)#水平方向分割，分成3份,没办法切割成相同大小的部分
print(arr2)
print(arr3)
print(arr4)
```


    ---------------------------------------------------------------------------
    
    TypeError                                 Traceback (most recent call last)
    
    ~/anaconda3/lib/python3.6/site-packages/numpy/lib/shape_base.py in split(ary, indices_or_sections, axis)
        552     try:
    --> 553         len(indices_or_sections)
        554     except TypeError:


    TypeError: object of type 'int' has no len()


​    
    During handling of the above exception, another exception occurred:


    ValueError                                Traceback (most recent call last)
    
    <ipython-input-5-2961433b0366> in <module>()
    ----> 1 arr2,arr3,arr4 = np.split(arr1,3,axis=1)#水平方向分割，分成3份
          2 print(arr2)
          3 print(arr3)
          4 print(arr4)


    ~/anaconda3/lib/python3.6/site-packages/numpy/lib/shape_base.py in split(ary, indices_or_sections, axis)
        557         if N % sections:
        558             raise ValueError(
    --> 559                 'array split does not result in an equal division')
        560     res = array_split(ary, indices_or_sections, axis)
        561     return res


    ValueError: array split does not result in an equal division



```python
arr7,arr8,arr9 = np.array_split(arr1,3,axis=1)#水平方向分割，分成3份，不等分割
print(arr7)
print(arr8)
print(arr9)
```

    [[0 1]
     [4 5]
     [8 9]]
    [[ 2]
     [ 6]
     [10]]
    [[ 3]
     [ 7]
     [11]]



```python
arrv1,arrv2,arrv3 = np.vsplit(arr1,3)#垂直分割
print(arrv1)
print(arrv2)
print(arrv3)
```

    [[0 1 2 3]]
    [[4 5 6 7]]
    [[ 8  9 10 11]]



```python
arrh1,arrh2 = np.hsplit(arr1,2)#水平分割
print(arrh1)
print(arrh2)
```

    [[0 1]
     [4 5]
     [8 9]]
    [[ 2  3]
     [ 6  7]
     [10 11]]

# numpy的深拷贝,浅拷贝


```python
import numpy as np
```


```python
arr1 = np.array([1,2,3])
```


```python
arr2 = arr1#arr1,arr2共享一块内存，浅拷贝
```


```python
arr2[0] = 5   #浅拷贝,同步改变
print(arr1)
print(arr2)
```

    [5 2 3]
    [5 2 3]



```python
arr3 = arr1.copy()#深拷贝这里就相当于普通变量的deepcopy
```


```python
arr3[0] = 10
print(arr1)
print(arr3)
```

    [5 2 3]
    [10  2  3]