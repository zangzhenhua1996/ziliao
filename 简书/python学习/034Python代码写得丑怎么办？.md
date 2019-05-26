一、Jupyter notebook 篇Jupyter notebook的代码要想写得规范，推荐用`Code prettify`插件。安装插件首先插件Nbextensions执行以下命令
```bash
pip install jupyter_contrib_nbextensions
````
无报错再执行：
```bash
jupyter contrib nbextension install --user
```
选取`Code prettify`模块
*备注：需要安装 yapf模块*
   ```bash
pip install yapf
```
安装完成后打开jupyter notebook
1 打开编辑
![image.png](https://upload-images.jianshu.io/upload_images/14555448-7334d65f6a994eb0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2 点开 nbxtensions config
![image.png](https://upload-images.jianshu.io/upload_images/14555448-fbaec534c207c48c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
3 选中code pretlity 
![](https://upload-images.jianshu.io/upload_images/14555448-825b2f16474e8180.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
4 返回代码界面刷新一下就可以看到代码整理工具:
![image.png](https://upload-images.jianshu.io/upload_images/14555448-b3f42e5ed80871fe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
是个小锤子,只要书写完代码点击一下就可以了.
比如一开始写的代码是这样的:
![image.png](https://upload-images.jianshu.io/upload_images/14555448-b79f68a8d4d2c530.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
整理完成后就会变成这样的
![image.png](https://upload-images.jianshu.io/upload_images/14555448-ec2fa3995bfd11d4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
再也不怕写的代码丑了
代码不规范,同事两行泪,哈哈
