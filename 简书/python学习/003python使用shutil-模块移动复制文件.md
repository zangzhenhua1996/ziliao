*# shutil模块:主要作用与拷贝文件用的。

> 引入： `import shutil`

###1. `shutil.copyfileobj(文件1，文件2)`：将文件1的数据覆盖copy给文件2,目标文件需要存在
例:
```python
import shutil #导包

f1 = open("1.txt",encoding="utf-8")

f2 = open("2.txt","w",encoding="utf-8")

shutil.copyfileobj(f1,f2)  #将f1中的数据覆盖f2中的数据

```

### 2.`shutil.copyfile(文件1，文件2)`：不用打开文件，直接用文件名进行覆盖copy。目标文件无需存在
```python
import shutil
shutil.copyfile("1.txt","3.txt")
```

###  3.`shutil.copymode(文件1，文件2)`：仅拷贝权限。 内容、组、用户均不变,  目标文件必须存在
原函数:
```python
def copymode(src,dst):
    """copy mode bits from src to dst"""
    if hasattr(os,'chmod'):
        st = os.stat(stc)
        mode = stat.S_IMODE(st.st_mode)
        os.chmod(dst,mode)
```
例:
```python
import os
import shutil
file='P:\\python程序\\哈哈.txt'  #有只读权限的文件
path='P:\\python程序\\file_path\\123.txt' #需要获取哈哈文件权限的文件
#shutil.copymode(文件1，文件2)  #伪代码
path_1=shutil.copymode(file,path)  #权限的更改
```
未执行时:

![哈哈文件的权限](https://upload-images.jianshu.io/upload_images/14555448-a6f1bc2bde3934f6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![哈哈文件的内容](https://upload-images.jianshu.io/upload_images/14555448-47820b886903f2af.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![123文件的权限](https://upload-images.jianshu.io/upload_images/14555448-f9bb52a04ab73c89.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![123文件的内容](https://upload-images.jianshu.io/upload_images/14555448-80ce5c93e65207bb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

执行程序后:
![123文件的权限发生了更改](https://upload-images.jianshu.io/upload_images/14555448-971e039c30e311ab.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![123文件的内容未发生变化](https://upload-images.jianshu.io/upload_images/14555448-80ce5c93e65207bb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 4.`shutil.copystat(文件1，文件)`：仅拷贝状态的信息，包括：mode bits, atime, mtime, flags,  目标文件必须存在
原函数:
```python
def copystat(src,dst):
    """将所有的状态信息(模式位、时间、时间、标志)从src复制到dst"""
    st = os.stat(src)
    mode = stat.S_IMODE(st.st_mode)
    if hasattr(os, 'utime'):
        os.utime(dst,(st.st_atime,st.st_mtime))
    if hasattr(os, 'chmod')
        os.chmod(dst,mode)
    if hasattr(os, 'chflags') and hasattr(st,'st_flags'):
        try:
            os.chflags(dst, st.st_flags)
        except OSError,why:
            for err in 'EOPNOTSUPP', 'ENOTSUP':
                if hasattr(errno,err) and why.errno == getattr(errno, err):
                    break
                else:
                    raise
```
执行之后只会改变权限,所属的

### 5.`shutil.copy(文件1，文件2)`：拷贝文件和权限都进行copy。目标文件不需要存在
原函数:
```python
def copy(src,dst):
    """copy data and mode bits ("cp src dst")
    The destination may be a directory.
    """
    if os.path.isdir(dst):
        dst = os.path.join(dst,os.path.basename(src))
        copyfile(src,dst)
        copymode(src,dst)
```
功能：拷贝文件和权限都进行copy。
格式：`shutil.copy('来源文件','目标地址')`
返回值：复制之后的路径
例:
```python
import os
import shutil
file='P:\\python程序\\哈哈.txt'  #文件路径
path='P:\\python程序\\file_path' #需要复制到的文件路径
#shutil.copy('来源文件','目标地址')  #伪代码
path_1=shutil.copy(file,path)  #进行文件的复制
print(path_1)  #打印返回值为文件的路径
```
执行结果:
```python
P:\python程序\file_path\哈哈.txt
```
### 6.`shutil.copy2(文件1，文件2)`：拷贝了文件和状态信息。目标文件不需要存在
### 7. `shutil.copytree(源目录，目标目录)`：可以递归copy多个目录到指定目录下。
使用方式:
```python
shutil.ignore_patterns(*patterns)
shutil.copytree(src, dst, symlinks=False, ignore=None)
```
使用方式:
```python
递归的去拷贝文件夹
import shutil
shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.pyc', 'tmp*')) #目标目录不能存在，注意对folder2目录父级目录要有可写权限，ignore的意思是排除 
```
# 例:目标目录不能存在,  `folder2='C:\\Users\\zangz\\Desktop\\123'` 这里的123文件夹不能存在
```python
#递归的去拷贝文件夹
folder1='P:\\python程序'
folder2='C:\\Users\\zangz\\Desktop\\123'
 
shutil.copytree(folder1, folder2, ignore=shutil.ignore_patterns('*.pyc', 'tmp*')) #目标目录不能存在，注意对folder2目录父级目录要有可写权限，ignore的意思是排除 
```

### 8. `shutil.rmtree(目标目录)`：可以递归删除目录下的目录及文件。
例:
```python
folder2='C:\\Users\\zangz\\Desktop\\123'
shutil.rmtree(folder2)
```
执行之后这个文件就会被删除, 但是注意的是有只读权限的删除不了
![image.png](https://upload-images.jianshu.io/upload_images/14555448-b27567341f2cdde2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![只读权限拒绝访问](https://upload-images.jianshu.io/upload_images/14555448-7b764a1ea9e393fa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 9. `shutil.move(源文件，指定路径)`：递归移动一个文件。
例:
```python
file='P:\\python程序\\哈哈.txt'  
folder2='C:\\Users\\zangz\\Desktop\\123'
shutil.move(file,folder2)
```
> 注意的是这里不能移动只读权限的文件,以及打开的文件

### 10.`shutil.make_archive()`：可以压缩，打包文件。
详细的解释:
**`shutil.make_archive(base_name, format,...)`**

创建压缩包并返回文件路径，例如：zip、tar

* base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
* 如 data_bak                       =>保存至当前路径
* 如：/tmp/data_bak =>保存至/tmp/
* format：	压缩包种类，“zip”, “tar”, “bztar”，“gztar”
* root_dir：	要压缩的文件夹路径（默认当前目录）
* owner：	用户，默认当前用户
* group：	组，默认当前组
* logger：	用于记录日志，通常是logging.Logger对象
例:

```python
folder1='P:\\python程序'
folder2='C:\\Users\\zangz\\Desktop\\123'
shutil.make_archive(folder1,"zip",folder2) #将folder中的文件压缩到P盘,名字为python程序,压缩的格式是zip
```
执行结果:
```python
'P:\\python程序.zip'   #这里返回的是压缩后的文件所在的路径
```

### shutil 对压缩包的处理是调用 ZipFile 和 TarFile 两个模块来进行的，详细：
`zipfile` 压缩解压
```python
import zipfile

# 压缩
z = zipfile.ZipFile('laxi.zip', 'w')
z.write('a.log')
z.write('data.data')
z.close()

# 解压
z = zipfile.ZipFile('laxi.zip', 'r')
z.extractall()
z.close()
```

`tarfile` 压缩解压
```python
import tarfile

# 压缩
tar = tarfile.open('your.tar','w')
tar.add('/Users/wupeiqi/PycharmProjects/bbs2.zip', arcname='bbs2.zip')
tar.add('/Users/wupeiqi/PycharmProjects/cmdb.zip', arcname='cmdb.zip')
tar.close()

# 解压
tar = tarfile.open('your.tar','r')
tar.extractall()  # 可设置解压地址
tar.close()
```
