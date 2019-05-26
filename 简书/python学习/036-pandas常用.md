## 1.pandas基础,Series,DataFrame
```python
import pandas as pd
import numpy as np    #导包
```

```python
s1 = pd.Series([4,7,-5,3])#创建一个series，索引为默认值
print(s1)
```
执行结果:
```
0    4
1    7
2   -5
3    3
dtype: int64
```

```python
s1.values #series的值
```
执行结果:
```python
array([ 4,  7, -5,  3], dtype=int64)
```


```python
s1.index#series的索引
```
执行结果:
```python
RangeIndex(start=0, stop=4, step=1)
```

```python
s2 = pd.Series([4.0,6.5,-0.5,4.2],index=['d','b','a','c'])  #带索引创建一个series
print(s2)
```
执行结果:
```python
d    4.0
b    6.5
a   -0.5
c    4.2
dtype: float64
```

```python
s2['a']#根据索引取值,跟列表相似
```
执行结果:
```python
-0.5
```

```python
s2[['a','b','c']]#根据索引取多行值,记得是双括号,单个值是单括号
```
执行结果:
```python
a   -0.5
b    6.5
c    4.2
dtype: float64
```

```python
'b' in s2   #判断索引在不在series中
```
执行结果:
```python
True
```


```python
'e' in s2
```
执行结果:
```python
False
```


```python
#Series可以看成是一个定长的有序字典,使用字典创建series
dic1 = {'apple':5,'pen':3,'applepen':10}
s3 = pd.Series(dic1)
print(s3)
```
执行结果:
```python
apple        5
pen          3
applepen    10
dtype: int64
```


```python
#DataFrame  ,使用字典创建dataframe
data = {'year':[2014,2015,2016,2017],
        'income':[10000,30000,50000,80000],
        'pay':[5000,20000,30000,30000]
}
df1 = pd.DataFrame(data)
df1
```
执行结果:
```python
	year	income	pay
0	2014	10000	5000
1	2015	30000	20000
2	2016	50000	30000
3	2017	80000	30000
```

```python
df2 = pd.DataFrame(np.arange(12).reshape((3,4)))
df2
```
执行结果:
```python
	0	1	2	3
0	0	1	2	3
1	4	5	6	7
2	8	9	10	11
```
```python
df3 = pd.DataFrame(np.arange(12).reshape((3,4)),index=['a','c','b'],columns=[2,33,44,5])   #创建dataframe时指定索引和列名
df3
```
执行结果:
```python
	2	33	44	5
a	0	1	2	3
c	4	5	6	7
b	8	9	10	11
```
```python
df1.columns #列,取出列名
```
执行结果:
```python
Index(['year', 'income', 'pay'], dtype='object')
```
```python
df1.index #行,取出行索引
```
执行结果:
```python
RangeIndex(start=0, stop=4, step=1)
```
```python
df1.values   #打印dataframe的所有值,是一个数组的形式
```
执行结果:
```python
array([[ 2014, 10000,  5000],
       [ 2015, 30000, 20000],
       [ 2016, 50000, 30000],
       [ 2017, 80000, 30000]], dtype=int64)
```
```python
df1.describe()    #describe描述表,对数据做了一些分析,计数,平均值,标准差,最小值,最大值等等
```
执行结果:
```python
	year	income	pay
count	4.000000	4.000000	4.000000
mean	2015.500000	42500.000000	21250.000000
std	1.290994	29860.788112	11814.539066
min	2014.000000	10000.000000	5000.000000
25%	2014.750000	25000.000000	16250.000000
50%	2015.500000	40000.000000	25000.000000
75%	2016.250000	57500.000000	30000.000000
max	2017.000000	80000.000000	30000.000000
```
```python
df1.T   #对dataframe进行转置
```
执行结果:
```python
	0	1	2	3
year	2014	2015	2016	2017
income	10000	30000	50000	80000
pay	5000	20000	30000	30000
```
```python
df3
```
执行结果:
```python
	2	33	44	5
a	0	1	2	3
c	4	5	6	7
b	8	9	10	11
```
```python
df3.sort_index(axis=1)#列排序,根据列索引名排序
```
执行结果:
```python
	2	5	33	44
a	0	3	1	2
c	4	7	5	6
b	8	11	9	10
```
```python
df3.sort_index(axis=0)#行排序,根据行索引名排序
```
执行结果:
```python

2	33	44	5
a	0	1	2	3
b	8	9	10	11
c	4	5	6	7
```
```python
df3.sort_values(by=44)   #根据列名对值进行排序,全部会变
```
执行结果:
```python

2	33	44	5
a	0	1	2	3
c	4	5	6	7
b	8	9	10	11
```



