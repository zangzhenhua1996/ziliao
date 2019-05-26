## 什么是多线程 Threading
多线程是加速程序计算的有效方式，Python的多线程模块threading上手快速简单，从这节开始我们就教大家如何使用它。

## 添加线程

本节我们来学习threading模块的一些基本操作，如获取线程数，添加线程等。首先别忘了导入模块：

```python
import threading
```
获取已激活的线程数
```python
threading.active_count()
```
```
查看所有线程信息
```python
threading.enumerate()
```

输出的结果是一个`<_MainThread(...)>`带多个`<Thread(...)>`。

查看现在正在运行的线程

```python
threading.current_thread()
```
整个的上述程序:
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import threading

def main():
   print("当前的线程数: \n",threading.active_count()) #查看已经激活的线程数
   print("查看所有的线程信息: \n",threading.enumerate()) #查看所有线程信息
   print("当前线程:\n",threading.current_thread())  #查看当前线程

if __name__=='__main__':   #判断是不是在当前程序下执行,是就执行主方法
    main()
```
执行结果:
```python
当前的线程数: 
 5
查看所有的线程信息: 
 [<_MainThread(MainThread, started 14952)>, <Thread(Thread-4, started daemon 15264)>, <Heartbeat(Thread-5, started daemon 11884)>, <HistorySavingThread(IPythonHistorySavingThread, started 2320)>, <GarbageCollectorThread(Thread-6, started daemon 7112)>]
当前线程:
 <_MainThread(MainThread, started 14952)>
```

>添加线程，`threading.Thread()`接收参数`target`代表这个线程要完成的任务，需自行定义

```python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 20:46:17 2019

@author: zangz
"""
import threading
def thread_job(): #定义线程任务(功能就是打印当前的线程任务)
    print('This is a thread of %s' % threading.current_thread())

def main():
    print("创建一个线程任务")
    thread = threading.Thread(target=thread_job,)   # 定义线程 
    print('_'*100)
    thread.start()  # 让线程开始工作

if __name__ == '__main__':
    main()
```
> python多线程的执行:

不加 join() 的结果
我们让 T1 线程工作的耗时增加.
```python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 20:46:17 2019

@author: zangz
"""
import threading
import time
def thread_job(): #定义线程任务
    print("T1 start\n") #打印我开始做了
    for i in range(10):
        time.sleep(0.1)#休息0.1秒
    print("T1 stop\n")#打印我做完了
def main():
    print("创建一个线程任务")
    added_thread = threading.Thread(target=thread_job,name='T1')   # 定义线程 name是线程定义的名字
    print('_'*100)
    added_thread.start()  # 让线程开始工作
    #如果是单线程会顺序执行完上面的函数,多线程的情况下是什么样子的呢?
    print("alldone\n")
if __name__ == '__main__':
    main()
```
预想中输出的结果是否为：
```python
T1 start
T1 finish
all done
```
但实际却是：
```python
创建一个线程任务
____________________________________________________________________________________________________
T1 start
alldone


T1 stop
```
也就是说执行了多线程(同时在进行的线程任务),没有进行顺序的执行

> 加入 join() 的结果(想要所有的线程执行完了再打印alldone)

线程任务还未完成便输出all done。如果要遵循顺序，可以在启动线程后对它调用join：
```python
added_thread.start()
added_thread.join()
print("all done\n")
```
总的程序:
```python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 20:46:17 2019

@author: zangz
"""
import threading
import time
def thread_job(): #定义线程任务
    print("T1 start\n") #打印我开始做了
    for i in range(10):
        time.sleep(0.1)#休息0.1秒
    print("T1 stop\n")#打印我做完了
def main():
    print("创建一个线程任务")
    added_thread = threading.Thread(target=thread_job,name='T1')   # 定义线程 name是线程定义的名字
    print('_'*100)
    
    added_thread.start()  # 让线程开始工作
    added_thread.join()   #让线程执行完在执行下面的语句
    
    print("alldone\n")
if __name__ == '__main__':
    main()
```
执行结果:
```python
创建一个线程任务
____________________________________________________________________________________________________
T1 start

T1 stop

alldone
```

使用join对控制多个线程的执行顺序非常关键。举个例子，假设我们现在再加一个线程T2，T2的任务量较小，会比T1更快完成：
输出的**”一种”**结果是：
例:
```python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:07:21 2019

@author: zangz
"""
import threading

def T1_job():  #执行的速度慢
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")

def T2_job():  #执行的速度快
    print("T2 start\n")
    print("T2 finish\n")

thread_1 = threading.Thread(target=T1_job, name='T1')  #创建线程1
thread_2 = threading.Thread(target=T2_job, name='T2')  #创建线程2
thread_1.start() # 开启T1
thread_2.start() # 开启T2
print("all done\n")
```
执行结果:
```python
T1 start
T2 start


T2 finish

all done

T1 finish
```
现在T1和T2都没有join，注意这里说**”一种”**是因为all done的出现完全取决于两个线程的执行速度， 完全有可能T2 finish出现在all done之后。这种杂乱的执行方式是我们不能忍受的，因此要使用join加以控制。

