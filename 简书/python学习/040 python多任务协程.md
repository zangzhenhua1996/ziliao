# 7.1迭代器
> 迭代是访问集合元素的一种方式。迭代器是一个可以记住遍历的位置的对象。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

## 1. 可迭代对象
我们已经知道可以对`list、tuple、str`等类型的数据使用`for...in...`的循环语法从其中依次拿到数据进行使用，我们把这样的过程称为遍历，也叫迭代。

但是，是否所有的数据类型都可以放到`for...in...`的语句中，然后让`for...in...`每次从中取出一条数据供我们使用，即供我们迭代吗？
```python

for i in 100:
    print(i)
    
Traceback (most recent call last):

  File "<ipython-input-3-86150fa0c47d>", line 1, in <module>
    for i in 100:

TypeError: 'int' object is not iterable
# int整型不是iterable，即int整型不是可以迭代的
```
```python
# 我们自定义一个容器MyList用来存放数据，可以通过add方法向其中添加数据
class MyList(object):
    def __init__(self):
        self.container = []
    def add(self, item):
        self.container.append(item)
        
mylist = MyList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
for num in mylist:
    print(num)
...

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'MyList' object is not iterable
>>>
# MyList容器的对象也是不能迭代的
但是调用这个对象的属性(我们存数据到的列表中是可以进行迭代的)

for num in mylist.container:
    print(num)

```

我们自定义了一个容器类型`MyList`，在将一个存放了多个数据的`MyList`对象放到`for...in...`的语句中，发现`for...in...`并不能从中依次取出一条数据返回给我们，也就说我们随便封装了一个可以存放多条数据的类型却并不能被迭代使用。

我们把可以通过`for...in...`这类语句迭代读取一条数据供我们使用的对象称之为可迭代对象**（Iterable)**。
## 2. 如何判断一个对象是否可以迭代
可以使用 isinstance() 判断一个对象是否是 Iterable 对象：
```python
In [50]: from collections import Iterable  #导入迭代类

In [51]: isinstance([], Iterable)
Out[51]: True  #列表是迭代对象

In [52]: isinstance({}, Iterable)
Out[52]: True #字典是迭代对象

In [53]: isinstance('abc', Iterable)
Out[53]: True  #字符串是迭代对象

In [54]: isinstance(mylist, Iterable)
Out[54]: False  #自己定义的对象不是可迭代对象(不一定)

In [55]: isinstance(100, Iterable)
Out[55]: False  #整形,浮点型不是可迭代的对象
```
## 3. 可迭代对象的本质
我们分析对可迭代对象进行迭代使用的过程，发现每迭代一次（即在`for...in...`中每循环一次）都会返回对象中的下一条数据，一直向后读取数据直到迭代了所有数据后结束。那么，在这个过程中就应该有一个`“人”`去记录每次访问到了第几条数据，以便每次迭代都可以返回下一条数据。我们把这个能帮助我们进行数据迭代的`“人”`称为迭代器**(Iterator)**。

可迭代对象的本质就是可以向我们提供一个这样的`中间“人”`即迭代器帮助我们对其进行迭代遍历使用。

可迭代对象通过`__iter__`方法向我们提供一个迭代器，我们在迭代一个可迭代对象的时候，实际上就是先获取该对象提供的一个迭代器，然后通过这个迭代器来依次获取对象中的每一个数据.