## 2 pandas选择数据

```python
import pandas as pd
import numpy as np
```
```python
#创建一个dataframe
dates = pd.date_range('20170101',periods=6)   #periods是周期的意思,初始值:20170101
print(dates)
df1 = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df1
```
执行结果:
```python
DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04',
               '2017-01-05', '2017-01-06'],
              dtype='datetime64[ns]', freq='D')
A	B	C	D
2017-01-01	0	1	2	3
2017-01-02	4	5	6	7
2017-01-03	8	9	10	11
2017-01-04	12	13	14	15
2017-01-05	16	17	18	19
2017-01-06	20	21	22	23
```

```python
df1['A']#将DataFrame的列获取为一个Series
```
执行结果:
```python
2017-01-01     0
2017-01-02     4
2017-01-03     8
2017-01-04    12
2017-01-05    16
2017-01-06    20
Freq: D, Name: A, dtype: int32
```
```python
df1.A    ##将DataFrame的列获取为一个Series,跟上面的方法是一样的
```
执行结果:
```python
2017-01-01     0
2017-01-02     4
2017-01-03     8
2017-01-04    12
2017-01-05    16
2017-01-06    20
Freq: D, Name: A, dtype: int32
```
```python
df1[0:2]#取0-1行的dataframe
```
执行结果:
```python
	A	B	C	D
2017-01-01	0	1	2	3
2017-01-02	4	5	6	7
```
```python
df1['20170102':'20170104']   #通过索引取多行
```
执行结果:
```python
	A	B	C	D
2017-01-02	4	5	6	7
2017-01-03	8	9	10	11
2017-01-04	12	13	14	15
```
```python
#通过行标签选择数据
df1.loc['20170102']
```
执行结果:
```python
A    4
B    5
C    6
D    7
Name: 2017-01-02 00:00:00, dtype: int32
```
```python
#通过行标签及列名取数据,先取出行,再取列
df1.loc['20170101',['A','C']]
```
执行结果:
```python
A    0
C    2
Name: 2017-01-01 00:00:00, dtype: int32
```
```python
df1.loc[:,['A','B']]   #取出所有行的某几列
```
执行结果:
```python
	A	B
2017-01-01	0	1
2017-01-02	4	5
2017-01-03	8	9
2017-01-04	12	13
2017-01-05	16	17
2017-01-06	20	21
```
```python
#通过位置选择数据
df1.iloc[2] #第二行
```
执行结果:
```python
A     8
B     9
C    10
D    11
Name: 2017-01-03 00:00:00, dtype: int32
```
```python
df1.iloc[1:3,2:4]   #取得是2-3行,3-4列
```
执行结果:
```python

C	D
2017-01-02	6	7
2017-01-03	10	11
```
```python
df1.iloc[[1,2,4],[1,3]]   #取2,3,5行的2,4列
```
执行结果:
```python
	B	D
2017-01-02	5	7
2017-01-03	9	11
2017-01-05	17	19
```
```python
#混合标签位置选择(标签加位置)
df1.ix[2:4,['A','C']]
```
执行结果:
```python
	A	C
2017-01-03	8	10
2017-01-04	12	14
```
```python
df1.ix['20170102':'20170104',2:4]
```
执行结果:
```python
	C	D
2017-01-02	6	7
2017-01-03	10	11
2017-01-04	14	15
```
```python
df1.A  #按列名取出该列
```
执行结果:
```python
2017-01-01     0
2017-01-02     4
2017-01-03     8
2017-01-04    12
2017-01-05    16
2017-01-06    20
Freq: D, Name: A, dtype: int32
```
```python
df1.A > 6   #提取某一列进行判断
```
执行结果
```
2017-01-01    False
2017-01-02    False
2017-01-03     True
2017-01-04     True
2017-01-05     True
2017-01-06     True
Freq: D, Name: A, dtype: bool
```
```python
df1[df1.A>6]    #将符合判断条件的数据再取出来,这一列数据中大于6的数据
```
执行结果:
```python
A	B	C	D
2017-01-03	8	9	10	11
2017-01-04	12	13	14	15
2017-01-05	16	17	18	19
2017-01-06	20	21	22	23
```