我们试试在T1启动后，T2启动前加上`thread_1.join()`:
```python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:07:21 2019

@author: zangz
"""
import threading

def T1_job():  #执行的速度慢
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")

def T2_job():  #执行的速度快
    print("T2 start\n")
    print("T2 finish\n")

thread_1 = threading.Thread(target=T1_job, name='T1')  #创建线程1
thread_2 = threading.Thread(target=T2_job, name='T2')  #创建线程2
thread_1.start() # 开启T1
thread_1.join() #等线程T1执行完再执行别的线程
thread_2.start() # 开启T2(由于T1在T2任务开启之前就加了join因此T2需要等待T1线程执行完才能开启)
print("all done\n")
```
执行结果:
```python
T1 start

T1 finish

T2 start
all done

T2 finish
```
可以看到，T2会等待T1结束后才开始运行。这是由于T1在T2任务开启之前就加了join因此T2需要等待T1线程执行完才能开启

如果我们在T2启动后放上thread_1.join()会怎么样呢？
```python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:07:21 2019

@author: zangz
"""
import threading

def T1_job():  #执行的速度慢
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")

def T2_job():  #执行的速度快
    print("T2 start\n")
    print("T2 finish\n")

thread_1 = threading.Thread(target=T1_job, name='T1')  #创建线程1
thread_2 = threading.Thread(target=T2_job, name='T2')  #创建线程2
thread_1.start() # 开启T1

thread_2.start() # 开启T2
thread_1.join() #等线程T1执行完再执行别的线程

print("all done\n")
```
执行结果:
```python
T1 start
T2 start

T2 finish


T1 finish

all done
```
结果分析: T2在T1之后启动，并且因为T2任务量小会在T1之前完成；而T1也因为加了join，所以在T1线程执行完毕all done才能继续执行

你也可以添加thread_2.join()进行尝试，但为了规避不必要的麻烦，推荐如下这种1221的V型排布(前提是不需要结果的顺序排列(T1输出的结果先存,T2的输出结果后存))
```python
thread_1.start() # start T1
thread_2.start() # start T2
thread_2.join() # join for T2
thread_1.join() # join for T1
print("all done\n")

"""
T1 start
T2 start
T2 finish
T1 finish
all done
"""
```
完整的程序代码:
```python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:07:21 2019

@author: zangz
"""
import threading

def T1_job():  #执行的速度慢
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")

def T2_job():  #执行的速度快
    print("T2 start\n")
    print("T2 finish\n")

thread_1 = threading.Thread(target=T1_job, name='T1')  #创建线程1
thread_2 = threading.Thread(target=T2_job, name='T2')  #创建线程2
thread_1.start() # 开启T1
thread_2.start() # 开启T2
thread_2.join() #等线程T2执行完再执行别的线程
thread_1.join() #等线程T1执行完再执行别的线程
print("all done\n")
```
执行结果:
```python
T1 start
T2 start


T2 finish

T1 finish

all done
```
>  这种执行方式可以让线程短的先执行完,为什么会这样呢?首先两个线程是都开启了,然后两个都加了join,因此会等两个线程结束后才会执行alldone,又由于两个线程都开启了所以执行快的先结束,不会因为谁先添加join谁就先执行完.比如下面的1212方式是同样的执行结果


采用1212的方式会如何?
```python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:07:21 2019

@author: zangz
"""
import threading

def T1_job():  #执行的速度慢
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")

def T2_job():  #执行的速度快
    print("T2 start\n")
    print("T2 finish\n")

thread_1 = threading.Thread(target=T1_job, name='T1')  #创建线程1
thread_2 = threading.Thread(target=T2_job, name='T2')  #创建线程2
thread_1.start() # 开启T1
thread_2.start() # 开启T2
thread_1.join() #等线程T1执行完再执行alldone
thread_2.join() #等线程T2执行完再执行alldone

print("all done\n")
```
执行结果:
```python
T1 start
T2 start


T2 finish

T1 finish

all done
```
可以看到使用1212方式执行线程时,还是线程执行快的先结束,不会因为join的前后顺序导致结果的改变,因此如果需要线程1先结束就要采取下面的1122方式(但是这样就失去了线程意义,不过在使用queue的时候还是要注意队列的先进先出的使用顺序的)

