1.set函数:  https://www.cnblogs.com/hukey/p/9242339.html
```python
nums=set([1,1,2,5,8])
print(len(nums))
```
执行结果:
```python
4
```
> 解析:
set 类型的特性是会移除集合中重复的元素，因此变量 nums 实际上等于：
nums = {1, 2, 5, 8}

2. 逻辑运算和比较运算:
下列代码运行结果是？ 
```python
a = 'a'
print (a > 'b' or 'c')
```
执行结果:
```python
c
```
>解析:
由于比较运算符优先级大于逻辑运算符，根据上表，当 a > 'b'，即 'a' > 'b' 为 Fasle 时（'a' 的 ASCII 码比 ‘b’ 小），返回值为 'c '(True)，   False or True 返回的是True的那个故答案选C。

3. 复数:
![image.png](https://upload-images.jianshu.io/upload_images/14555448-fb2aac83dbf351b7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
4 .Python函数
![image.png](https://upload-images.jianshu.io/upload_images/14555448-b0e7386c9071dd2f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

>解析:  https://www.cnblogs.com/smallmars/p/6936871.html
在 Python 中万物皆为对象，函数也不例外，函数作为对象可以赋值给一个变量、可以作为元素添加到集合对象中、可作为参数值传递给其它函数，还可以当做函数的返回值，这些特性就是第一类对象所特有的。