那么也就是说，一个具备了`__iter__`方法的对象，就是一个可迭代对象。
```python
class MyList(object):
    def __init__(self):
        self.container = []
    def add(self, item):
        self.container.append(item)
    def __iter__(self):
#返回一个迭代器
 # 我们暂时忽略如何构造一个迭代器对象
        pass
        
mylist = MyList()
mylist.add(1)
mylist.add(2)
mylist.add(3)

from collections import Iterable
isinstance(mylist, Iterable)

===============
Out[13]: True
# 这回测试发现添加了__iter__方法的mylist对象已经是一个可迭代对象了
```
## 4. iter()函数与next()函数
`list、tuple`等都是可迭代对象，我们可以通过`iter()`函数获取这些可迭代对象的迭代器。然后我们可以对获取到的迭代器不断使用`next()`函数来获取下一条数据。`iter()`函数实际上就是调用了可迭代对象的`__iter__`方法。
```python
li = [11, 22, 33]

li_iter = iter(li)

next(li_iter)
Out[16]: 11

next(li_iter)
Out[17]: 22

next(li_iter)
Out[18]: 33

next(li_iter)
=============
Traceback (most recent call last):

  File "<ipython-input-21-ab6a83f394a1>", line 1, in <module>
    next(li_iter)

StopIteration


```
> 注意，当我们已经迭代完最后一个数据之后，再次调用next()函数会抛出StopIteration的异常，来告诉我们所有数据都已迭代完成，不用再执行next()函数了。

## 5. 如何判断一个对象是否是迭代器(前面介绍的是如何判断一个对象是否可以迭代),这里是一个对象是否是迭代器,含义是不一样的,使用的判断函数也不一样
可以使用 isinstance() 判断一个对象是否是 Iterator 对象：
```python
In [56]: from collections import Iterator

In [57]: isinstance([], Iterator)
Out[57]: False

In [58]: isinstance(iter([]), Iterator)
Out[58]: True

In [59]: isinstance(iter("abc"), Iterator)
Out[59]: True
```

## 6. 迭代器Iterator
通过上面的分析，我们已经知道，迭代器是用来帮助我们记录每次迭代访问到的位置，当我们对迭代器使用`next()`函数的时候，迭代器会向我们返回它所记录位置的下一个位置的数据。实际上，在使用`next()`函数的时候，调用的就是迭代器对象的`__next__`方法（Python3中是对象的`__next__`方法，Python2中是对象的`next()`方法）。所以，我们要想构造一个迭代器，就要实现它的`__next__`方法。但这还不够，python要求迭代器本身也是可迭代的，所以我们还要为迭代器实现`__iter__`方法，而`__iter__`方法要返回一个迭代器，迭代器自身正是一个迭代器，所以迭代器的`__iter__`方法返回自身即可。

