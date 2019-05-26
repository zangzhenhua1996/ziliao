## 什么是 Multiprocessing
和 threading 的比较:
多进程 Multiprocessing 和多线程 threading 类似, 他们都是在 python 中用来并行运算的. 不过既然有了 threading, 为什么 Python 还要出一个 multiprocessing 呢? 原因很简单, 就是用来弥补 threading 的一些劣势, 比如在 threading [教程中提到的GIL](https://morvanzhou.github.io/tutorials/python-basic/threading/5-GIL/).

使用 multiprocessing 也非常简单, 如果对 threading 有一定了解的朋友, 你们的享受时间就到了. 因为 python 把 multiprocessing 和 threading 的使用方法做的几乎差不多. 这样我们就更容易上手. 也更容易发挥你电脑多核系统的威力了!


## 导入线程进程标准模块

```python
import multiprocessing as mp #多进程模块
import threading as td    #多线程模块

```

## 定义一个被线程和进程调用的函数 

```
def job(a,d):
    print('aaaaa')

```

## 创建线程和进程 

```python
t1 = td.Thread(target=job,args=(1,2))
p1 = mp.Process(target=job,args=(1,2))

```

注意：Thread和Process的首字母都要大写，被调用的函数没有括号，被调用的函数的参数放在args(…)中

分别启动线程和进程

```python
t1.start()
p1.start()

```

分别连接线程和进程

```python
t1.join()
p1.join()

```

## 完整的线程和进程创建使用对比代码

```python
import multiprocessing as mp
import threading as td

def job(a,d):
    print('aaaaa')

t1 = td.Thread(target=job,args=(1,2))
p1 = mp.Process(target=job,args=(1,2))
t1.start()
p1.start()
t1.join()
p1.join()

```

从上面的使用对比代码可以看出，线程和进程的使用方法相似

## 运用

> 在运用时需要添加上一个定义main函数的语句(必须要有):原因：多进程需要在main函数中运行，

```python
if __name__=='__main__':

```

完整的应用代码：

```
import multiprocessing as mp  #导包

def job(a,d):  #定义函数功能
    print('aaaaa')

if __name__=='__main__':
    p1 = mp.Process(target=job,args=(1,2))  #创建一个进程
    p1.start()   #开启进程
    p1.join()   #连接进程

```

运行环境要在terminal环境下，可能其他的编辑工具会出现运行结束后没有打印结果，在terminal中的运行后打印的结果为：

```python
aaaaa
```
![多进程](https://upload-images.jianshu.io/upload_images/14555448-cda9e35b156ee8f8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


### 存储进程输出 Queue
Queue的功能是将每个核或线程的运算结果放在队里中， 等到每个线程或核运行完毕后再从队列中取出结果， 继续加载运算。原因很简单, 多线程调用的函数不能有返回值, 所以使用Queue存储多个线程运算的结果
> 把结果放在 Queue 里

定义一个被多线程调用的函数，q 就像一个队列，用来保存每次函数运行的结果
```python
#该函数没有返回值！！！
def job(q):
    res=0
    for i in range(1000):
        res+=i+i**2+i**3
    q.put(res)    #queue
```
主函数
定义一个多线程队列，用来存储结果
```python
if __name__=='__main__':
    q = mp.Queue()
```
定义两个线程函数，用来处理同一个任务, args 的参数只要一个值的时候，参数后面需要加一个逗号，表示args是可迭代的，后面可能还有别的参数，不加逗号会出错
```
p1 = mp.Process(target=job,args=(q,))
p2 = mp.Process(target=job,args=(q,))
```
分别启动、连接两个线程
```python
p1.start()
p2.start()
p1.join()
p2.join()
```
上面是分两批处理的，所以这里分两批输出，将结果分别保存
```python
res1 = q.get()
res2 = q.get()
打印最后的运算结果
```python
print(res1+res2)
```
完整的代码
```python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 20:04:45 2019

@author: zangz
"""

import multiprocessing as mp  #导包

def job(q):  #多进程没有返回值,压到队列中
    res=0  #初始值
    for i in range(1000):
        res+=i+i**2+i**3
    q.put(res)    #queue,就运算的结果压到队列中

if __name__=='__main__':
    q = mp.Queue()  #创建一个队列
    p1 = mp.Process(target=job,args=(q,)) #target是目标函数,args是函数中传入的参数
#    args 的参数只要一个值的时候，参数后面需要加一个逗号，表示args是可迭代的，后面可能还有别的参数，不加逗号会出错
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get() #队列的先进先出
    res2 = q.get()  
    print(res1+res2)
```
运行的时候还是要在terminal中，最后运行结果为:
```python
499667166000
```

### 效率对比 threading & multiprocessing
上篇讲了多进程/多核的运算，这次我们来对比下多进程，多线程和什么都不做时的消耗时间，看看哪种方式更有效率。
创建多进程 multiprocessing
和上节一样，首先import multiprocessing并定义要实现的job()，同时为了容易比较，我们将计算的次数增加到1000000
```python
import multiprocessing as mp

def job(q):
    res = 0
    for i in range(1000000):
        res += i + i**2 + i**3
    q.put(res) # queue
```
因为多进程是多核运算，所以我们将上节的多进程代码命名为multicore()
```python
def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:',res1 + res2)
```
创建多线程 multithread:
接下来创建多线程程序，创建多线程和多进程有很多相似的地方。首先import threading然后定义multithread()完成同样的任务
```python
import threading as td

def multithread():
    q = mp.Queue() # thread可放入process同样的queue中
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:', res1 + res2)
```
创建普通函数:
最后我们定义最普通的函数。注意，在上面例子中我们建立了两个进程或线程，均对job()进行了两次运算，所以在normal()中我们也让它循环两次:
```python
def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i + i**2 + i**3
    print('normal:', res)
```
运行时间
最后，为了对比各函数运行时间，我们需要import time， 然后依次运行定义好函数：
```python
import time

if __name__ == '__main__':
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time:', st1 - st)
    multithread()
    st2 = time.time()
    print('multithread time:', st2 - st1)
    multicore()
    print('multicore time:', time.time() - st2)
```
大功告成，下面我们来看下实际运行对比。
整个的程序:
```python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 20:15:11 2019

@author: zangz
"""

import multiprocessing as mp  #多进程导包
import threading as td   #多线程导包
    
import time

def job(q):   #目标函数功能
    res = 0
    for i in range(1000000):
        res += i + i**2 + i**3
    q.put(res) # queue

def multicore():  #多进程函数
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:',res1 + res2)
      
def multithread():   #多线程
    q = mp.Queue() # thread可放入process同样的queue中
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:', res1 + res2)
    
def normal():  #普通函数
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i + i**2 + i**3
    print('normal:', res)
    


if __name__ == '__main__':  #主函数
    st = time.time()
    normal()
    st1 = time.time()  
    print('normal time:', st1 - st) #计算的是执行普通函数的时间差
    multithread()
    st2 = time.time()  
    print('multithread time:', st2 - st1)  #计算的是多线程的时间差
    multicore()
    print('multicore time:', time.time() - st2)  #计算的是多进程的时间差
```
执行结果:
```python
normal: 499999666667166666000000
normal time: 1.8903188705444336
multithread: 499999666667166666000000
multithread time: 1.8123459815979004
multicore: 499999666667166666000000
multicore time: 1.237776756286621
```
> 多次运行的结果表示运算量低的时候使用正常的函数比较好,但是运算量较高的时候使用多进程明显快很多

比如我将任务量改为:range(10000000):
执行结果:
```python
normal: 4999999666666716666660000000
normal time: 18.560267686843872
multithread: 499999666667166666000000
multithread time: 1.814974308013916
multicore: 499999666667166666000000
multicore time: 1.2792866230010986
```
> 多进程和多线程的使用是需要明确使用场景的，多进程比较适合处理计算（CPU）密集型的任务（如上代码就是计算密集型），多线程适合处理I/O密集型的任务，它避免了多进程资源不断释放和申请（多线程共享多进程资源）。

### 进程池 Pool
这次我们讲进程池Pool。 进程池就是我们将所要运行的东西，放到池子里，Python会自行解决多进程的问题

首先import multiprocessing和定义job()
```python

import multiprocessing as mp

def job(x):
    return x*x
```
进程池 Pool() 和 map()
然后我们定义一个Pool
```python
pool = mp.Pool()
```
有了池子之后，就可以让池子对应某一个函数，我们向池子里丢数据，池子就会返回函数返回的值。 Pool和之前的Process的不同点是丢向Pool的函数有返回值，而Process的没有返回值。

接下来用map()获取结果，在map()中需要放入函数和需要迭代运算的值，然后它会自动分配给CPU核，返回结果
```python
res = pool.map(job, range(10))
```
让我们来运行一下
```python
def multicore():
    pool = mp.Pool()
    res = pool.map(job, range(10))
    print(res)
    
if __name__ == '__main__':
    multicore()
```
完整的程序:

```python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 20:40:20 2019

@author: zangz
"""

import multiprocessing as mp

def job(x): #定义目标的功能有返回值
    return x*x


def multicore():  #多线程的函数
    pool = mp.Pool()  #实例化(创建)一个池
    res = pool.map(job, range(10))  #使用map函数获得最终的返回值
    print(res)
    
if __name__ == '__main__':
    multicore()

```
运行结果:
```python
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
自定义核数量:
我们怎么知道Pool是否真的调用了多个核呢？我们可以把迭代次数增大些，然后打开CPU负载看下CPU运行情况

Pool默认大小是CPU的核数，我们也可以通过在Pool中传入processes参数即可自定义需要的核数量，
```python
def multicore():
    pool = mp.Pool(processes=3) # 定义CPU核数量为3
    res = pool.map(job, range(10))
    print(res)
```

**apply_async()**
Pool除了map()外，还有可以返回结果的方式，那就是apply_async().

apply_async()中只能传递一个值，它只会放入一个核进行运算，但是传入值时要注意是可迭代的，所以在传入值后需要加逗号, 同时需要用get()方法获取返回值
```python
def multicore():
    pool = mp.Pool() 
    res = pool.map(job, range(10))
    print(res)
   #使用apply_async函数,一次只能传入获取一个值
    res = pool.apply_async(job, (2,))
    # 用get获得结果
    print(res.get())
```
执行结果:
```python
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
4
```
**用 apply_async() 输出多个结果**
那么如何用apply_async()输出多个迭代呢？

我们在apply_async()中多传入几个值试试
```python
res = pool.apply_async(job, (2,3,4,))
```
结果会报错：
```python
TypeError: job() takes exactly 1 argument (3 given)
```
即apply_async()只能输入一组参数。
> 在此我们将apply_async() 放入迭代器中，定义一个新的multi_res
```python
multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
```
同样在取出值时需要一个一个取出来
```python
print([res.get() for res in multi_res])
```
合并代码
```python
def multicore():
    pool = mp.Pool() 
    res = pool.map(job, range(10))
    print(res)
    res = pool.apply_async(job, (2,))
    # 用get获得结果
    print(res.get())
    # 迭代器，i=0时apply一次，i=1时apply一次等等
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    # 从迭代器中取出(这里也得使用res.get,因为列表中存的都是地址,需要进行获取)
    print([res.get() for res in multi_res])
```
运行结果:
```python
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] # map()
4 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] # multi_res
```
可以看出在apply用迭代器的得到的结果和用map得到的结果是一样的
> 总结:
Pool默认调用是CPU的核数，传入processes参数可自定义CPU核数
map() 放入迭代参数，返回多个结果
apply_async()只能放入一组参数，并返回一个结果，如果想得到map()的效果需要通过迭代

### 共享内存 shared memory  
这节我们学习如何定义共享内存。只有用共享内存才能让CPU之间有交流。  多线程使用的是一个核因此使用全局变量就可以使用共享内存.但是多核进程时需要使用共享内存才可以.
Shared Value
我们可以通过使用Value数据存储在一个共享的内存表中
```python
import multiprocessing as mp

value1 = mp.Value('i', 0) 
value2 = mp.Value('d', 3.14)
```
其中d和i参数用来设置数据类型的，d表示一个双精浮点类型，i表示一个带符号的整型。更多的形式请查看本页最后的表
**Shared Array**
在Python的mutiprocessing中，有还有一个Array类，可以和共享内存交互，来实现在进程之间共享数据
```python
array = mp.Array('i', [1, 2, 3, 4])
```
这里的Array和numpy中的不同，它只能是一维的，不能是多维的。同样和Value 一样，需要定义数据形式，否则会报错。 我们会在后一节举例说明这两种的使用方法.
错误形式
```python
array = mp.Array('i', [[1, 2], [3, 4]]) # 2维list

"""
TypeError: an integer is required
"""
```
参考数据形式:
各参数代表的数据类型
```bash

| Type code | C Type             | Python Type       | Minimum size in bytes |
| --------- | ------------------ | ----------------- | --------------------- |
| `'b'`     | signed char        | int               | 1                     |
| `'B'`     | unsigned char      | int               | 1                     |
| `'u'`     | Py_UNICODE         | Unicode character | 2                     |
| `'h'`     | signed short       | int               | 2                     |
| `'H'`     | unsigned short     | int               | 2                     |
| `'i'`     | signed int         | int               | 2                     |
| `'I'`     | unsigned int       | int               | 2                     |
| `'l'`     | signed long        | int               | 4                     |
| `'L'`     | unsigned long      | int               | 4                     |
| `'q'`     | signed long long   | int               | 8                     |
| `'Q'`     | unsigned long long | int               | 8                     |
| `'f'`     | float              | float             | 4                     |
| `'d'`     | double             | float             | 8                     |
```
### 进程锁
进程锁 Lock
## 不加进程锁 

让我们看看没有加进程锁时会产生什么样的结果。

```python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 22:08:56 2019

@author: zangz
"""

import multiprocessing as mp  #导包
import time

def job(v, num):  #目标函数
    for _ in range(5):
        time.sleep(0.1) # 暂停0.1秒，让输出效果更明显
        v.value += num # v.value获取共享变量值(必须是这样的形式)
        print(v.value, end="\n")

def multicore():
    v = mp.Value('i', 0) # 定义共享变量(整数型,初始值为0)
    p1 = mp.Process(target=job, args=(v,1))
    p2 = mp.Process(target=job, args=(v,3)) # 设定不同的number看如何抢夺内存
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    multicore()


```

在上面的代码中，我们定义了一个共享变量`v`，两个进程都可以对它进行操作。 在`job()`中我们想让`v`每隔0.1秒输出一次累加`num`的结果，但是在两个进程`p1`和`p2` 中设定了不同的累加值。所以接下来让我们来看下这两个进程是否会出现冲突。

运行一下：使用的命令行才可以

```
1
4
5
8
9
12
13
16
17
20

```

我们可以看到，进程1和进程2在相互抢着使用共享内存`v`。

## 加进程锁 

为了解决上述不同进程抢共享资源的问题，我们可以用加进程锁来解决。

首先需要定义一个进程锁

```
    l = mp.Lock() # 定义一个进程锁

```

然后将进程锁的信息传入各个进程中

```
    p1 = mp.Process(target=job, args=(v,1,l)) # 需要将Lock传入
    p2 = mp.Process(target=job, args=(v,3,l)) 

```

在`job()`中设置进程锁的使用，保证运行时一个进程的对锁内内容的独占

```
def job(v, num, l):
    l.acquire() # 锁住
    for _ in range(5):
        time.sleep(0.1) 
        v.value += num # v.value获取共享内存
        print(v.value)
    l.release() # 释放

```

完整代码：

```
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 22:08:56 2019

@author: zangz
"""

import multiprocessing as mp  #导包
import time

def job(v, num, l):
    l.acquire() # 锁住
    for _ in range(5):
        time.sleep(0.1) 
        v.value += num # 获取共享内存
        print(v.value,'\n')
    l.release() # 释放

def multicore():
    l = mp.Lock() # 定义一个进程锁
    v = mp.Value('i', 0) # 定义共享内存
    p1 = mp.Process(target=job, args=(v,1,l)) # 需要将lock传入
    p2 = mp.Process(target=job, args=(v,3,l)) 
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    multicore()


```

运行一下，让我们看看是否还会出现抢占资源的情况：

```
1
2
3
4
5
8
11
14
17
20

```

显然，进程锁保证了进程`p1`的完整运行，然后才进行了进程`p2`的运行