测试一下另一种1122的方式是这样的:
```python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:07:21 2019

@author: zangz
"""
import threading

def T1_job():  #执行的速度慢
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")

def T2_job():  #执行的速度快
    print("T2 start\n")
    print("T2 finish\n")

thread_1 = threading.Thread(target=T1_job, name='T1')  #创建线程1
thread_2 = threading.Thread(target=T2_job, name='T2')  #创建线程2
thread_1.start() # 开启T1
thread_1.join() #等线程T1执行完再执行别的线程
thread_2.start() # 开启T2
thread_2.join() #等线程T2执行完再执行别的线程

print("all done\n")
```
执行结果:
```python
T1 start

T1 finish

T2 start

T2 finish

all done
```
> 这种的就是完全按照顺序来执行线程

### 储存进程结果 Queue

代码实现功能，将数据列表中的数据传入，使用四个线程处理，将结果保存在Queue中，线程执行完后，从Queue中获取存储的结果

导入线程,队列的标准模块
```python
import threading
import time
from queue import Queue
```
定义一个被多线程调用的函数

函数的参数是一个列表l和一个队列q，函数的功能是，对列表的每个元素进行平方计算，将结果保存在队列中
```python
def job(l,q):
    for i in range (len(l)):
        l[i] = l[i]**2
    q.put(l)   #多线程调用的函数不能用return返回值
```
定义一个多线程函数

在多线程函数中定义一个Queue，用来保存返回值，代替return，定义一个多线程列表，初始化一个多维数据列表，用来处理：
```python
def multithreading():
    q =Queue()    #q中存放返回值，代替return的返回值
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
```
在多线程函数中定义四个线程，启动线程，将每个线程添加到多线程的列表中
```python
for i in range(4):   #定义四个线程
    t = threading.Thread(target=job,args=(data[i],q)) #Thread首字母要大写，被调用的job函数没有括号，只是一个索引，参数在后面
    t.start()#开始线程
    threads.append(t) #把每个线程append到线程列表中

```
分别join四个线程到主线程
```python
for thread in threads:
    thread.join()
```
定义一个空的列表results，将四个线运行后保存在队列中的结果返回给空列表results
```python
results = []
for _ in range(4):
    results.append(q.get())  #q.get()按顺序从q中拿出一个值
print(results)
```
完整的代码
```python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:21:09 2019

@author: zangz
"""
import threading
import time

from queue import Queue  #队列

#定义了一个函数:l是一个列表,对列表中的每一个元素进行平方的运算
def job(l,q):
    for i in range (len(l)):
        l[i] = l[i]**2
    q.put(l)  #线程中不能返回一个值

def multithreading():
    q =Queue()  #先定义一个q队列(放入我们计算出的返回值)
    threads = []   #把所有的线程放大这个列表中
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]  #四个数据列表
    for i in range(4):  #循环定义四个线程
        t = threading.Thread(target=job,args=(data[i],q)) #target是功能的名字,args是传入的参数
        t.start()  #开启线程
        threads.append(t) #将线程加到全部的线程中
    for thread in threads:
        thread.join()  #将join功能加到线程中,使得所有的线程运行完以后才返回结果值(同时这样不会出现混乱,依次线程执行)
#   循环得到四个线程中的值
    results = []
    for _ in range(4):
        results.append(q.get()) #从q中取值;传了四次拿四次.队列先进先出
    print(results)

if __name__=='__main__':
    multithreading()
```
最后运行结果为:
```python
[[1, 4, 9], [9, 16, 25], [16, 16, 16], [25, 25, 25]]
```
>  需要注意的是在这里采用的是全部开启服务再加join的方式,如果某个列表的执行速度慢了,就会导致存进队列的时候顺序不一致,导致结果的错乱.

## GIL 不一定有效率
这次我们来看看为什么说 python 的多线程 threading 有时候并不是特别理想. 最主要的原因是就是, Python 的设计上, 有一个必要的环节, 就是 Global Interpreter Lock (GIL). 这个东西让 Python 还是一次性只能处理一个东西.

