# python glob model

说明：

### 1、glob是python自己带的一个文件操作相关模块，用它可以查找符合自己目的的文件，就类似于Windows下的文件搜索，支持通配符操作: * , ? , [], 这三个通配符，*代表0个或多个字符，?代表一个字符，[]匹配指定范围内的字符，如[0-9]匹配数字。

### 它的主要方法就是glob, 该方法返回所有匹配的文件路径列表，该方法需要一个参数用来指定匹配的路径字符串（本字符串可以为绝对路径也可以为相对路径），其返回的文件名只包括当前目录里的文件名，不包括子文件夹里的文件。

####比如：
```python
import glob
glob.glob(r'K:\python程序\*.txt')
```
> 这里就是获得`K:\python程序\` 路径下的所有txt文件
执行结果:
```python
['K:\\python程序\\123.txt', 'K:\\python程序\\哈哈1.txt']
```  
> 以列表的形式返回

```python
glob.glob(r'E:\pic\*\*.jpg')
```
获得指定目录下的所有jpg文件

使用相对路径：
```python
glob.glob(r'../python程序/*.py')
```
执行结果:
```python
['../python程序\\copy筛选的文件.py',
 '../python程序\\glob模块的使用.py',
 '../python程序\\MP3到wav格式的转换.py',
 '../python程序\\shutil模块的使用.py',
 '../python程序\\wav转换.py',
 '../python程序\\合并std的文字.py',
 '../python程序\\循环copy文件.py',
 '../python程序\\循环读取行并写入新的文办.py',
 '../python程序\\批量对应重命名.py',
 '../python程序\\批量建立文件.py',
 '../python程序\\文件合并.py',
 '../python程序\\文件名的处理.py',
 '../python程序\\获取当前目录下的所有的文件名,以及子目录所有文件名.py',
 '../python程序\\词频切割.py',
 '../python程序\\词频反正排序.py',
 '../python程序\\读取文件的绝对路径.py',
 '../python程序\\音频整段剪切.py']
```
### 2、`iglob`方法：

#### 获取一个可遍历对象，使用它可以逐个获取匹配的文件路径名。与glob.glob()的区别是：glob.glob同时获取所有的匹配路径，而 glob.iglob一次只获取一个匹配路径。这有点类似于.NET中操作数据库用到的DataSet与DataReader。下面是一个简单的例子：
```python
#父目录中的.py文件
f = glob.iglob(r'../python程序/*.py')
print (f) 
for py in f:
    print (py)
```
执行结果:
```python
<generator object _iglob at 0x0000018EABD605E8>
../python程序\copy筛选的文件.py
../python程序\glob模块的使用.py
../python程序\MP3到wav格式的转换.py
../python程序\shutil模块的使用.py
../python程序\wav转换.py
../python程序\合并std的文字.py
../python程序\循环copy文件.py
../python程序\循环读取行并写入新的文办.py
../python程序\批量对应重命名.py
../python程序\批量建立文件.py
../python程序\文件合并.py
../python程序\文件名的处理.py
../python程序\获取当前目录下的所有的文件名,以及子目录所有文件名.py
../python程序\词频切割.py
../python程序\词频反正排序.py
../python程序\读取文件的绝对路径.py
../python程序\音频整段剪切.py
```