## 3.pandas赋值及操作
```python
import pandas as pd
import numpy as np
```
```python
dates = np.arange(20170101,20170107)
df1 = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df1
```
执行结果:
```python
	A	B	C	D
20170101	0	1	2	3
20170102	4	5	6	7
20170103	8	9	10	11
20170104	12	13	14	15
20170105	16	17	18	19
20170106	20	21	22	23
```

```python
df1.iloc[2,2]    #按照位置取出3行3列的数
```
执行结果:
```python
10
```

```python
df1.iloc[2,2] = 100   #将3行3列位置的数进行重新赋值
df1
```
执行结果:
```python
	A	B	C	D
20170101	0	1	2	3
20170102	4	5	6	7
20170103	8	9	100	11
20170104	12	13	14	15
20170105	16	17	18	19
20170106	20	21	22	23
```


```python
df1.loc[20170102,'B'] = 200   #使用标签取出对应位置的数据进行赋值
df1
```
执行结果:
```python
	A	B	C	D
20170101	0	1	2	3
20170102	4	200	6	7
20170103	8	9	100	11
20170104	12	13	14	15
20170105	16	17	18	19
20170106	20	21	22	23
```


```python
df1[df1.A>10] = 0    #使用条件判断对满足条件的数据进行赋值
df1
```
执行结果:
```python
A	B	C	D
20170101	0	1	2	3
20170102	4	200	6	7
20170103	8	9	100	11
20170104	0	0	0	0
20170105	0	0	0	0
20170106	0	0	0	0
```


```python
df1.A[df1.A==0] = 1
df1
```
执行结果:
```python
	A	B	C	D
20170101	1	1	2	3
20170102	4	200	6	7
20170103	8	9	100	11
20170104	1	0	0	0
20170105	1	0	0	0
20170106	1	0	0	0
```


```python
df1['E'] = 10 #添加一列,这一列的所有数据都是这个数
df1
```
执行结果:
```python
	A	B	C	D	E
20170101	1	1	2	3	10
20170102	4	200	6	7	10
20170103	8	9	100	11	10
20170104	1	0	0	0	10
20170105	1	0	0	0	10
20170106	1	0	0	0	10
```


```python
df1['F'] = pd.Series([1,2,3,4,5,6],index=dates)#添加一列,使用series添加
```
执行结果:
```python
	A	B	C	D	E	F
20170101	1	1	2	3	10	1
20170102	4	200	6	7	10	2
20170103	8	9	100	11	10	3
20170104	1	0	0	0	10	4
20170105	1	0	0	0	10	5
20170106	1	0	0	0	10	6
```

