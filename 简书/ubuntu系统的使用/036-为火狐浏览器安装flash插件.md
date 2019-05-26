1.到aodbe官方下载软件包，get.aodbe.com/flash，如图1；选择我们需要的软件包，一般选择选者.tar.gz包，如图2；点下载。

![image](https://upload-images.jianshu.io/upload_images/14555448-c872568986773bdb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image](https://upload-images.jianshu.io/upload_images/14555448-5957c98fe575cdb0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2.打开终端，快捷键Ctrl+Alt+T，输入命令“ls”会给你列出主目录下的所有文件及文件夹；

默认下载为Downloads, 输入命令“ cd Downloads ”,切换到Downloads文件夹，

再次“ls”,看到我们刚才下载的Flash插件包。如图3，4所示。输入命令  tar-zxvf  软件包名字   ”（Ubuntu终端有个小tip,当文件夹里只有很少类似名字的文件时，输入某文件夹的前几个字母然后 Tab，就会帮你输入全程，非常方便）。

![image](https://upload-images.jianshu.io/upload_images/14555448-3d0045cb2e623f0f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image](https://upload-images.jianshu.io/upload_images/14555448-cc2c56387a9654e1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

3.解压后如图5；我们要做的就是把图5中红色框里的文件复制到火狐浏览器的插件目录，

切换到终端，输入命令“ls”，如图6；输入命令“sudo cp libflashplayer.so

/usr/lib/mozilla/plugins/ ”

（这里需要管理员权限，所以会让你输入一次密码，密码不显示的，你只要确保你输入对了，回车键就OK了）

![image](https://upload-images.jianshu.io/upload_images/14555448-a14293b061133f89.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

.

![image](https://upload-images.jianshu.io/upload_images/14555448-a9403ad94bd0e632.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

4.然后命令行继续输入命令  “sudo cp -r  ./usr/*/usr/”   将usr目录下的所有文档拷贝到系统的/usr目录下，

如果不带sudo 那会提示你权限不够.到此安装完成，重启浏览器，再打开视频网站就可以愉快的播放了；如图7所示。

![image](https://upload-images.jianshu.io/upload_images/14555448-d8adfbddb28b2bc8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

5.学完有点难的，最后给大家说个简单的吧，Ubuntu系统自带的软件中心，

打开搜索，关键字“Flash”,点击安装，等待结束，重启浏览器，一样能达到上面的效果。

不过这里只所以最后说因为我们是天朝特色，使用这个软件中心装东西非常慢，至于有多慢，哈，你试过就知道了～！
