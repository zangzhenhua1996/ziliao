ubuntu怎么切换到root用户，我们都知道使用su root命令，去切换到root权限，此时会提示输入密码，可是怎么也输不对，提示“Authentication failure”，

此时有两种情况一个是真的是密码错了，另一种就是刚安装好的Linux系统，没有给root设置密码。

通过下文就可以解决这两个问题。

打开Ubuntu，输入命令：`su root`，回车提示输入密码，怎么输入都不对

![image.png](https://upload-images.jianshu.io/upload_images/14555448-f375e886e9e65f2a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

给root用户设置密码：

命令：`sudo passwd root`

输入密码，并确认密码。
![image.png](https://upload-images.jianshu.io/upload_images/14555448-b242d793b98269a6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

重新输入命令：`su root`

然后输入密码：

发现可以切换到root权限了。
![image.png](https://upload-images.jianshu.io/upload_images/14555448-ea23c57d899defd3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
使用`su xyx`命令，切换到普通用户。
![image.png](https://upload-images.jianshu.io/upload_images/14555448-4cfa25add6e1b5f4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