```python
df1.loc[20170107,['A','B','C']] = [1,2,3]   #添加一行中哪些列(按照标签)
df1
```
执行结果:没有赋值的列就是nan
```python
A	B	C	D	E	F
20170101	1.0	1.0	2.0	3.0	10.0	1.0
20170102	4.0	200.0	6.0	7.0	10.0	2.0
20170103	8.0	9.0	100.0	11.0	10.0	3.0
20170104	1.0	0.0	0.0	0.0	10.0	4.0
20170105	1.0	0.0	0.0	0.0	10.0	5.0
20170106	1.0	0.0	0.0	0.0	10.0	6.0
20170107	1.0	2.0	3.0	NaN	NaN	NaN
```
```python
s1 = pd.Series([1,2,3,4,5,6],index=['A','B','C','D','E','F'])
s1.name = 'S1'
df2 = df1.append(s1)  #使用append添加一行(series)
df2
```
执行结果:
```python

A	B	C	D	E	F
20170101	1.0	1.0	2.0	3.0	10.0	1.0
20170102	4.0	200.0	6.0	7.0	10.0	2.0
20170103	8.0	9.0	100.0	11.0	10.0	3.0
20170104	1.0	0.0	0.0	0.0	10.0	4.0
20170105	1.0	0.0	0.0	0.0	10.0	5.0
20170106	1.0	0.0	0.0	0.0	10.0	6.0
20170107	1.0	2.0	3.0	NaN	NaN	NaN
S1	1.0	2.0	3.0	4.0	5.0	6.0
```
```python
df1.insert(1,'G',df2['E'])#在第一列插入索引为G的df2中的E列
df1
```
执行结果:
```python
	                  A	  G	 B	C	D	E	F
20170101	1.0	10.0	1.0	2.0	3.0	10.0	1.0
20170102	4.0	10.0	200.0 6.0	7.0	10.0	2.0
20170103	8.0	10.0	9.0	100.0	11.0	10.0	3.0
20170104	1.0	10.0	0.0	0.0	0.0	10.0	4.0
20170105	1.0	10.0	0.0	0.0	0.0	10.0	5.0
20170106	1.0	10.0	0.0	0.0	0.0	10.0	6.0
20170107	1.0	NaN	2.0	3.0	NaN	NaN	NaN
```
```python
g = df1.pop('G')#弹出G列
df1.insert(6,'G',g)#在最后插入
df1
```
执行结果:
```python
	A	B	C	D	E	F	G
20170101	1.0	1.0	2.0	3.0	10.0	1.0	10.0
20170102	4.0	200.0	6.0	7.0	10.0	2.0	10.0
20170103	8.0	9.0	100.0	11.0	10.0	3.0	10.0
20170104	1.0	0.0	0.0	0.0	10.0	4.0	10.0
20170105	1.0	0.0	0.0	0.0	10.0	5.0	10.0
20170106	1.0	0.0	0.0	0.0	10.0	6.0	10.0
20170107	1.0	2.0	3.0	NaN	NaN	NaN	NaN
```
```python
del df1['G']#删除G列
df1
```
执行结果:
```python
	A	B	C	D	E	F
20170101	1.0	1.0	2.0	3.0	10.0	1.0
20170102	4.0	200.0	6.0	7.0	10.0	2.0
20170103	8.0	9.0	100.0	11.0	10.0	3.0
20170104	1.0	0.0	0.0	0.0	10.0	4.0
20170105	1.0	0.0	0.0	0.0	10.0	5.0
20170106	1.0	0.0	0.0	0.0	10.0	6.0
20170107	1.0	2.0	3.0	NaN	NaN	NaN
```
```python
df2 = df1.drop(['A','B'],axis=1)#删除AB列
df2
```
执行结果:
```python

C	D	E	F
20170101	2.0	3.0	10.0	1.0
20170102	6.0	7.0	10.0	2.0
20170103	100.0	11.0	10.0	3.0
20170104	0.0	0.0	10.0	4.0
20170105	0.0	0.0	10.0	5.0
20170106	0.0	0.0	10.0	6.0
20170107	3.0	NaN	NaN	NaN
```
```python
df2 = df1.drop([20170101,20170102],axis=0)#删除20170101,20170102行,axis=0代表删除的是行
df1
```
执行结果:
```python
	A	B	C	D	E	F
20170101	1.0	1.0	2.0	3.0	10.0	1.0
20170102	4.0	200.0	6.0	7.0	10.0	2.0
20170103	8.0	9.0	100.0	11.0	10.0	3.0
20170104	1.0	0.0	0.0	0.0	10.0	4.0
20170105	1.0	0.0	0.0	0.0	10.0	5.0
20170106	1.0	0.0	0.0	0.0	10.0	6.0
20170107	1.0	2.0	3.0	NaN	NaN	NaN
```
```python
df2
```
执行结果:
```python
	A	B	C	D	E	F
20170103	8.0	9.0	100.0	11.0	10.0	3.0
20170104	1.0	0.0	0.0	0.0	10.0	4.0
20170105	1.0	0.0	0.0	0.0	10.0	5.0
20170106	1.0	0.0	0.0	0.0	10.0	6.0
20170107	1.0	2.0	3.0	NaN	NaN	NaN
```

