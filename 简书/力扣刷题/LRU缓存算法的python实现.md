```python
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 08:23:40 2019

@author: zangz
"""
from collections import OrderedDict #导入这个可以对键排序的字典
class LRUCache:
    def __init__(self,capacity=128):
        self.od = OrderedDict()
        self.capacity = capacity #设置一歌最大的容量
    def get(self,key): #每次访问的时候更新最新使用的 Key
        if key in self.od:
            val = self.od[key] #取出这个键对应的值
            self.od.move_to_end(key) #将访问过的键值移动到这个字典的最后面
            return val #返回要的值
        else:
            return -1
    def put(self,key,value): #更新k/v
        if key in self.od: #如果这个键已经存在了
            del self.od[key] #删除
            self.od[key] = value #更新key到表头
        else: #不在字典中就执行插入
            self.od[key]=value #进行插入操作
            #判断当前的容量是不是已经满了
            if len(self.od) >self.capacity:
                self.od.popitem(last=False) #如果已经满了就抛弃字典的最后一个也就是最近最少使用的
            
```