一个实现了`__iter__`方法和`__next__`方法的对象，就是迭代器。
![image.png](https://upload-images.jianshu.io/upload_images/14555448-4c0d58be651012c1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
#定义可迭代对象
class MyList(object):
    """自定义的一个可迭代对象"""
    def __init__(self):
        self.items = []

    def add(self, val):
        self.items.append(val)

    def __iter__(self):
        #在实例化的时候其实就把mylist(迭代对象的实例化)传递给了Myiterator
        myiterator = MyIterator(self) #使用下面的函数生成一个可迭代对象使用的迭代器(实例化一个迭代器)
        return myiterator   #返回这个使用的迭代器

#迭代器
class MyIterator(object):
    """自定义的供上面可迭代对象使用的一个迭代器"""
    def __init__(self, obj):  #这里的obj就是引用这个类的对象,比如说前面建立了一个mylist对象,然后在__iter__方法中返回的是这个迭代器对象,那么就会把这个mylist传递给这个obj
        self.mylist = obj  #这个其实就是个对象
        # current用来记录当前访问到的位置
        self.current = 0

    def __next__(self):
        if self.current < len(self.mylist.items):
            item = self.mylist.items[self.current]  #这个就是取这个对象中的列表的值
            self.current += 1
            return item  #每次使用next()返回一个值
        else:
            raise StopIteration  #产生一个异常告诉for循环该停止了

    def __iter__(self): #迭代器同样需要返回一个迭代器,返回自身即可
        return self  #返回自身


if __name__ == '__main__':
    mylist = MyList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(4)
    mylist.add(5)
    for num in mylist:
        print(num)
```
执行结果:
```python
1
2
3
4
5
```
## 7. for...in...循环的本质
`for item in Iterable` 循环的本质就是先通过`iter()`函数获取可迭代对象`Iterable`的迭代器，然后对获取到的迭代器不断调用`next()`方法来获取下一个值并将其赋值给`item`，当遇到`StopIteration`的异常后循环结束。
## 8. 迭代器的应用场景
我们发现迭代器最核心的功能就是可以通过`next()`函数的调用来返回下一个数据值。如果每次返回的数据值不是在一个已有的数据集合中读取的，而是通过程序按照一定的规律计算生成的，那么也就意味着可以不用再依赖一个已有的数据集合，也就是说不用再将所有要迭代的数据都一次性缓存下来供后续依次读取，这样可以节省大量的存储（内存）空间。
```python
range(100000)
Out[4]: range(0, 100000)
```
举个例子，比如，数学中有个著名的斐波拉契数列`（Fibonacci）`，数列中第一个数为0，第二个数为1，其后的每一个数都可由前两个数相加得到：

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

现在我们想要通过`for...in...`循环来遍历迭代斐波那契数列中的前`n`个数。那么这个斐波那契数列我们就可以用迭代器来实现，每次迭代都通过数学计算来生成下一个数。
```python
class FibIterator(object):
    """斐波那契数列迭代器"""
    def __init__(self, n):
        """
        :param n: int, 指明生成数列的前n个数
        """
        self.n = n
        # current用来保存当前生成到数列中的第几个数了
        self.current = 0
        # num1用来保存前前一个数，初始值为数列中的第一个数0
        self.num1 = 0
        # num2用来保存前一个数，初始值为数列中的第二个数1
        self.num2 = 1

    def __next__(self):
        """被next()函数调用来获取下一个数"""
        if self.current < self.n:
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1+self.num2
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__返回自身即可"""
        return self


if __name__ == '__main__':
    fib = FibIterator(10)
    for num in fib:
        print(num, end=" ")
```
## 9. 并不是只有for循环能接收可迭代对象
除了for循环能接收可迭代对象，list、tuple等也能接收。
```python
li = list(FibIterator(15))  #其实是挨个取值写入到了新的列表中,在元组跟列表进行类型的转换的时候也是同样的道理,并不是简单的类型转换.而是会相当于迭代器的取值赋值
print(li)
tp = tuple(FibIterator(6))
print(tp)
```


# 7.2生成器
## 1. 生成器
利用迭代器，我们可以在每次迭代获取数据（通过`next()`方法）时按照特定的规律进行生成。但是我们在实现一个迭代器时，关于当前迭代到的状态需要我们自己记录，进而才能根据当前状态生成下一个数据。为了达到记录当前状态，并配合`next()`函数进行迭代使用，我们可以采用更简便的语法，即生成器`(generator)`。生成器是一类特殊的迭代器。
## 2. 创建生成器方法1
要创建一个生成器，有很多种方法。第一种方法很简单，只要把一个列表生成式的 [ ] 改成 ( )
```python
In [15]: L = [ x*2 for x in range(5)]   #使用[]生成的是一个列表

In [16]: L
Out[16]: [0, 2, 4, 6, 8]

In [17]: G = ( x*2 for x in range(5))  #而使用()生成的就是一个生成器

In [18]: G
Out[18]: <generator object <genexpr> at 0x7f626c132db0>
```
创建 L 和 G 的区别仅在于最外层的 [ ] 和 ( ) ， L 是一个列表，而 G 是一个生成器。我们可以直接打印出列表L的每一个元素，而对于生成器G，我们可以按照迭代器的使用方法来使用，即可以通过next()函数、for循环、list()等方法使用。
```python
In [19]: next(G)
Out[19]: 0

In [20]: next(G)
Out[20]: 2

In [21]: next(G)
Out[21]: 4

In [22]: next(G)
Out[22]: 6

In [23]: next(G)
Out[23]: 8

In [24]: next(G)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-24-380e167d6934> in <module>()
----> 1 next(G)

StopIteration:

In [25]:
In [26]: G = ( x*2 for x in range(5))

In [27]: for x in G:
   ....:     print(x)
   ....:     
0
2
4
6
8

```
## 3. 创建生成器方法2
generator非常强大。如果推算的算法比较复杂，用类似列表生成式的 for 循环无法实现的时候，还可以用函数来实现。

我们仍然用上一节提到的斐波那契数列来举例，回想我们在上一节用迭代器的实现方式：
```python
class FibIterator(object):
    """斐波那契数列迭代器"""
    def __init__(self, n):
        """
        :param n: int, 指明生成数列的前n个数
        """
        self.n = n
        # current用来保存当前生成到数列中的第几个数了
        self.current = 0
        # num1用来保存前前一个数，初始值为数列中的第一个数0
        self.num1 = 0
        # num2用来保存前一个数，初始值为数列中的第二个数1
        self.num2 = 1

    def __next__(self):
        """被next()函数调用来获取下一个数"""
        if self.current < self.n:
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1+self.num2
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__返回自身即可"""
        return self
```
注意，在用迭代器实现的方式中，我们要借助几个变量(n、current、num1、num2)来保存迭代的状态。现在我们用生成器来实现一下。
不使用生成器函数:
```python
def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        print(num)
        num1, num2 = num2, num1+num2
        current += 1
#        yield num
#    return 'done'
```
执行:
```python
fib(10)
0
1
1
2
3
5
8
13
21
34
```
使用生成器:

```python
def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1, num2 = num2, num1+num2
        current += 1
        yield num  #如果一个函数有yield语句,那么这个就不在是函数,而是一个生成器模板
    return 'done'

#如果在调用fib时,发现这个函数有yield,那么此时不是调用一个函数,而是生成一个生成器对象
a=fib(10)
```
```python
In [31]: F = fib(5)

In [32]: next(F)
Out[32]: 1

In [33]: next(F)
Out[33]: 1

In [34]: next(F)
Out[34]: 2

In [35]: next(F)
Out[35]: 3

In [36]: next(F)
Out[36]: 5

In [37]: next(F)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-37-8c2b02b4361a> in <module>()
----> 1 next(F)

StopIteration: done
```
在使用生成器实现的方式中，我们将原本在迭代器`__next__`方法中实现的基本逻辑放到一个函数中来实现，但是将每次迭代返回数值的`return`换成了`yield`，此时新定义的函数便不再是函数，而是一个生成器了。简单来说：只要在`def`中有`yield`关键字的 就称为 生成器

此时按照调用函数的方式( 案例中为`F = fib(5)` )使用生成器就不再是执行函数体了，而是会返回一个生成器对象（ 案例中为`F `），然后就可以按照使用迭代器的方式来使用生成器了。
```python
In [38]: for n in fib(5):
   ....:     print(n)
   ....:     
1
1
2
3
5
```
但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获`StopIteration`错误，返回值包含在`StopIteration`的`value`中：
```python
In [39]: g = fib(5)

In [40]: while True:
   ....:     try:
   ....:         x = next(g)
   ....:         print("value:%d"%x)      
   ....:     except StopIteration as e:
   ....:         print("生成器返回值:%s"%e.value)
   ....:         break
   ....:     
value:1
value:1
value:2
value:3
value:5
生成器返回值:done
```
## 总结
* 使用了yield关键字的函数不再是函数，而是生成器。（使用了yield的函数就是生成器）
yield关键字有两点作用：
    * 保存当前运行状态（断点），然后暂停执行，即将生成器（函数）挂起
    * 将yield关键字后面表达式的值作为返回值返回，此时可以理解为起到了return的作用
* 可以使用next()函数让生成器从断点处继续执行，即唤醒生成器（函数）
* Python3中的生成器可以使用return返回最终运行的返回值，而Python2中的生成器不允许使用return返回一个返回值（即可以使用return从生成器中退出，但return后不能有任何表达式）。
## 4. 使用send唤醒
我们除了可以使用`next()`函数来唤醒生成器继续执行外，还可以使用`send()`函数来唤醒执行。使用`send()`函数的一个好处是可以在唤醒的同时向断点处传入一个附加数据。

例子：执行到`yield`时，`gen`函数作用暂时保存，返回`i`的值; `temp`接收下次`c.send("python")`，`send`发送过来的值，`c.next(`)等价`c.send(None)`
```python
def gen():
    i = 0
    while i<5:
        temp = yield i
        print(temp)  #这里使用send的时候就可以接收一个返回值
        i+=1
```
使用send(第一次不能使用,没有人接收值)
```python
In [43]: f = gen()

In [44]: next(f)
Out[44]: 0

In [45]: f.send('haha')
haha
Out[45]: 1

In [46]: next(f)
None
Out[46]: 2

In [47]: f.send('haha')
haha
Out[47]: 3

In [48]:
```
使用next函数
```python
In [11]: f = gen()

In [12]: next(f)
Out[12]: 0

In [13]: next(f)
None
Out[13]: 1

In [14]: next(f)
None
Out[14]: 2

In [15]: next(f)
None
Out[15]: 3

In [16]: next(f)
None
Out[16]: 4

In [17]: next(f)
None
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-17-468f0afdf1b9> in <module>()
----> 1 next(f)

StopIteration:
```
使用`__next__()`方法（不常使用）
```python
In [18]: f = gen()

In [19]: f.__next__()
Out[19]: 0

In [20]: f.__next__()
None
Out[20]: 1

In [21]: f.__next__()
None
Out[21]: 2

In [22]: f.__next__()
None
Out[22]: 3

In [23]: f.__next__()
None
Out[23]: 4

In [24]: f.__next__()
None
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-24-39ec527346a9> in <module>()
----> 1 f.__next__()

StopIteration:
```
## 总结
迭代器可以减少内存的空间
生成器可以是函数暂时停止执行,使用next方法继续执行

# 7.3协程-yield
协程，又称微线程，纤程。英文名`Coroutine`。

## 协程是啥
协程是python个中另外一种实现多任务的方式，只不过比线程更小占用更小执行单元（理解为需要的资源）。 为啥说它是一个执行单元，因为它自带CPU上下文。这样只要在合适的时机， 我们可以把一个协程 切换到另一个协程。 只要这个过程中保存或恢复 CPU上下文那么程序还是可以运行的。

通俗的理解：在一个线程中的某个函数，可以在任何地方保存当前函数的一些临时变量等信息，然后切换到另外一个函数中执行，注意不是通过调用函数的方式做到的，并且切换的次数以及什么时候再切换到原来的函数都由开发者自己确定

## 协程和线程差异
在实现多任务时, 线程切换从系统层面远不止保存和恢复 CPU上下文这么简单。 操作系统为了程序运行的高效性每个线程都有自己缓存Cache等等数据，操作系统还会帮你做这些数据的恢复操作。 所以线程的切换非常耗性能。但是协程的切换只是单纯的操作CPU的上下文，所以一秒钟切换个上百万次系统都抗的住。

## 简单实现协程
如果不加yield那么因为是死循环那么就会在work中跳不出来了
```python
import time

def work1():
    while True:
        print("----work1---")
        yield
        time.sleep(0.5)

def work2():
    while True:
        print("----work2---")
        yield
        time.sleep(0.5)

def main():
    w1 = work1()
    w2 = work2()
    while True:
        next(w1)
        next(w2)

if __name__ == "__main__":
    main()
```
```python
运行结果：

----work1---
----work2---
----work1---
----work2---
----work1---
----work2---
----work1---
----work2---
----work1---
----work2---
----work1---
----work2---
...省略...
```
# 7.4协程-greenlet(一般不用)
为了更好使用协程来完成多任务，python中的`greenlet`模块对其封装，从而使得切换任务变的更加简单
```python
#coding=utf-8

from greenlet import greenlet
import time

def test1():
    while True:
        print "---A--"
        gr2.switch()
        time.sleep(0.5)

def test2():
    while True:
        print "---B--"
        gr1.switch()
        time.sleep(0.5)

gr1 = greenlet(test1)
gr2 = greenlet(test2)

#切换到gr1中运行
gr1.switch()
```
# 7.5协程-gevent(常用)
`greenlet`已经实现了协程，但是这个还的人工切换，是不是觉得太麻烦了，不要捉急，python还有一个比`greenlet`更强大的并且能够自动切换任务的模块`gevent`

其原理是当一个`greenlet`遇到`IO`(指的是`input output` 输入输出，比如网络、文件操作等)操作时，比如访问网络，就自动切换到其他的`greenlet`，等到`IO`操作完成，再在适当的时候切换回来继续执行。

由于`IO`操作非常耗时，经常使程序处于等待状态，有了`gevent`为我们自动切换协程，就保证总有`greenlet`在运行，而不是等待`IO`(有延时就切换)

安装:
`pip3 install gevent`
### 1. gevent的使用
```python
import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()
```
```python
运行结果

<Greenlet at 0x10e49f550: f(5)> 0
<Greenlet at 0x10e49f550: f(5)> 1
<Greenlet at 0x10e49f550: f(5)> 2
<Greenlet at 0x10e49f550: f(5)> 3
<Greenlet at 0x10e49f550: f(5)> 4
<Greenlet at 0x10e49f910: f(5)> 0
<Greenlet at 0x10e49f910: f(5)> 1
<Greenlet at 0x10e49f910: f(5)> 2
<Greenlet at 0x10e49f910: f(5)> 3
<Greenlet at 0x10e49f910: f(5)> 4
<Greenlet at 0x10e49f4b0: f(5)> 0
<Greenlet at 0x10e49f4b0: f(5)> 1
<Greenlet at 0x10e49f4b0: f(5)> 2
<Greenlet at 0x10e49f4b0: f(5)> 3
<Greenlet at 0x10e49f4b0: f(5)> 4
```
可以看到，3个greenlet是依次运行而不是交替运行
### 2. gevent切换执行
```python
import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        #用来模拟一个耗时操作，注意不是time模块中的sleep
        gevent.sleep(1)  #注意这里的延时不是用的time.sleep()

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()
```
```python
运行结果

<Greenlet at 0x7fa70ffa1c30: f(5)> 0
<Greenlet at 0x7fa70ffa1870: f(5)> 0
<Greenlet at 0x7fa70ffa1eb0: f(5)> 0
<Greenlet at 0x7fa70ffa1c30: f(5)> 1
<Greenlet at 0x7fa70ffa1870: f(5)> 1
<Greenlet at 0x7fa70ffa1eb0: f(5)> 1
<Greenlet at 0x7fa70ffa1c30: f(5)> 2
<Greenlet at 0x7fa70ffa1870: f(5)> 2
<Greenlet at 0x7fa70ffa1eb0: f(5)> 2
<Greenlet at 0x7fa70ffa1c30: f(5)> 3
<Greenlet at 0x7fa70ffa1870: f(5)> 3
<Greenlet at 0x7fa70ffa1eb0: f(5)> 3
<Greenlet at 0x7fa70ffa1c30: f(5)> 4
<Greenlet at 0x7fa70ffa1870: f(5)> 4
<Greenlet at 0x7fa70ffa1eb0: f(5)> 4
```
### 3. 给程序打补丁(不使用gevent的延时函数)
```python
from gevent import monkey
import gevent
import random
import time

def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())

gevent.joinall([
        gevent.spawn(coroutine_work, "work1"),
        gevent.spawn(coroutine_work, "work2")
])
```
```python
运行结果

work1 0
work1 1
work1 2
work1 3
work1 4
work1 5
work1 6
work1 7
work1 8
work1 9
work2 0
work2 1
work2 2
work2 3
work2 4
work2 5
work2 6
work2 7
work2 8
work2 9
```

```python
from gevent import monkey
import gevent
import random
import time

# 有耗时操作时需要
monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块

def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())

