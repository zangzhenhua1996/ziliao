[官网网址](https://pypi.org/project/psutil/)
### 一、psutil模块:

1. psutil是一个跨平台库,能够轻松实现获取系统运行的进程和系统利用率（包括CPU、内存、磁盘、网络等）信息。它主要用来做系统监控，性能分析，进程管理。它实现了同等命令行工具提供的功能，如ps、top、lsof、netstat、ifconfig、who、df、kill、free、nice、ionice、iostat、iotop、uptime、pidof、tty、taskset、pmap等。目前支持32位和64位的Linux、Windows、OS X、FreeBSD和Sun Solaris等操作系统.
2.安装psutil模块：如果是安装了anaconda会自带这个模块
```bash
CentOS安装psutil包：
python版本：3.5
 
wget https://pypi.python.org/packages/source/p/psutil/psutil-3.2.1.tar.gz --no-check-certificate
tar zxvf psutil-3.2.1.tar.gz
cd psutil-3.2.1
python setup.py install
 
Windos安装psutil包：
 
D:\python35\Scripts>pip3.exe install psutil
Collecting psutil
  Downloading psutil-5.3.1-cp35-cp35m-win_amd64.whl (215kB)
    100% |████████████████████████████████| 225kB 84kB/s
Installing collected packages: psutil
Successfully installed psutil-5.3.1
```
二、.获取系统基本信息的使用:

#### 1.CPU信息
使用cpu_times方法获取cpu的完整信息，如下所示。
```python
In [3]: psutil.cpu_times()
Out[3]: scputimes(user=22096.843749999996, system=23272.625, idle=272734.671875, interrupt=454.625, dpc=385.421875)
```
获取单个数据，如查看用户的cpu时间比，如下所示：

```python
In [8]: psutil.cpu_times().user
Out[8]: 22285.656249999996
```
获取cpu逻辑和物理个数，默认logical值为True 。
```python
#CPU逻辑个数
In [9]: psutil.cpu_count()
Out[9]: 4
#CPU物理个数
In [10]: psutil.cpu_count(logical=False)
Out[10]: 2
```
获取cpu的使用率:
```python
In [28]: psutil.cpu_percent()  #总得占有率
Out[28]: 14.0

In [29]: psutil.cpu_percent(1)  #pid为1的进程的cpu占有率
Out[29]: 11.1
```
#### 2.内存信息
内存信息的获取主要使用virtual_memory方法。swap使用就用swap_memory方法。
```python
In [3]: psutil.virtual_memory()
Out[3]: svmem(total=8485965824, available=4302585856, percent=49.3, used=4183379968, free=4302585856)
```
其中percent表示实际已经使用的内存占比，即（8485965824-4302585856）/8485965824*100% 。available表示还可以使用的内存。
获取单个的信息跟cpu的使用是一样的,比如获取内存的使用率
```python
In [5]: psutil.virtual_memory().percent
Out[5]: 48.9
```
#### 交换分区的信息
```python
In [4]: psutil.swap_memory()
Out[4]: sswap(total=10566340608, used=5468590080, free=5097750528, percent=51.8, sin=0, sout=0)
```
###  3.磁盘信息
磁盘信息主要有两部分，一个是磁盘的利用率，一个是io，他们分别可以通过disk_usage和disk_io_counters方法获取。

如下先获取分区信息，然后看下根分区的使用情况:
```python
In [6]: psutil.disk_partitions()
Out[6]:
[sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed'),
 sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed'),
 sdiskpart(device='E:\\', mountpoint='E:\\', fstype='NTFS', opts='rw,fixed'),
 sdiskpart(device='F:\\', mountpoint='F:\\', fstype='NTFS', opts='rw,fixed'),
 sdiskpart(device='G:\\', mountpoint='G:\\', fstype='NTFS', opts='rw,fixed'),
 sdiskpart(device='M:\\', mountpoint='M:\\', fstype='NTFS', opts='rw,fixed'),
 sdiskpart(device='N:\\', mountpoint='N:\\', fstype='NTFS', opts='rw,fixed'),
 sdiskpart(device='O:\\', mountpoint='O:\\', fstype='NTFS', opts='rw,fixed'),
 sdiskpart(device='P:\\', mountpoint='P:\\', fstype='NTFS', opts='rw,fixed')]
```
查看某个分区的信息
```python
In [9]: psutil.disk_usage('c:')
Out[9]: sdiskusage(total=107375226880, used=48413634560, free=58961592320, percent=45.1)

In [10]: psutil.disk_usage('D:')
Out[10]: sdiskusage(total=132677468160, used=51502489600, free=81174978560, percent=38.8)

In [11]: psutil.disk_usage('E:')  #注意一定要有:
Out[11]: sdiskusage(total=224426729472, used=201101312, free=224225628160, percent=0.1)
```
默认disk_io_counters方法获取的是硬盘总的io数和读写信息，如果需要获取单个硬盘的io和读写信息加上"perdisk=True"参数。
```python
In [15]: psutil.disk_io_counters()
Out[15]: sdiskio(read_count=14388378, write_count=5578458, read_bytes=858581854208, write_bytes=40740875776, read_time=10644, write_time=3237)
In [18]: psutil.disk_io_counters("perdisk=True")   #这里的分区是整个盘,我这里挂载了三块盘
Out[18]:
{'PhysicalDrive0': sdiskio(read_count=2357409, write_count=5552659, read_bytes=77187101184, write_bytes=40293819904, read_time=2817, write_time=2244),
 'PhysicalDrive1': sdiskio(read_count=868070, write_count=25558, read_bytes=49977322496, write_bytes=447356928, read_time=4129, write_time=935),
 'PhysicalDrive2': sdiskio(read_count=11338523, write_count=1000, read_bytes=742926391808, write_bytes=8146944, read_time=3770, write_time=58)}
```
#### 4.网络信息：
 网络io和磁盘io使用方法差不多，主要使用net_io_counters方法，如果需要获取单个网卡的io信息，加上pernic=True参数。
```python
In [20]: #获取网络总的io情况

In [21]: psutil.net_io_counters()
Out[21]: snetio(bytes_sent=1926789, bytes_recv=10124347, packets_sent=33645, packets_recv=11464, errin=0, errout=0, dropin=0, dropout=0)

In [22]: #获取网卡的io情况

In [23]: psutil.net_io_counters(pernic=True)
Out[23]:
{'以太网': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0),
 '本地连接* 9': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0),
 '本地连接* 10': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0),
 'VMware Network Adapter VMnet1': snetio(bytes_sent=7784, bytes_recv=168, packets_sent=7783, packets_recv=168, errin=0, errout=0, dropin=0, dropout=0),
 'VMware Network Adapter VMnet8': snetio(bytes_sent=17403, bytes_recv=167, packets_sent=17403, packets_recv=167, errin=0, errout=0, dropin=0, dropout=0),
 'WLAN': snetio(bytes_sent=1962230, bytes_recv=10165831, packets_sent=8554, packets_recv=11234, errin=0, errout=0, dropin=0, dropout=0),
 'Loopback Pseudo-Interface 1': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0)}
#### 5.其他系统信息：
1. 获取开机时间(不是当前时间是开机的时间)
```python
In [24]:  psutil.boot_time()
Out[24]: 1556333804.0
#转换成自然时间格式
In [26]: import datetime

In [27]: datetime.datetime.fromtimestamp(psutil.boot_time ()).strftime("%Y-%m-%d %H: %M: %S")
Out[27]: '2019-04-27 10: 56: 44'  #现在的时间是4-28
```
2.查看系统全部进程
```python

In [31]: psutil.pids()
Out[31]:   #输出太多了就不全部剪切了
[0,
 4,
 96,
 380,
 540,
 680,
 692,
 712,
 820,
 844,
 892,
 928,
 956,
```
3.查看单个进程
```python
p = psutil.Process(16031)
p.name()      #进程名
p.exe()         #进程的bin路径
p.cwd()        #进程的工作目录绝对路径
p.status()     #进程状态
p.create_time()  #进程创建时间
p.uids()      #进程uid信息
p.gids()      #进程的gid信息
p.cpu_times()    #进程的cpu时间信息,包括user,system两个cpu信息
p.cpu_affinity()  #get进程cpu亲和度,如果要设置cpu亲和度,将cpu号作为参考就好
p.memory_percent()  #进程内存利用率
p.memory_info()    #进程内存rss,vms信息
p.io_counters()    #进程的IO信息,包括读写IO数字及参数
p.connectios()    #返回进程列表
p.num_threads()  #进程开启的线程数
听过psutil的Popen方法启动应用程序，可以跟踪程序的相关信息
from subprocess import PIPE
p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"],stdout=PIPE)
p.name()
p.username()
```
 查看系统硬件脚本：:
```python
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:40:47 2019

@author: zangz
"""

#!/usr/bin/env python
#coding:utf-8

import psutil
import datetime
import time

# 当前时间
now_time = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
print(now_time)

# 查看cpu物理个数的信息
print(u"物理CPU个数: %s" % psutil.cpu_count(logical=False))

#CPU的使用率
cpu = (str(psutil.cpu_percent(1))) + '%'
print(u"cup使用率: %s" % cpu)

#查看内存信息,剩余内存.free  总共.total
#round()函数方法为返回浮点数x的四舍五入值(这里取了2位)。这里是bit所以换算成G需要除以1024**3

free = str(round(psutil.virtual_memory().free / (1024.0 **3), 2))
total = str(round(psutil.virtual_memory().total / (1024.0 * 1024.0 * 1024.0), 2))
memory = int(psutil.virtual_memory().total - psutil.virtual_memory().free) / float(psutil.virtual_memory().total)
print(u"物理内存： %s G" % total)
print(u"剩余物理内存： %s G" % free)
print(u"物理内存使用率： %s %%" % int(memory * 100))
# 系统启动时间
print(u"系统启动时间: %s" % datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))

# 系统用户
users_count = len(psutil.users())
#
# >>> for u in psutil.users():
# ...   print(u)
# ...
# suser(name='root', terminal='pts/0', host='61.135.18.162', started=1505483904.0)
# suser(name='root', terminal='pts/5', host='61.135.18.162', started=1505469056.0)
# >>> u.name
# 'root'
# >>> u.terminal
# 'pts/5'
# >>> u.host
# '61.135.18.162'
# >>> u.started
# 1505469056.0
# >>>

users_list = ",".join([u.name for u in psutil.users()])
print(u"当前有%s个用户，分别是 %s" % (users_count, users_list))

#网卡，可以得到网卡属性，连接数，当前流量等信息
net = psutil.net_io_counters()
bytes_sent = '{0:.2f} Mb'.format(net.bytes_recv / 1024 / 1024)
bytes_rcvd = '{0:.2f} Mb'.format(net.bytes_sent / 1024 / 1024)
print(u"网卡接收流量 %s 网卡发送流量 %s" % (bytes_rcvd, bytes_sent))

io = psutil.disk_partitions()
# print(io)
# print("io[-1]为",io[-1])
#del io[-1]

print('-----------------------------磁盘信息---------------------------------------')

print("系统磁盘信息：" + str(io))

for i in io:
    o = psutil.disk_usage(i.device)   #N:\\(i.device)
    print("总容量：" + str(int(o.total / (1024.0 * 1024.0 * 1024.0))) + "G")
    print("已用容量：" + str(int(o.used / (1024.0 * 1024.0 * 1024.0))) + "G")
    print("可用容量：" + str(int(o.free / (1024.0 * 1024.0 * 1024.0))) + "G")

print('-----------------------------进程信息-------------------------------------')
# 查看系统全部进程
for pnum in psutil.pids():
    p = psutil.Process(pnum)
    print(u"进程名 %-20s  内存利用率 %-18s 进程状态 %-10s 创建时间 %-10s " \
    % (p.name(), p.memory_percent(), p.status(), p.create_time()))


```