## 4.pandas处理丢失数据
```python
import pandas as pd
import numpy as np
dates = np.arange(20170101,20170105)
df1 = pd.DataFrame(np.arange(12).reshape((4,3)),index=dates,columns=['A','B','C'])
df1
```
执行结果:
![image.png](https://upload-images.jianshu.io/upload_images/14555448-4fd3276f77a89914.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
df2 = pd.DataFrame(df1,index=dates,columns=['A','B','C','D','E'])   #创建包含nan的dataframe
df2
```
执行:
![image.png](https://upload-images.jianshu.io/upload_images/14555448-aa3f454576feeeb0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
s1 = pd.Series([3,4,6],index=dates[:3])
s2 = pd.Series([32,5,2],index=dates[1:])
df2['D'] = s1
df2['E'] = s2
df2
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-f21640b526361492.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
df2.dropna(axis=0,how='any') #axis=[0,1] 0代表行，1代表列。how=['any','all'] any任意一个或多个 all全部,删除含有空值的行
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-fa99061bd6be4856.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
df2.dropna(axis=1,how='any') #axis=[0,1] 0代表行，1代表列。how=['any','all'] any任意一个或多个 all全部
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-89999aa98c2c4864.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
df2.fillna(value=0)#把空值赋值为0,fill填充的意思
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-1a46d1a26f533e69.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
df2.isnull()#查看空值
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-47de0106196c3984.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
np.any(df2.isnull())#只要有一个或多个空值就会返回true
```
执行结果:
```
True
```
```python
np.all(df2.isnull())#所有为空值才返回true
```
```python
False
```


## 5.pandas读取及写入文件
```python
import pandas as pd
```
```python
file = pd.read_csv('people.csv',encoding='gbk')
file
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-a9e8cb030ae54f5e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
file.iloc[2,0] = '深圳'  #赋值操作
file
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-af17aebcf5ee69ee.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
file.to_csv('people2.csv')  #写入文件
```

## 6.pandas合并,concat
```python
import pandas as pd
import numpy as np
```
```python
df1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=['a','b','c','d'])
df2 = pd.DataFrame(np.arange(12,24).reshape((3,4)),columns=['a','b','c','d'])
df3 = pd.DataFrame(np.arange(24,36).reshape((3,4)),columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-2882579dbe69517f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
df4 = pd.concat([df1,df2,df3],axis=0)#纵向合并,concat连接
df4
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-dd0a8460b07447fb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
df4 = pd.concat([df1,df2,df3],axis=0,ignore_index=True)#纵向合并，不考虑原来的index
df4
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-f1308be14ee26d15.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
df5 = pd.concat([df1,df2,df3],axis=1)#横向合并
df5
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-548140f548ab93dd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
df1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=['a','b','c','f'])
df2 = pd.DataFrame(np.arange(12,24).reshape((3,4)),columns=['a','c','d','e'])
print(df1)
print(df2)
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-62e7dd02c531f383.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
df6 = pd.concat([df1,df2],join='outer',ignore_index=True)#合并两个表，缺少的部分填充NaN
df6
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-6154a3053d6537cc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
df7 = pd.concat([df1,df2],join='inner',ignore_index=True)#合并两个表，缺少的部分去掉
df7
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-90f7a3cca0d3ded2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
df1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=['a','b','c','f'])
df2 = pd.DataFrame(np.arange(12,24).reshape((4,3)),columns=['a','c','d'])
print(df1)
print(df2)
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-a087ec140e2c5e5a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
df8 = pd.concat([df1,df2],axis=1,join_axes=[df1.index])#横向合并，index使用df1的index
df8
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-da4d616c76910a0b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
df8 = pd.concat([df1,df2],axis=1)#横向合并
df8
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-c61ba67a82abbf05.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 7.pandas合并merge
```python
import pandas as pd
```
```python
left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})