gevent.joinall([      
        gevent.spawn(coroutine_work, "work1"),
        gevent.spawn(coroutine_work, "work2")
])   #添加所有的携程任务(更方便)
```
```python
运行结果

work1 0
work2 0
work1 1
work1 2
work1 3
work2 1
work1 4
work2 2
work1 5
work2 3
work1 6
work1 7
work1 8
work2 4
work2 5
work1 9
work2 6
work2 7
work2 8
work2 9
```
# 7.6进程、线程、协程对比
### 请仔细理解如下的通俗描述
* 有一个老板想要开个工厂进行生产某件商品（例如剪子）
* 他需要花一些财力物力制作一条生产线，这个生产线上有很多的器件以及材料这些所有的 为了能够生产剪子而准备的资源称之为：进程
* 只有生产线是不能够进行生产的，所以老板的找个工人来进行生产，这个工人能够利用这些材料最终一步步的将剪子做出来，这个来做事情的工人称之为：线程
* 这个老板为了提高生产率，想到3种办法：
    * 在这条生产线上多招些工人，一起来做剪子，这样效率是成倍増长，即单进程 多线程方式
    * 老板发现这条生产线上的工人不是越多越好，因为一条生产线的资源以及材料毕竟有限，所以老板又花了些财力物力购置了另外一条生产线，然后再招些工人这样效率又再一步提高了，即多进程 多线程方式
    * 老板发现，现在已经有了很多条生产线，并且每条生产线上已经有很多工人了（即程序是多进程的，每个进程中又有多个线程），为了再次提高效率，老板想了个损招，规定：如果某个员工在上班时临时没事或者再等待某些条件（比如等待另一个工人生产完谋道工序 之后他才能再次工作） ，那么这个员工就利用这个时间去做其它的事情，那么也就是说：如果一个线程等待某些条件，可以充分利用这个时间去做其它事情，其实这就是：协程方式
## 简单总结
* 1. 进程是资源分配的单位
* 2.线程是操作系统调度的单位
* 3.进程切换需要的资源很最大，效率很低
* 4.线程切换需要的资源一般，效率一般（当然了在不考虑GIL的情况下）
* 5.协程切换任务资源很小，效率高
* 6.多进程、多线程根据cpu核数不一样可能是并行的，但是协程是在一个线程中 所以是并发
# 7.7并发下载器
## 并发下载原理
```python
from gevent import monkey
import gevent
import urllib.request  

