# 程序员换壁纸还是用程序比较好啊,谁让windows切换壁纸的功能那么的垃圾呢
# 功能如下,这是使用的功能1,初始使用的情况
```python
欢迎使用壁纸切换系统

使用上次的文件夹路径请输入:1

在使用上次的文件夹路径的基础上追加路径:2

重新定义新的文件夹路径请输入:3

请输入选项: 1

壁纸路径不存在,请重新定义新的文件夹路径

还要添加文件路径吗?
是请输入:1
否请输入:2

请输入选项: 1

还要添加文件路径吗?
是请输入:1
否请输入:2

请输入选项: 2

请输入切换的时间间隔: 3

死鬼
想要结束系统请使用快捷键:Ctrl + C
```
# 可以设置壁纸切换的多个路径
# 可以追加壁纸切换的路径
# 可以重新定义壁纸切换的路径
# 可以定义电脑壁纸切换的时间间隔,当然不是那么的准确.没有办法那么精确,一两个小时写的东西考虑这些已经不错了


源代码如下:冗余的部分较多,懒得定义函数就直接复制粘贴了
```python
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 19:56:45 2019

@author: zangz
"""


import random
import ctypes
import time
import os
import random
import tkinter as tk
from tkinter import filedialog
import os

 
# path = "E:\\私密文件\\壁纸\\横屏壁纸收集\\sex\\" #存储图片的文件夹

print()
print("欢迎使用壁纸切换系统")
print()
print("查看当前壁纸路径吗?")
print("查看请输入:1")
print("否请输入:2")
look_lujing=int(input("请输入选项: "))

if look_lujing == 1:
    exists=os.path.exists("壁纸路径.txt")  #判断这个文件存在与否,返回值为True或者False
    if exists:  #存在的话就直接读取路径
        print()
        print("当前壁纸路径有:")
        print()
        file=open("壁纸路径.txt")
        for line in file.readlines():    
            curLine=line.strip()
            print(curLine+'\n')
        print("请选择您要进行的操作:")
        print()
    else:
        print()
        print("当前壁纸路径不存在")
        print()
        print("请选择您要进行的操作:")
        print()

else:
    print()
    print("请选择您要进行的操作:")
    print()
print("使用上次的文件夹路径请输入:1")
print()
print("在使用上次的文件夹路径的基础上追加路径:2")
print()
print("重新定义新的文件夹路径请输入:3")
print()
num=int(input("请输入选项: "))


if num ==1:  #进入的是使用存在的路径
    exists=os.path.exists("壁纸路径.txt")  #判断这个文件存在与否,返回值为True或者False
    if exists:  #存在的话就直接读取路径
        print()
        print("壁纸路径存在")
        print()
    else:
        print()
        print("壁纸路径不存在,请重新定义新的文件夹路径")
        exists=os.path.exists("壁纸路径.txt")  #判断这个文件存在与否,返回值为True或者False
        if exists:  #冗余代码懒得删
            os.remove("壁纸路径.txt")
        else:
            pass
        while True:
            print()
            print("还要添加文件路径吗?"+'\n'+"是请输入:1"+"\n"+"否请输入:2")
            print()
            a=int(input("请输入选项: "))
            if a==1:
                root = tk.Tk()
                root.withdraw()
                path = filedialog.askdirectory()
                path+="/"   #这里需要添加""/"不然无法读取这个文件夹中的内容
                with open("壁纸路径.txt",'a') as f:
                        f.write(path+'\n')
            elif a==2:
                break
    #最后都要从本地的文件中读取路径
    path_list=[]
    file=open("壁纸路径.txt")
    for line in file.readlines():    
        curLine=line.strip()
        path_list.append(curLine)  


elif num ==2:
    exists=os.path.exists("壁纸路径.txt")  #判断这个文件存在与否,返回值为True或者False
    if exists:  #如果存在就继续添加路径
        while True:
            print()
            print("还要添加文件路径吗?"+'\n'+"是请输入:1"+"\n"+"否请输入:2")
            print()
            a=int(input("请输入选项: "))
            if a==1:
                root = tk.Tk()
                root.withdraw()
                path = filedialog.askdirectory()
                path+="/"   #这里需要添加""/"不然无法读取这个文件夹中的内容
                with open("壁纸路径.txt",'a') as f:
                        f.write(path+'\n')
            elif a==2:
                break

    else:
        print("壁纸路径不存在,请重新定义新的文件夹路径")
        exists=os.path.exists("壁纸路径.txt")  #判断这个文件存在与否,返回值为True或者False
        if exists:
            os.remove("壁纸路径.txt")
        else:
            pass
        while True:
            print()
            print("还要添加文件路径吗?"+'\n'+"是请输入:1"+"\n"+"否请输入:2")
            print()
            a=int(input("请输入选项: "))
            if a==1:
                root = tk.Tk()
                root.withdraw()
                path = filedialog.askdirectory()
                path+="/"   #这里需要添加""/"不然无法读取这个文件夹中的内容
                with open("壁纸路径.txt",'a') as f:
                        f.write(path+'\n')
            elif a==2:
                break
    
    path_list=[]
    file=open("壁纸路径.txt")
    for line in file.readlines():    
        curLine=line.strip()
        path_list.append(curLine)  







elif num==3:
    exists=os.path.exists("壁纸路径.txt")  #判断这个文件存在与否,返回值为True或者False
    if exists:
        os.remove("壁纸路径.txt")
    else:
        pass
    while True:
        print()
        print("还要添加文件路径吗?"+'\n'+"是请输入:1"+"\n"+"否请输入:2")
        print()
        a=int(input("请输入选项: "))
        if a==1:
            root = tk.Tk()
            root.withdraw()
            path = filedialog.askdirectory()
            path+="/"   #这里需要添加""/"不然无法读取这个文件夹中的内容
            with open("壁纸路径.txt",'a') as f:
                    f.write(path+'\n')
        elif a==2:
            break
    
    path_list=[]
    file=open("壁纸路径.txt")
    for line in file.readlines():    
        curLine=line.strip()
        path_list.append(curLine)  
else:
    for q in range(100):
        print()
        print("你是傻逼吗?"+"\n"+"你是傻逼吗?"+"\n"+"你是傻逼吗?")
        time.sleep(0.2) #睡眠时间
    print("老子不跟你玩了,再见!")
    exit()
print()
sleepTime=float(input("请输入切换的时间间隔: "))
print()
print("死鬼")
print("想要结束系统请使用快捷键:Ctrl + C")


while True:  
    index=int(random.random()*len(path_list))
    path=path_list[index]
    file = os.listdir(path)   #打开存储图片文件夹中的图片目录
    filepath = path + random.choice(file) #随机选取某张图片，建立绝对地址
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0) # 设置桌面壁纸
    time.sleep(sleepTime) #睡眠时间


#pyinstaller -F -i tubiao.ico 壁纸切换.py      #打包的代码
```
上述代码使用请谨慎,有恶意删除的代码.程序员懂得自然懂.

最后使用的是puinstaller进行了打包
想要直接使用exe文件的请自觉赞赏一下,私信我,我发给你.exe文件中没有恶意代码
