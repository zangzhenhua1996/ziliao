我们大部分日常的电脑系统都是windows，在windows下安装虚拟机工具大家基本上都是很常见的，也有部分系统安装的是linux，如ubuntu等，在这样的系统下安装虚拟机的话，首先需要安装虚拟机软件，如linux版的vmware、开源的virtualbox等。下面我们介绍一下如何在ubuntu系统下安装vmware工具。

1.首先，在vmware官网上下载linux版的vmware workstation。

https://my.vmware.com/en/web/vmware/info/slug/desktop_end_user_computing/vmware_workstation_pro/15_0

![image](https://upload-images.jianshu.io/upload_images/14555448-62961216fb08cabe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2、安装

　　准备工作中下载下来的Linux 版本VMware后缀是.bundle的，好奇怪，在Windows下都没见过这个。

　　1、把下载下来的VMware放在用户目录下，即跟桌面处于同一目录下，不然待会安装会出现“root access is required for the operations you have chosen”的错误。或者值直接在你的文件夹中打开终端.大家既然使用乌班图就不用我说了.

![image](https://upload-images.jianshu.io/upload_images/14555448-58dc303457b95964.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2、给VMware.bundle加可执行权限sudo chmod+x VMware.bundle(下载下来的文件名很长，建议改短，方便操作)

`sudo chmod +x VMware-Workstation-Full-15.0.2-10952284.x86_64.bundle`

![image](https://upload-images.jianshu.io/upload_images/14555448-28110b545f5f511b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

3、在终端中输入`sudo./VMware.bundle`，然后就会弹出图形化界面，安装过程就跟Windows下安装一样，中途会让你输入Key，

![image](https://upload-images.jianshu.io/upload_images/14555448-b86477fc4c4bec37.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image](https://upload-images.jianshu.io/upload_images/14555448-90d61e3e2bf5748a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

输入激活码随便百度一大堆.
```bash
YG5H2-ANZ0H-M8ERY-TXZZZ-YKRV8

UG5J2-0ME12-M89WY-NPWXX-WQH88

UA5DR-2ZD4H-089FY-6YQ5T-YPRX6

GA590-86Y05-4806Y-X4PEE-ZV8E0

ZF582-0NW5N-H8D2P-0XZEE-Z22VA

YA18K-0WY8P-H85DY-L4NZG-X7RAD
```
直接安装好了可能没法直接使用,因为没有GCC编译环境

那就安装一个就好了

在Ubuntu下安装GCC和其他一些Linux系统有点不一样。

方法一:

`sudo apt-get build-dep gcc`

我没有成功

方法二:

`sudo apt-get install build-essential`

这个成功了

安装完了可以执行如下的命令来查看版本，

`gcc --version`

![image](https://upload-images.jianshu.io/upload_images/14555448-69b111d3cf0805f1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

然后就可以正常的使用了:

![image](https://upload-images.jianshu.io/upload_images/14555448-d6adc8d24c58d40a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

开心的燥起来吧