# 有耗时操作时需要
monkey.patch_all() 

def my_downLoad(url):
    print('GET: %s' % url) 
    resp = urllib.request.urlopen(url)  #打开这个url
    data = resp.read()  #读取的是图片的内容
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(my_downLoad, 'http://www.baidu.com/'),
        gevent.spawn(my_downLoad, 'http://www.itcast.cn/'),
        gevent.spawn(my_downLoad, 'http://www.itheima.com/'),
])
```
```python
运行结果

GET: http://www.baidu.com/
GET: http://www.itcast.cn/
GET: http://www.itheima.com/
111327 bytes received from http://www.baidu.com/.
172054 bytes received from http://www.itheima.com/.
215035 bytes received from http://www.itcast.cn/.
```
从上能够看到是先发送的获取baidu的相关信息，然后依次是itcast、itheima，但是收到数据的先后顺序不一定与发送顺序相同，这也就体现出了异步，即不确定什么时候会收到数据，顺序不一定
## 实现多个视频下载
```python
from gevent import monkey
import gevent
import urllib.request

#有IO才做时需要这一句
monkey.patch_all()

def my_downLoad(file_name, url):
    print('GET: %s' % url)
    resp = urllib.request.urlopen(url)
    data = resp.read()

    with open(file_name, "wb") as f:
        f.write(data)

    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(my_downLoad, "1.mp4", 'http://oo52bgdsl.bkt.clouddn.com/05day-08-%E3%80%90%E7%90%86%E8%A7%A3%E3%80%91%E5%87%BD%E6%95%B0%E4%BD%BF%E7%94%A8%E6%80%BB%E7%BB%93%EF%BC%88%E4%B8%80%EF%BC%89.mp4'),
        gevent.spawn(my_downLoad, "2.mp4", 'http://oo52bgdsl.bkt.clouddn.com/05day-03-%E3%80%90%E6%8E%8C%E6%8F%A1%E3%80%91%E6%97%A0%E5%8F%82%E6%95%B0%E6%97%A0%E8%BF%94%E5%9B%9E%E5%80%BC%E5%87%BD%E6%95%B0%E7%9A%84%E5%AE%9A%E4%B9%89%E3%80%81%E8%B0%83%E7%94%A8%28%E4%B8%8B%29.mp4'),
])
```
上面的url可以换为自己需要下载视频、音乐、图片等网址