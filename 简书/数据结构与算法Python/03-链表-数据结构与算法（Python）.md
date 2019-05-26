# 链表

### 为什么需要链表

顺序表的构建需要预先知道数据大小来申请连续的存储空间，而在进行扩充时又需要进行数据的搬迁，所以使用起来并不是很灵活。

链表结构可以充分利用计算机内存空间，实现灵活的内存动态管理。

### 链表的定义

链表（Linked list）是一种常见的基础数据结构，是一种**线性表**，但是不像顺序表一样连续存储数据，而是在每一个节点（数据存储单元）里存放下一个节点的位置信息（即地址）。

![image.png](https://upload-images.jianshu.io/upload_images/14555448-afb7d88284f2bab9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![链表简单演示图](https://upload-images.jianshu.io/upload_images/14555448-e92c3b4d6dea0666.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### python变量标识的本质
![Python变量标识本质.jpeg](https://upload-images.jianshu.io/upload_images/14555448-990cc4a46d3af7c0.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)






## 3.1 单向链表

单向链表也叫单链表，是链表中最简单的一种形式，它的每个节点包含两个域，一个信息域（元素域）和一个链接域。这个链接指向链表中的下一个节点，而最后一个节点的链接域则指向一个空值。

![image.png](https://upload-images.jianshu.io/upload_images/14555448-e221048aa2ac643d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


*   表元素域elem用来存放具体的数据。
*   链接域next用来存放下一个节点的位置（python中的标识）
*   变量p指向链表的头节点（首节点）的位置，从p出发能找到表中的任意节点。




### 节点实现(定义成类)

```python
class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None   #不知道的情况下设置为空

```

### 单链表的操作

*   is_empty() 链表是否为空
*   length() 链表长度
*   travel() 遍历整个链表
*   add(item) 链表头部添加元素
*   append(item) 链表尾部添加元素
*   insert(pos, item) 指定位置添加元素
*   remove(item) 删除节点
*   search(item) 查找节点是否存在
![单链表操作.jpeg](https://upload-images.jianshu.io/upload_images/14555448-7474c6960ce5e3f4.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 单链表的实现

```python
class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None   #不知道的情况下设置为空


class SingleLinkList(object):
    """单链表"""
    def __init__(self,node=None): #node=None保证了先创建链表再创建节点照样可以使用.就是一个空的链表
        self._head = node   #必须存在一个属性指向第一个节点(对象属性)==头结点

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None   #相等就是空的,返回的就是True(是空的)

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self._head   #(游标)
        count = 0   #初始为零
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head   #建立current游标
        while cur != None:
            print (cur.item)
            cur = cur.next
        print ("")

```

**头部添加元素**

![image.png](https://upload-images.jianshu.io/upload_images/14555448-5dd7a28dfe920f9a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


```python
    def add(self, item):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self._head
        # 将链表的头_head指向新节点
        self._head = node

```

**尾部添加元素**

```python
    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
```

**指定位置添加元素**

![image.png](https://upload-images.jianshu.io/upload_images/14555448-ec2b25bbf89484f3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

这里操作的是插入位置的前一个元素,如果下一个元素那么就不能将前一个元素指向新添加的元素了
```python
    def insert(self, pos, item):
        """指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length()-1):
            self.append(item)
        # 找到指定位置
        else:
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self._head
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

```

**删除节点**

![image.png](https://upload-images.jianshu.io/upload_images/14555448-e0c69d758e87c8ea.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


```
    def remove(self,item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

```

**查找节点是否存在**

```
    def search(self,item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

```

**测试**

```
if __name__ == "__main__":
    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    print "length:",ll.length()
    ll.travel()
    print ll.search(3)
    print ll.search(5)
    ll.remove(1)
    print "length:",ll.length()
    ll.travel()

```
**索引查找链表的值**
```python
    def index(self,index):
        """返回索引链表值"""
        cur = self._head   #建立current游标
        count = 0  #用来计数
        while count < index: #当游标没有到达指定索引位置就继续执行while循环
            cur = cur.next
            count+=1
        return cur.item   #while结束循环,返回索引到的值
```
完整的代码:
```python
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 08:20:37 2019

@author: zangz
"""
class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None   #不知道的情况下设置为空


class SingleLinkList(object):
    """单链表"""
    def __init__(self,node=None): #node=None保证了先创建链表再创建节点照样可以使用.就是一个空的链表
        self._head = node   #必须存在一个属性指向第一个节点(对象属性)==头结点

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None   #相等就是空的,返回的就是True(是空的)

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self._head   #(游标)
        count = 0   #初始为零
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head   #建立current游标
        while cur != None:
            print (cur.item)
            cur = cur.next
        print ("")
        
    def add(self, item):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self._head
        # 将链表的头_head指向新节点
        self._head = node
       
        
        
        
    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            
            
    def insert(self, pos, item):
        """指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length()-1):
            self.append(item)
        # 找到指定位置
        else:
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self._head   #pre指向节点
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node
            
     
    def search(self,item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
    
    def remove(self,item):
        """删除节点"""
        cur = self._head
        pre = None   #pre游标先移
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur  #先移动pre.再移动current
                cur = cur.next
    def index(self,index):
        """返回索引链表值"""
        cur = self._head   #建立current游标
        count = 0  #用来计数
        while count < index: #当游标没有到达指定索引位置就继续执行while循环
            cur = cur.next
            count+=1
        return cur.item   #while结束循环,返回索引到的值
            
if __name__ == "__main__":
    ll = SingleLinkList()
    print("链表是否为空: ",ll.is_empty())
    print("链表的长度: ",ll.length())
    
    ll.append(1)  #向链表的尾部插入一个元素1
    print("链表的长度: ",ll.length())
    ll.append(2)
    ll.add(8)   #在头部插入元素
    ll.append(3)
    ll.append(4)
    ll.insert(3,100)
    ll.travel()  #遍历
    print("判断元素是不是在链表中: ",ll.search(100))
    print("索引链表中的元素: ",ll.index(0))
```
### 链表与顺序表的对比

链表失去了顺序表随机读取的优点，同时链表由于增加了结点的指针域，空间开销比较大，但对存储空间的使用要相对灵活。

链表与顺序表的各种操作复杂度如下所示：

| 操作 | 链表 | 顺序表 |
| --- | --- | --- |
| 访问元素 | O(n) | O(1) |
| 在头部插入/删除 | O(1) | O(n) |
| 在尾部插入/删除 | O(n) | O(1) |
| 在中间插入/删除 | O(n) | O(n) |

注意虽然表面看起来复杂度都是 O(n)，但是链表和顺序表在插入和删除时进行的是完全不同的操作。链表的主要耗时操作是遍历查找，删除和插入操作本身的复杂度是O(1)。顺序表查找很快，主要耗时的操作是拷贝覆盖。因为除了目标元素在尾部的特殊情况，顺序表进行插入和删除时需要对操作点之后的所有元素进行前后移位操作，只能通过拷贝和覆盖的方法进行。


## 3.2 单向循环链表

单链表的一个变形是单向循环链表，链表中最后一个节点的next域不再为None，而是指向链表的头节点。

![image.png](https://upload-images.jianshu.io/upload_images/14555448-c223058950ee5ec4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![单向循环链表.jpeg](https://upload-images.jianshu.io/upload_images/14555448-65fd1781138b811b.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 操作

*   is_empty() 判断链表是否为空
*   length() 返回链表的长度
*   travel() 遍历
*   add(item) 在头部添加一个节点
*   append(item) 在尾部添加一个节点
*   insert(pos, item) 在指定位置pos添加节点
*   remove(item) 删除一个节点
*   search(item) 查找节点是否存在


### 实现
```python
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:52:13 2019

@author: zangz
"""

class Node(object):
    """节点"""
    def __init__(self, item):
        self.item = item
        self.next = None


class SinCycLinkedlist(object):
    """单向循环链表"""
    def __init__(self,node=None):
        self._head = node   #循环列表需要节点循环,因此只有一个节点的时候需要进行下一步
        if node:
            node.next = node #如果创建的不是空的链表就让其指向自身   
    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None  #不用改与单链表一样

    def length(self):
        """返回链表的长度"""
        # 如果链表为空，返回长度0,也是为了下面的count=1做准备
        if self.is_empty():
            return 0
        count = 1 #首先给计数一次,然后就让游标指向的是下一个节点:cur.next,这样才能满足循环的条件
        cur = self._head
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self._head  #指向的是第一个节点
        print (cur.item)  #打印的是第一个节点的值
        while cur.next != self._head:
            cur = cur.next
            print (cur.item)   
        print ("")


    def add(self, item):
        """头部添加节点"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            #添加的节点指向_head
            node.next = self._head
            
            # 移到链表尾部，将尾部节点的next指向node
            cur = self._head
            while cur.next != self._head:
                cur = cur.next   #退出循环指向的是尾部的节点
            cur.next = node  #将尾部节点的next指向node
            #_head指向添加node的
            self._head = node

    def append(self, item):
        """尾部添加节点"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            # 移到链表尾部
            cur = self._head
            while cur.next != self._head:
                cur = cur.next  #得到尾结点
            # 将尾节点指向node
            cur.next = node
            # 将node指向头节点_head
            node.next = self._head

    def insert(self, pos, item):
        """在指定位置添加节点"""
        if pos <= 0:   #头插
            self.add(item)
        elif pos > (self.length()-1):  #尾插
            self.append(item)
        else:   #不涉及断开循环
            node = Node(item)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos-1):
                count += 1
                cur = cur.next  #得到插入位置的前一个节点
            node.next = cur.next    #将节点的next指向下一个节点
            cur.next = node   #   #将前一个节点指向该节点

    def remove(self, item):
        """删除一个节点"""
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        # 将cur指向头节点
        cur = self._head
        pre = None
        # 若头节点的元素就是要查找的元素item
        if cur.item == item:
            # 如果链表不止一个节点
            if cur.next != self._head:
                # 先找到尾节点，将尾节点的next指向第二个节点
                while cur.next != self._head:
                    cur = cur.next
                # cur指向了尾节点
                cur.next = self._head.next
                self._head = self._head.next
            else:
                # 链表只有一个节点
                self._head = None
        else:
            pre = self._head
            # 第一个节点不是要删除的
            while cur.next != self._head:
                # 找到了要删除的元素
                if cur.item == item:
                    # 删除
                    pre.next = cur.next
                    return   #不能使用break
                else:
                    pre = cur
                    cur = cur.next
            # cur 指向尾节点
            if cur.item == item:
                # 尾部删除
                pre.next = cur.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self._head
        if cur.item == item:  #首先判断第一个节点
            return True   
        while cur.next != self._head:  #循环是遍历不到最后一个节点的
            cur = cur.next
            if cur.item == item:
                return True
        return False
    
    def index(self,index):
        """返回索引链表值"""  #循环链表注意输入的值如果超了会循环回开始的节点
        cur = self._head   #建立current游标
        count = 0  #用来计数
        while count < index: #当游标没有到达指定索引位置就继续执行while循环
            cur = cur.next
            count+=1
        return cur.item   #while结束循环,返回索引到的值

if __name__ == "__main__":
    ll = SinCycLinkedlist()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print ("length:",ll.length())
    ll.travel()
    print (ll.search(3))
    print( ll.search(7))
    ll.remove(1)
    print( "length:",ll.length())
    ll.travel()
    print(ll.index(6))
```
## 3.3 双向链表

一种更复杂的链表是“双向链表”或“双面链表”。每个节点有两个链接：一个指向前一个节点，当此节点为第一个节点时，指向空值；而另一个指向下一个节点，当此节点为最后一个节点时，指向空值。

![image.png](https://upload-images.jianshu.io/upload_images/14555448-c3655e95db14300d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![双向链表.jpeg](https://upload-images.jianshu.io/upload_images/14555448-4b2bb0c321a04564.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


### 操作

*   is_empty() 链表是否为空
*   length() 链表长度
*   travel() 遍历链表
*   add(item) 链表头部添加
*   append(item) 链表尾部添加
*   insert(pos, item) 指定位置添加
*   remove(item) 删除节点
*   search(item) 查找节点是否存在

### 实现

```python
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 09:31:16 2019

@author: zangz
"""

class Node(object):
    """双向链表节点"""
    def __init__(self, item):
        self.item = item  #数据
        self.next = None  #后继
        self.prev = None  #前驱

class DLinkList(object):
    """双向链表"""
    def __init__(self,node=None):
        self._head = node     #定义头结点
        

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """返回链表的长度"""
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print (cur.item)
            cur = cur.next
        print( "")

    def add(self, item):
        """头部插入元素"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self._head = node
        else:
            # 将node的next指向_head的头节点
            node.next = self._head
            # 将_head的头节点的prev指向node
            self._head.prev = node
            # 将_head 指向node
            self._head = node

    def append(self, item):
        """尾部插入元素"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self._head = node
        else:
            # 移动到链表尾部
            cur = self._head
            while cur.next != None:
                cur = cur.next
            # 将尾节点cur的next指向node
            cur.next = node
            # 将node的prev指向cur
            node.prev = cur

    def search(self, item):
        """查找元素是否存在"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

```

**指定位置插入节点**

![image.png](https://upload-images.jianshu.io/upload_images/14555448-536fd2769cb29e34.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


```python
    def insert(self, pos, item):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos-1):
                count += 1
                cur = cur.next
            # 将node的prev指向cur
            node.prev = cur
            # 将node的next指向cur的下一个节点
            node.next = cur.next
            # 将cur的下一个节点的prev指向node
            cur.next.prev = node
            # 将cur的next指向node
            cur.next = node

```

**删除元素**

![image.png](https://upload-images.jianshu.io/upload_images/14555448-ac696b2b9f1c3f01.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


```python
    def remove(self, item):
        """删除元素"""
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                # 如果首节点的元素即是要删除的元素
                if cur.next == None:
                    # 如果链表只有这一个节点
                    self._head = None
                else:
                    # 将第二个节点的prev设置为None
                    cur.next.prev = None
                    # 将_head指向第二个节点
                    self._head = cur.next
                return
            while cur != None:
                if cur.item == item:
                    # 将cur的前一个节点的next指向cur的后一个节点
                    cur.prev.next = cur.next
                    # 将cur的后一个节点的prev指向cur的前一个节点
                    cur.next.prev = cur.prev
                    break
                cur = cur.next

```

**测试**

```python
    
if __name__ == "__main__":
    ll = DLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print ("length:",ll.length())
    ll.travel()
    print (ll.search(3))
    print (ll.search(4))
    ll.remove(1)
    print ("length:",ll.length())
    ll.travel()
```
完整代码:
```python
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 09:31:16 2019

@author: zangz
"""

class Node(object):
    """双向链表节点"""
    def __init__(self, item):
        self.item = item  #数据
        self.next = None  #后继
        self.prev = None  #前驱

class DLinkList(object):
    """双向链表"""
    def __init__(self,node=None):
        self._head = node     #定义头结点
        

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """返回链表的长度"""
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print (cur.item)
            cur = cur.next
        print( "")

    def add(self, item):
        """头部插入元素"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self._head = node
        else:
            # 将node的next指向_head的头节点
            node.next = self._head
            # 将_head的头节点的prev指向node
            self._head.prev = node
            # 将_head 指向node
            self._head = node

    def append(self, item):
        """尾部插入元素"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self._head = node
        else:
            # 移动到链表尾部
            cur = self._head
            while cur.next != None:
                cur = cur.next
            # 将尾节点cur的next指向node
            cur.next = node
            # 将node的prev指向cur
            node.prev = cur

    def insert(self, pos, item):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos-1):
                count += 1
                cur = cur.next
            # 将node的prev指向cur
            node.prev = cur
            # 将node的next指向cur的下一个节点
            node.next = cur.next
            # 将cur的下一个节点的prev指向node
            cur.next.prev = node
            # 将cur的next指向node
            cur.next = node

    def remove(self, item):
        """删除元素"""
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                # 如果首节点的元素即是要删除的元素
                if cur.next == None:
                    # 如果链表只有这一个节点
                    self._head = None
                else:
                    # 将第二个节点的prev设置为None
                    cur.next.prev = None
                    # 将_head指向第二个节点
                    self._head = cur.next
                return
            while cur != None:
                if cur.item == item:
                    # 将cur的前一个节点的next指向cur的后一个节点
                    cur.prev.next = cur.next
                    # 将cur的后一个节点的prev指向cur的前一个节点
                    cur.next.prev = cur.prev
                    break
                cur = cur.next


    def search(self, item):
        """查找元素是否存在"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
    
    def index(self,index):
        """返回索引链表值"""
        cur = self._head   #建立current游标
        count = 0  #用来计数
        while count < index: #当游标没有到达指定索引位置就继续执行while循环
            cur = cur.next
            count+=1
        return cur.item   #while结束循环,返回索引到的值   
    
if __name__ == "__main__":
    ll = DLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print ("length:",ll.length())
    ll.travel()
    print (ll.search(3))
    print (ll.search(4))
    ll.remove(1)
    print ("length:",ll.length())
    ll.travel()
    print(ll.index(4))
```