我从[这里](http://python3-cookbook.readthedocs.io/zh_CN/latest/c12/p09_dealing_with_gil_stop_worring_about_it.html)摘抄了一段对于 GIL 的解释.

> 尽管Python完全支持多线程编程， 但是解释器的C语言实现部分在完全并行执行时并不是线程安全的。 实际上，解释器被一个全局解释器锁保护着，它确保任何时候都只有一个Python线程执行。 GIL最大的问题就是Python的多线程程序并不能利用多核CPU的优势 （比如一个使用了多个线程的计算密集型程序只会在一个单CPU上面运行）。

> 在讨论普通的GIL之前，有一点要强调的是GIL只会影响到那些严重依赖CPU的程序（比如计算型的）。 如果你的程序大部分只会涉及到I/O，比如网络交互，那么使用多线程就很合适， 因为它们大部分时间都在等待。实际上，你完全可以放心的创建几千个Python线程， 现代操作系统运行这么多线程没有任何压力，没啥可担心的。
### 测试 GIL
我们创建一个 job, 分别用 threading 和 一般的方式执行这段程序. 并且创建一个 list 来存放我们要处理的数据. 在 Normal 的时候, 我们这个 list 扩展4倍, 在 threading 的时候, 我们建立4个线程, 并对运行时间进行对比.
```python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:47:13 2019

@author: zangz
"""

import threading  #导入线程包
from queue import Queue   #队列
import copy  #拷贝包
import time

def job(l, q):
    res = sum(l)  #对列表中的内容进行求和
    q.put(res)   #进队列

def multithreading(l):
    q = Queue()  #实例化一个队列
    threads = [] #存放线程 
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0  #初始一个值
    for _ in range(4):
        total += q.get() #取出所有的结果
    print(total)  #打印结果

def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(1000000)) 
    s_t = time.time() #获取当前时间
    normal(l*4)
    print('normal: ',time.time()-s_t)  #得到执行时间
    s_t = time.time()
    multithreading(l)
    print('multithreading: ', time.time()-s_t)
```
如果你成功运行整套程序, 你大概会有这样的输出. 我们的运算结果没错, 所以程序 threading 和 Normal 运行了一样多次的运算. 但是我们发现 threading 却没有快多少, 按理来说, 我们预期会要快3-4倍, 因为有建立4个线程, 但是并没有. 这就是其中的 GIL 在作怪.
执行结果:
```python
1999998000000
normal:  0.17794227600097656
1999998000000
multithreading:  0.16945099830627441
```
执行的甘特图:
![同时只有一个线程运算](https://upload-images.jianshu.io/upload_images/14555448-2a9201e082cee2e5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> 线程执行到输出的时候就会交给另一个线程进行运算

## 线程锁 lock 
如果第一个线程处理完的初步的结果拿给第二个线程用的时候需要使用线程锁.锁住第一个线程等它处理完再开始第二个线程.

导入线程标准模块
```python
import threading
```
不使用 Lock 的情况:
函数一：全局变量A的值每次加1，循环10次，并打印
```python
def job1():
    global A
    for i in range(10):
        A+=1
        print('job1',A)
```
函数二：全局变量A的值每次加10，循环10次，并打印
```python
def job2():
    global A
    for i in range(10):
        A+=10
        print('job2',A)
```
主函数：定义两个线程，分别执行函数一和函数二

```python
if __name__== '__main__':
    A=0
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
```
完整代码：
```python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 11:52:24 2019

@author: zangz
"""

import threading

def job1():
    global A
    for i in range(10):
        A+=1
        print('job1',A)

def job2():
    global A
    for i in range(10):
        A+=10
        print('job2',A)

if __name__== '__main__':
    lock=threading.Lock()
    A=0
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
```
执行结果:
```python
job1job2  11
job2 21
job2 31
job2 41
job2 51
job2 61
job2 71
job2 81
job2 91
job2 101
1
job1 102
job1 103
job1 104
job1 105
job1 106
job1 107
job1 108
job1 109
job1 110
```
可以看出，打印的结果非常混乱
使用 Lock 的情况:
lock在不同线程使用同一共享内存时，能够确保线程之间互不影响，使用lock的方法是， 在每个线程执行运算修改共享内存之前，执行lock.acquire()将共享内存上锁， 确保当前线程执行时，内存不会被其他线程访问，执行运算完毕后，使用lock.release()将锁打开， 保证其他的线程可以使用该共享内存。

函数一和函数二加锁
```python
def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=1
        print('job1',A)
    lock.release()

def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=10
        print('job2',A)
    lock.release()
```
主函数中定义一个Lock
```python
if __name__== '__main__':
    lock=threading.Lock()
    A=0
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
```
完整的代码
```python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 11:52:24 2019

@author: zangz
"""

import threading

def job1():
    global A,lock  #使用全局变量
    lock.acquire()   #获得锁
    for i in range(10):
        A+=1
        print('job1',A)
    lock.release()  #释放锁  ,别的进程可以开始执行了

def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=10
        print('job2',A)
    lock.release()

if __name__== '__main__':
    lock=threading.Lock()
    A=0  #全局变量
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
```
运行结果
```python
job1 1
job1 2
job1 3
job1 4
job1 5
job1 6
job1 7
job1 8
job1 9
job1 10
job2 20
job2 30
job2 40
job2 50
job2 60
job2 70
job2 80
job2 90
job2 100
job2 110
```
从打印结果来看，使用lock后，一个一个线程执行完。使用lock和不使用lock，最后打印输出的结果是不同的。
