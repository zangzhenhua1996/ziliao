# 翻看了不少别人写的例子,发现虽然程序简单但是功能实现不是很好,自己做出了一些小的改进:代码依旧冗余,以后再修改,嘿嘿
话不多少上代码:
```python
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:12:44 2019

@author: zangz
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 16:18:42 2018

@author: zangz
"""
import time
import os
from time import sleep
from shutil import copytree
from psutil import disk_partitions  #获取分区的信息
def copy_u_to_computer():
    a=True  #定义while循环结束的标志
    while (a):  #写一个一直循环的while
        sleep(1)  #暂停一秒
        #检查所有驱动器
        for item in disk_partitions():
            #发现可移动驱动器
            #(if语句的意思是):如果在opts中包含'removable'信息就继续往下执行if语句中的内容
            #不使用==的原因是opts信息中不仅包含'removable'信息和'fixed'信息
            if 'removable' in item.opts:   #removable是可拆卸的意思,fixed是固定的意思(移动硬盘同样是固定的,只有u盘会检测是removable)
                driver,opts=item.device,item.opts  #device是驱动器的根目录比如F:\
                #输出可移动驱动器符号
                print('发现优盘,嘿嘿',driver)
                a=False  #发现优盘就停止while循环
                                #复制根目录
                #
                #生成拷贝到的路径:使用时间作为路径
                # 获取当前时间
                now_time = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
                #由于创建文件夹时不能有:等非法的字符,所以使用replace函数进行过滤
                now_time1=now_time.replace(':','-')
                
                print(now_time1)
                #创建一个使用时间为文件名的路径
                path='E:\\拷贝\\'+str(now_time1)
                #拷贝优盘中所有的文件
                copytree(driver,path)
                
                break
            else:
                print('没发现可移动优盘')
        a=False  #循环查看完一遍所有的驱动器还是没有发现可移动的优盘就跳出循环(有可能是移动硬盘)
    


qu_num=len(disk_partitions())

print(qu_num)

while(True):  #这里的while循环保证了,只要驱动器的个数与设定的不一样就会执行拷贝函数

    if len(disk_partitions()) == qu_num:
        print("驱动器个数未改变")
        sleep(3)
        
    else:
        print("驱动器个数发生改变,准备拷贝优盘的内容")
        qu_num=len(disk_partitions())  #改变驱动器的个数防止执行拷贝函数后死循环
        print(qu_num)
        copy_u_to_computer()  #执行拷贝函数
    
        
    
    
```
测试的结果很是很给力的,由于是死循环就不截图了
