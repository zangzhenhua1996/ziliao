一直苦于python在执行for循环的过程中只能使用print(i)打印执行的效果是什么样子,可是真的不方便
今天就来试一下python中这个可以显示进度的`tqdm`包
`tqdm`是一个显示工作进度的模块,其实就是我们在安装python的扩展包的使用常见的进度条
# 语法：` tqdm(iterator)` 括号里面是一个可迭代的对象

## 默认设置打印进度
```python
from tqdm import tqdm
import time

for i in tqdm(range(10000)):  #将range迭代器放到了tqdm中
    time.sleep(0.01)
```
**看一下效果是这样的:**
![image.png](https://upload-images.jianshu.io/upload_images/14555448-9b38f9af4fc20f09.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 自定义格式
```python
from tqdm import tqdm
import time

pbar = tqdm(["a","b","c","d"])  #首先使用tqdm定义了一个迭代器
for char in pbar:
    time.sleep(5)
    #设置进度显示的名称使用的是set_description(设置描述):进程的名字.
    pbar.set_description("processing {}".format(char))  

```
效果是这样子的: 注意名称的变化
![image.png](https://upload-images.jianshu.io/upload_images/14555448-1f3d2eac3e69acd3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/14555448-824904387391cc80.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 手动控制更新的进度（按时间控制）
```python
from tqdm import tqdm
import time
#放到with中设置总得进度是100,
#然后for循环总共迭代20,那么就让tqdm每次更新进度为5循环完了进度就成为100
with tqdm(total=100) as pbar:  
    for i in range(20):
        time.sleep(0.2)
        pbar.update(5)
```
或者使用这种格式
```python
from tqdm import tqdm
import time

# 或者这样跟使用with的形式其实是一样的,
#我更喜欢这种方式,不过最后需要将定义的这个进度关闭
pbar = tqdm(total=100)
for i in range(20):
    time.sleep(0.2)
    pbar.update(5)
pbar.close()

```
效果都是一致的:
![image.png](https://upload-images.jianshu.io/upload_images/14555448-33ea0ea4c0f2cee7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