print(left)
print(right)
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-74e63532edf06589.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
res = pd.merge(left,right,on='key')   #根据哪一列进行合并
res
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-6305df2fda40969d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
left = pd.DataFrame({'key1':['K0','K0','K1','K2'],
                     'key2':['K0','K1','K0','K1'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right = pd.DataFrame({'key1':['K0','K1','K1','K3'],
                      'key2':['K0','K0','K0','K0'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})

print(left)
print(right)
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-24f953e67474f377.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
#how = ['left','right','inner','outer']
res = pd.merge(left,right,on=['key1','key2'],how='outer')#how默认inner,带缺失值
res
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-6ae0973c9c89001a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
#how = ['left','right','inner','outer']
res = pd.merge(left,right,on=['key1','key2'],how='inner')#how默认inner,不带缺失值
res
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-0fd6e375e56a023f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
#how = ['left','right','inner','outer']
res = pd.merge(left,right,on=['key1','key2'],how='left')#how默认inner,使用left,按照左边表的索引来合并,由于2表中有两个k1,k0行.因此需要两行
res
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-bd52c19f8014d50d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
#how = ['left','right','inner','outer']
res = pd.merge(left,right,on=['key1','key2'],how='outer',indicator=True)#显示merge信息
res
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-85ed8cc3d4c487a2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
#how = ['left','right','inner','outer']
res = pd.merge(left,right,on=['key1','key2'],how='outer',indicator='indicator_column')#显示merge信息
res
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-60c1fe2fc2dcc5f1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
left = pd.DataFrame({'A':['A0','A1','A2'],
                     'B':['B0','B1','B2']},
                     index = ['K0','K1','K2'])
right = pd.DataFrame({'C':['C0','C2','C3'],
                      'D':['D0','D2','D3']},
                      index=['K0','K2','K3'])
print(left)
print(right)
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-16a63ea6b0634805.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
boys = pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})

girls = pd.DataFrame({'k':['K0','K0','K3'],'age':[4,5,6]})

print(boys)
print(girls)
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-e73a3923b8bef496.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


```python
res = pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='outer')   #根据k进行合并,suffixs为了区别合并后的信息
res
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-2215221a7cb96d67.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
## 8.pandas plot
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```
```python
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
# print(data)
data = data.cumsum()  #累加操作
# print(data)    #索引加数据
data.plot()    #调用画图,索引为x,值为y
plt.show()
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-a995a10cee3058dd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=['A','B','C','D'])
data = data.cumsum()
print(data.head())
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-201924360ed4f582.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
data.plot()
plt.show()
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-d17b3685edc90ef2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
ax = data.plot.scatter(x='A',y='B',color='Blue',label='class 1')
data.plot.scatter(x='A',y='C',color='Green',label='class 2',ax=ax)
plt.show()
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-79d9747120e7111e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
## 9 导出csv文件参数的设置
###  to_csv 方法和主要参数
to_csv 方法可以将Series和DataFrame对象输出成逗号分隔的csv文件
```python
df.to_csv(path_or_buf, sep, na_rep, float_format, columns, header, index, index_label, mode, encoding, line_terminator, quoting, quotechar, doublequote, escapechar, chunksize, tupleize_cols, date_format)
```
参数说明
* path_or_buf  ：要保存的路径及文件名
```pyhon
df.to_csv("./output.csv")    #保存在当前文件夹
```
* sep ：分隔符，默认是","
```python
df.to_csv("./output.csv", sep="\t")    #用Tab做分隔符
```
* na_rep ：指定空值的输出方式，默认是空字符串
`float_format `：浮点数的输出格式，要用双引号括起来
```python
df.to_csv("./output.csv", float_format="%.2f")      #浮点数格式表示方法
```
* columns ：指定要输出的列，用列名列表表示，默认是None
注意文档有些地方写的参数名是cols，是不对的
```python
df.to_csv("./output.csv", cols=["month","fruit"])
```
* header ：是否输出列名，默认是True
```python
df.to_csv("./output.csv",header=False)  #不输出列名
```
* index ：是否输出索引，默认是True
```python
df.to_csv("./output.csv",index=False)    #不输出索引
```
* index_label ：索引列的列名，默认是None
```python
df.to_csv("./output.csv",index_label="id")    #索引列的列名为id
```
* encoding ：编码方式，Python2下默认“ascii”，Python3下默认“utf-8”
```python
df.to_csv("./output.csv",encoding="utf-8")
```
* line_terminator ：换行符，默认是'\n'
```python
df.to_csv("./output.csv",line_terminator="\r\n")   #用dos下的换行符输出
```
* quoting ：输出是否用引号，默认参数值为0，表示不加双引号，参数值为1，则每个字段都会加上引号，数值也会被当作字符串看待
```python
df.to_csv("./output.csv",quoting=1)    #给输出的每个字段加上双引号
```
* quotechar ：引用字符，当quoting=1可以指定引号字符为双引号"\""或单引号"\'"
```python
df.to_csv("./output.csv",quoting=1,quotechar="\'")
```
* chunksize ：一次写入csv文件的行数，当df表内容特别大时需要一点一点写入csv文件
```python
df.to_csv("./output.csv",chunksize=100)
```
* date_format ：日期输出格式

## 10pandas重置DataFrame或Series的索引index(重置索引)
当我们在清洗数据时往往会将带有空值的行删除，不论是DataFrame还是Series的index都将不再是连续的索引了，那么这个时候我们可以使用reset_index()方法来重置它们的索引，以便后续的操作。

具体例子1：
```python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(20).reshape(5,4),index=[1,3,4,6,8])
print(df)
```

执行结果:

```python
    0   1   2   3
1   0   1   2   3
3   4   5   6   7
4   8   9  10  11
6  12  13  14  15
8  16  17  18  19
```



* 我们使用`reset_index()`来处理：

  ```python
  print(df.reset_index())
  ```

  执行结果:

  ```python
  index  0   1   2   3
  0      1   0   1   2   3
  1      3   4   5   6   7
  2      4   8   9  10  11
  3      6  12  13  14  15
  4      8  16  17  18  19
  ```

  

* 可以看到此时获得了新的index列，而原来的index变成了我们的数据列，保留了下来。如果我们不想保留原来的index，直接使用重置后的索引，那么可以使用参数drop=True，默认值是False

  ```python
  print(df.reset_index(drop=True))
  ```

  

执行结果:

```python
    0   1   2   3
0   0   1   2   3
1   4   5   6   7
2   8   9  10  11
3  12  13  14  15
4  16  17  18  19
```

`df.reset_index(drop=True)`仅仅只是去除了原本的索引，但是并没有替换，df的索引会有部分缺失。若要直接替换，应该是这样`df.reset_index(drop=True,inplace=True)`

```python
df
Out[4]: 
    0   1   2   3
1   0   1   2   3
3   4   5   6   7
4   8   9  10  11
6  12  13  14  15
8  16  17  18  19
```

在原来的列表上上重置索引

```python
df.reset_index(drop=True,inplace=True)

df
Out[6]: 
    0   1   2   3
0   0   1   2   3
1   4   5   6   7
2   8   9  10  11
3  12  13  14  15
4  16  17  18  19
```

