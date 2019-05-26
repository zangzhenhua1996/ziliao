win10系统怎么禁用defender？Windows Defender是自带杀毒软件，但是对于某些第三方软件的使用者或者不喜欢安装杀毒软件的用户怎么禁用它成为了难题。其实禁用defender的方法有很多种，下面跟随小编我一起往下边来看看win10系统禁用defender的方法。

方法一，通过Windows Defender设置临时关闭

1，打开Windows Defender操作界面，依次打开“病毒和威胁防护”-“病毒和威胁防护设置”；

![win10系统禁用defender的三种方法【图文】](http://upload-images.jianshu.io/upload_images/14555448-ca9e63958ca84326.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240 "win10系统禁用defender的三种方法【图文】")

2，在“病毒和威胁防护”设置界面，关闭“实时保护”，关闭“云提供的保护”，关闭“自动提交样本”这三项。

如果按钮是灰色无法修改，那么可能你的第三方软件已通过其他方式为您已经关闭了。

![win10系统禁用defender的三种方法【图文】](http://upload-images.jianshu.io/upload_images/14555448-4131a70c6bcd6f9e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240 "win10系统禁用defender的三种方法【图文】")

方法2：通过修改注册表，永久禁用Windows Defender1，打开注册表编辑器。

按 Win +R键入regedit，点击确定。

![win10系统禁用defender的三种方法【图文】](http://upload-images.jianshu.io/upload_images/14555448-d93f4a67d166c764.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240 "win10系统禁用defender的三种方法【图文】")

2，定位需要修改的注册表其路径如下HKEY_LOCAL_MACHINE \ SOFTWARE \ Policies \ Microsoft \ Windows Defender。

![win10系统禁用defender的三种方法【图文】](http://upload-images.jianshu.io/upload_images/14555448-871e44746c2946e3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240 "win10系统禁用defender的三种方法【图文】")

3，创建DWORD（32位）注册表值；

右侧空白区域右键-新建-DWORD（32位）值，命名它为DisableAntiSpyware。

修改数值为1，因0代表启用，1代表禁用。

点确定关闭注册表。

重启电脑Windows Defender已经不会在开机启动了。

![win10系统禁用defender的三种方法【图文】](http://upload-images.jianshu.io/upload_images/14555448-06eba48e33cacc93.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240 "win10系统禁用defender的三种方法【图文】")

方法3：通过组策略禁用Windows Defender1，打开本地组策略编辑器应用程序

还是按下Win+R键，输入gpedit.msc，打开组策略窗口。

![win10系统禁用defender的三种方法【图文】](http://upload-images.jianshu.io/upload_images/14555448-8a279233a2307b23.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240 "win10系统禁用defender的三种方法【图文】")

2，找到windows Defender选项管理模板-windows组件-windows defender防病毒程序，

![win10系统禁用defender的三种方法【图文】](http://upload-images.jianshu.io/upload_images/14555448-06570730d822f9c5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240 "win10系统禁用defender的三种方法【图文】")

3，在右侧选择关闭windows defender防病毒程序，打开 选择 启用，确定！

如果没有立刻关闭，请重启电脑或者刷新策略组。

注意：禁用的运行WD，启用才是关闭。

![win10系统禁用defender的三种方法【图文】](http://upload-images.jianshu.io/upload_images/14555448-7510fee8b69604ce.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240 "win10系统禁用defender的三种方法【图文】")

以上就是win10系统禁用defender的三种方法，选择一款你习惯的方法关闭，希望能够帮助到大家。