# 6. 多任务-进程

## 6.1. 进程以及状态

## 进程以及状态

### 1. 进程

程序：例如xxx.py这是程序，是一个静态的

进程：一个程序运行起来后，代码+用到的资源 称之为进程，它是操作系统分配资源的基本单元。

不仅可以通过线程完成多任务，进程也是可以的

### 2. 进程的状态

工作中，任务数往往大于cpu的核数，即一定有一些任务正在执行，而另外一些任务在等待cpu进行执行，因此导致了有了不同的状态

![image.png](https://upload-images.jianshu.io/upload_images/14555448-69f0dd2aaab5017a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 就绪态：运行的条件都已经满足，正在等在cpu执行
- 执行态：cpu正在执行其功能
- 等待态：等待某些条件满足，例如一个程序sleep了，此时就处于等待态

## 6.2. 进程的创建-multiprocessing

## 进程的创建-multiprocessing

multiprocessing模块就是跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象，这个对象可以理解为是一个独立的进程，可以执行另外的事情

### 1. 2个while循环一起执行

```python
# -*- coding:utf-8 -*-
from multiprocessing import Process #使用的是多进程的Process类
import time


def run_proc():
    """子进程要执行的代码"""
    while True:
        print("----2----")
        time.sleep(1)


if __name__=='__main__':
    p = Process(target=run_proc) #创建一个进程
    p.start() #开启进程
    while True:
        print("----1----")
        time.sleep(1)
```

#### 说明

- 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动

#### 多进程



```python
import threading
import time
import multiprocessing


def test1():
    while True:
        print("1--------")
        time.sleep(1)


def test2():
    while True:
        print("2--------")
        time.sleep(1)


def main():
 #    t1 = threading.Thread(target=test1)
 #    t2 = threading.Thread(target=test2)
 #    t1.start()
 #    t2.start()

    p1 = multiprocessing.Process(target=test1)  #threading.Thread() #跟进程的区分一下
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    p2.start()

if __name__ == "__main__":
    main()
```

![image.png](https://upload-images.jianshu.io/upload_images/14555448-a1a0557e94cccb6b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

进程开的越多,资源占用的越多,进程越来越多,效率会降低.一开始是快的不过是占用内存.但是进程越来越多的时候就挤不开了.

子进程是要复制一份主进程的资源,但是代码是共享的,因此会又占用一部分内存这也是耗费资源多的一个原因.

![image.png](https://upload-images.jianshu.io/upload_images/14555448-8074e0cd858b8278.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 2. 进程pid

```python
# -*- coding:utf-8 -*-
from multiprocessing import Process
import os #系统的操作
import time

def run_proc():
    """子进程要执行的代码"""
    print('子进程运行中，pid=%d...' % os.getpid())  # os.getpid获取当前进程的进程号
    print('子进程将要结束...')

if __name__ == '__main__':
    print('父进程pid: %d' % os.getpid())  # os.getpid获取当前进程的进程号
    p = Process(target=run_proc)
    p.start()
```

### 3. Process语法结构如下：

Process([group [, target [, name [, args [, kwargs]]]]])

- target：如果传递了函数的引用，可以任务这个子进程就执行这里的代码
- args：给target指定的函数传递的参数，以元组的方式传递
- kwargs：给target指定的函数传递命名参数
- name：给进程设定一个名字，可以不设定
- group：指定进程组，大多数情况下用不到

Process创建的实例对象的常用方法：

- start()：启动子进程实例（创建子进程）
- is_alive()：判断进程子进程是否还在活着
- join([timeout])：是否等待子进程执行结束，或等待多少秒
- terminate()：不管任务是否完成，立即终止子进程

Process创建的实例对象的常用属性：

- name：当前进程的别名，默认为Process-N，N为从1开始递增的整数
- pid：当前进程的pid（进程号）

### 4. 给子进程指定的函数传递参数

```python
# -*- coding:utf-8 -*-
from multiprocessing import Process
import os
from time import sleep


def run_proc(name, age, **kwargs):
    for i in range(10):
        print('子进程运行中，name= %s,age=%d ,pid=%d...' % (name, age, os.getpid()))
        print(kwargs)
        sleep(0.2)

if __name__=='__main__':
    p = Process(target=run_proc, args=('test',18), kwargs={"m":20})
    p.start()
    sleep(1)  # 1秒中之后，立即结束子进程
    p.terminate()
    p.join()
```

运行结果:

```python
子进程运行中，name= test,age=18 ,pid=45097...
{'m': 20}
子进程运行中，name= test,age=18 ,pid=45097...
{'m': 20}
子进程运行中，name= test,age=18 ,pid=45097...
{'m': 20}
子进程运行中，name= test,age=18 ,pid=45097...
{'m': 20}
子进程运行中，name= test,age=18 ,pid=45097...
{'m': 20}
```

### 5. 进程间不同享全局变量(子进程都会拷贝主进程的一份资源,因此输出的使用nums都是单独的资源)

```python
# -*- coding:utf-8 -*-
from multiprocessing import Process
import os
import time

nums = [11, 22]

def work1():
    """子进程要执行的代码"""
    print("in process1 pid=%d ,nums=%s" % (os.getpid(), nums))
    for i in range(3):
        nums.append(i)
        time.sleep(1)
        print("in process1 pid=%d ,nums=%s" % (os.getpid(), nums))

def work2():
    """子进程要执行的代码"""
    print("in process2 pid=%d ,nums=%s" % (os.getpid(), nums))

if __name__ == '__main__':
    p1 = Process(target=work1)
    p1.start()
    p1.join()

    p2 = Process(target=work2)
    p2.start()
```

#### 运行结果:

```python
in process1 pid=11349 ,nums=[11, 22]
in process1 pid=11349 ,nums=[11, 22, 0]
in process1 pid=11349 ,nums=[11, 22, 0, 1]
in process1 pid=11349 ,nums=[11, 22, 0, 1, 2]
in process2 pid=11350 ,nums=[11, 22]
```

## 6.3. 进程、线程对比

## 进程、线程对比

### 功能

- 进程(一坨资源及代码的总称)，能够完成多任务，比如 在一台电脑上能够同时运行多个QQ
- 线程，能够完成多任务，比如 一个QQ中的多个聊天窗口

![image.png](https://upload-images.jianshu.io/upload_images/14555448-a17648a507f0a300.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 定义的不同

- 进程是系统进行资源分配和调度的一个独立单位.
- 线程是进程的一个实体,是CPU调度和分派的基本单位,它是比进程更小的能独立运行的基本单位.线程自己基本上不拥有系统资源,只拥有一点在运行中必不可少的资源(如程序计数器,一组寄存器和栈),**但是它可与同属一个进程的其他的线程共享进程所拥有的全部资源.**

### 区别

- 一个程序至少有一个进程,一个进程至少有一个线程.
- 线程的划分尺度小于进程(资源比进程少)，使得多线程程序的并发性高。
- 进程在执行过程中拥有独立的内存单元，而多个线程共享内存，从而极大地提高了程序的运行效率
- ![image.png](https://upload-images.jianshu.io/upload_images/14555448-db05340a5c6a571d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 线线程不能够独立执行，必须依存在进程中
- 可以将进程理解为工厂中的一条流水线，而其中的线程就是这个流水线上的工人

![image.png](https://upload-images.jianshu.io/upload_images/14555448-78012dcb43c8e11d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 优缺点

线程和进程在使用上各有优缺点：线程执行开销小，但不利于资源的管理和保护；而进程正相反。

## 6.4. 进程间通信-Queue

## 进程间通信-Queue

Process之间有时需要通信，操作系统提供了很多机制来实现进程间的通信。

### 1\. Queue的使用

可以使用multiprocessing模块的Queue实现多进程之间的数据传递，Queue本身是一个消息列队程序，首先用一个小实例来演示一下Queue的工作原理：

```python

#coding=utf-8
from multiprocessing import Queue
q=Queue(3) #初始化一个Queue对象，最多可接收三条put消息
q.put("消息1") 
q.put("消息2")
print(q.full())  #False
q.put("消息3")
print(q.full()) #True

#因为消息列队已满下面的try都会抛出异常，第一个try会等待2秒后再抛出异常，第二个Try会立刻抛出异常
try:
    q.put("消息4",True,2) #等两秒再存消息
except:
    print("消息列队已满，现有消息数量:%s"%q.qsize())

try:
    q.put_nowait("消息4")  #不想等直接就要往里存消息
except:
    print("消息列队已满，现有消息数量:%s"%q.qsize())

#推荐的方式，先判断消息列队是否已满，再写入
if not q.full():
    q.put_nowait("消息4")

#读取消息时，先判断消息列队是否为空，再读取
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())

```

运行结果:

```python

False
True
消息列队已满，现有消息数量:3
消息列队已满，现有消息数量:3
消息1
消息2
消息3

```

##### 说明

初始化Queue()对象时（例如：q=Queue()），若括号中没有指定最大可接收的消息数量，或数量为负值，那么就代表可接受的消息数量没有上限（直到内存的尽头）；

*   Queue.qsize()：返回当前队列包含的消息数量；

*   Queue.empty()：如果队列为空，返回True，反之False ；

*   Queue.full()：如果队列满了，返回True,反之False；

*   Queue.get([block[, timeout]])：获取队列中的一条消息，然后将其从列队中移除，block默认值为True；

1）如果block使用默认值，且没有设置timeout（单位秒），消息列队如果为空，此时程序将被阻塞（停在读取状态），直到从消息列队读到消息为止，如果设置了timeout，则会等待timeout秒，若还没读取到任何消息，则抛出"Queue.Empty"异常；

2）如果block值为False，消息列队如果为空，则会立刻抛出"Queue.Empty"异常；

*   Queue.get_nowait()：相当Queue.get(False)；

*   Queue.put(item,[block[, timeout]])：将item消息写入队列，block默认值为True；

1）如果block使用默认值，且没有设置timeout（单位秒），消息列队如果已经没有空间可写入，此时程序将被阻塞（停在写入状态），直到从消息列队腾出空间为止，如果设置了timeout，则会等待timeout秒，若还没空间，则抛出"Queue.Full"异常；

2）如果block值为False，消息列队如果没有空间可写入，则会立刻抛出"Queue.Full"异常；

*   Queue.put_nowait(item)：相当Queue.put(item, False)；

### 2\. Queue实例

我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：

简单的做法

```python

import multiprocessing

"""
一个进程向Queue中写入数据，另外一个进程从Queue中获取数据，
通过Queue完成了 多个需要配合的进程间的数据共享，从而能够 起到 解耦的作用
"""
def download_from_web(q):
    """下载数据"""
    # 模拟从网上下载的数据
    data = [11, 22, 33, 44]

    # 向队列中写入数据（只管往里放）
    for temp in data:
        q.put(temp)

    print("---下载器已经下载完了数据并且存入到队列中----")


def analysis_data(q):
    """数据处理"""
    waitting_analysis_data = list()
    # 从队列中获取数据
    while True:
        data = q.get()  #取数据
        waitting_analysis_data.append(data) #存储数据

        if q.empty():#队列空了就结束循环
            break

    # 模拟数据处理
    print(waitting_analysis_data)

def main():
    # 1. 创建一个队列
    q = multiprocessing.Queue()   #在创建子进程之前就把队列先创建好

    # 2. 创建多个进程，将队列的引用当做实参进行传递到里面
    p1 = multiprocessing.Process(target=download_from_web, args=(q,)) #args=（q，）#表示是一个元祖，超过两个参数后面就不用再加多余的一个逗号
    p2 = multiprocessing.Process(target=analysis_data, args=(q,)) #传递的都是同一个队列的引用，先进先出
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()


```

更系统的做法

```python
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue.' % value)
            time.sleep(random.random())
        else:
            break

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()    
    # 等待pw结束:
    pw.join()
    # 启动子进程pr，读取:
    pr.start()
    pr.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    print('')
    print('所有数据都写入并且读完')

```

运行结果：

![13123123123123126.gif](https://upload-images.jianshu.io/upload_images/14555448-90f8caa6718feace.gif?imageMogr2/auto-orient/strip)

## 6.5. 进程的创建-进程池Pool

## 进程池Pool

当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态成生多个进程，但如果是上百甚至上千个目标，手动的去创建进程的工作量巨大，此时就可以用到multiprocessing模块提供的Pool方法。

初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到指定的最大值，那么该请求就会等待，直到池中有进程结束，才会用之前的进程来执行新的任务，请看下面的实例：

```python
# -*- coding:utf-8 -*-
from multiprocessing import Pool #导入进程池
import os, time, random

def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d" % (msg,os.getpid()))
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random()*2) 
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f" % (t_stop-t_start))

po = Pool(3)  # 定义一个进程池，最大进程数3
for i in range(0,10):  #会把所有的进程任务全部添加,但是执行的只有Pool最大的数量,会慢慢的把添加的任务分配到进程池里进行执行
    # Pool().apply_async(要调用的目标,(传递给目标的参数元祖,))
    # 每次循环将会用空闲出来的子进程去调用目标
    po.apply_async(worker,(i,)) #worker 函数名,(i,) 参数
#使用pool创建的任务,主进程不会等待子进程的任务执行完,会继续往下执行,因此需要一个join函数进行堵塞,等待子进程的执行完毕
print("----start----")
po.close()  # 关闭进程池，关闭后po不再接收新的请求,会继续向下执行,需要对主进程进行堵塞
po.join()  # 等待po中所有子进程执行完成，必须放在close语句之后
print("-----end-----")
```

![图片.png](https://upload-images.jianshu.io/upload_images/14555448-9d6390c19c8ee9b3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

运行结果:

```python
----start----
0开始执行,进程号为21466
1开始执行,进程号为21468
2开始执行,进程号为21467
0 执行完毕，耗时1.01
3开始执行,进程号为21466
2 执行完毕，耗时1.24
4开始执行,进程号为21467
3 执行完毕，耗时0.56
5开始执行,进程号为21466
1 执行完毕，耗时1.68
6开始执行,进程号为21468
4 执行完毕，耗时0.67
7开始执行,进程号为21467
5 执行完毕，耗时0.83
8开始执行,进程号为21466
6 执行完毕，耗时0.75
9开始执行,进程号为21468
7 执行完毕，耗时1.03
8 执行完毕，耗时1.05
9 执行完毕，耗时1.69
-----end-----
```

multiprocessing.Pool常用函数解析：

- apply_async(func[, args[, kwds]]) ：使用非阻塞方式调用func（并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程），args为传递给func的参数列表，kwds为传递给func的关键字参数列表；
- close()：关闭Pool，使其不再接受新的任务；
- terminate()：不管任务是否完成，立即终止；
- join()：主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用；

## 进程池中的Queue

如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()，而不是multiprocessing.Queue()，否则会得到一条如下的错误信息：

RuntimeError: Queue objects should only be shared between processes through inheritance.

下面的实例演示了进程池中的进程如何通信：

```python
# -*- coding:utf-8 -*-

# 修改import中的Queue为Manager
from multiprocessing import Manager,Pool
import os,time,random

def reader(q):
    print("reader启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s" % q.get(True))

def writer(q):
    print("writer启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in "itcast":
        q.put(i)

if __name__=="__main__":
    print("(%s) start" % os.getpid())
    q = Manager().Queue()  # 使用Manager中的Queue
    po = Pool()
    po.apply_async(writer, (q,))

    time.sleep(1)  # 先让上面的任务向Queue存入数据，然后再让下面的任务开始从中取数据

    po.apply_async(reader, (q,))
    po.close()
    po.join()
    print("(%s) End" % os.getpid())
```

运行结果:

```python
(11095) start
writer启动(11097),父进程为(11095)
reader启动(11098),父进程为(11095)
reader从Queue获取到消息：i
reader从Queue获取到消息：t
reader从Queue获取到消息：c
reader从Queue获取到消息：a
reader从Queue获取到消息：s
reader从Queue获取到消息：t
(11095) End
```

## 6.6. 案例：文件夹copy器（多进程版）

## 应用：文件夹copy器（多进程版）

初始版本

```python
import os
import multiprocessing


def copy_file(file_name, old_folder_name, new_folder_name):
    """完成文件的复制"""
    print("======>模拟copy文件：从%s--->到%s 文件名是:%s" % (old_folder_name, new_folder_name, file_name))
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()


def main():
    # 1. 获取用户要copy的文件夹的名字
    old_folder_name = input("请输入要copy的文件夹的名字：")

    # 2. 创建一个新的文件夹使用try的好处就是已经存在的话就不用二次创建导致报错了
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass

    # 3. 获取文件夹的所有的待copy的文件名字  listdir()
    file_names = os.listdir(old_folder_name)
    print(file_names)

    # 4. 创建进程池
    po = multiprocessing.Pool(5)

    # 5. 向进程池中添加 copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(file_name, old_folder_name, new_folder_name))

    po.close() #关闭进程池不再像进程池中存储任务
    po.join()


if __name__ == "__main__":
    main()


```
打印进度版本
```python
import os
import multiprocessing


def copy_file(q, file_name, old_folder_name, new_folder_name):
    """完成文件的复制"""
    # print("======>模拟copy文件：从%s--->到%s 文件名是:%s" % (old_folder_name, new_folder_name, file_name))
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()

    # 如果拷贝完了文件，那么就向队列中写入一个消息，表示已经完成
    q.put(file_name)


def main():
    # 1. 获取用户要copy的文件夹的名字
    old_folder_name = input("请输入要copy的文件夹的名字：")

    # 2. 创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass

    # 3. 获取文件夹的所有的待copy的文件名字  listdir()
    file_names = os.listdir(old_folder_name)
   # print(file_names)

    # 4. 创建进程池
    po = multiprocessing.Pool(5)

    # 5. 创建一个队列
    q = multiprocessing.Manager().Queue() #这里必须使用的是Manager的队列

    # 6. 向进程池中添加 copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))

    po.close()
    # po.join()
    all_file_num = len(file_names)  # 测一下所有的文件个数
    copy_ok_num = 0  #拷贝完的文件的个数进行初始化
    while True:
        file_name = q.get()  #往外取拷贝完了的文件名,获取到了就加一
        # print("已经完成copy：%s" % file_name)
        copy_ok_num+=1
        print("\r拷贝的进度为：%.2f %%" % (copy_ok_num*100/all_file_num), end="")
        if copy_ok_num >= all_file_num:#个数相等就说明拷贝完了就结束循环
            break


    print()

if __name__ == "__main__":
    main()

```

多进程拷贝文件,输入原始路径及需要拷贝到的路径



```python
import multiprocessing
import os
import time
import random


def copy_file(queue, file_name,source_folder_name,  dest_folder_name):
    """copy文件到指定的路径"""
    f_read = open(source_folder_name + "/" + file_name, "rb")
    f_write = open(dest_folder_name + "/" + file_name, "wb")
    while True:
        time.sleep(random.random())
        content = f_read.read(1024)
        if content:
            f_write.write(content)
        else:
            break
    f_read.close()
    f_write.close()

    # 发送已经拷贝完毕的文件名字
    queue.put(file_name)


def main():
    # 获取要复制的文件夹
    source_folder_name = input("请输入要复制文件夹名字:")

    # 整理目标文件夹
    dest_folder_name = source_folder_name + "[副本]"

    # 创建目标文件夹
    try:
        os.mkdir(dest_folder_name)
    except:
        pass  # 如果文件夹已经存在，那么创建会失败

    # 获取这个文件夹中所有的普通文件名
    file_names = os.listdir(source_folder_name)

    # 创建Queue
    queue = multiprocessing.Manager().Queue()

    # 创建进程池
    pool = multiprocessing.Pool(3)

    for file_name in file_names:
        # 向进程池中添加任务
        pool.apply_async(copy_file, args=(queue, file_name, source_folder_name, dest_folder_name))

    # 主进程显示进度
    pool.close()

    all_file_num = len(file_names)
    while True:
        file_name = queue.get()
        if file_name in file_names:
            file_names.remove(file_name)

        copy_rate = (all_file_num-len(file_names))*100/all_file_num
        print("\r%.2f...(%s)" % (copy_rate, file_name) + " "*50, end="")
        if copy_rate >= 100:
            break
    print()


if __name__ == "__main__":
    main()
```