** 在ubuntu16.04上安装eclipse**

**一、下载**

   首先我们需要[安装jdk1.8](http://www.cnblogs.com/zyrblog/p/8510132.html)及其以上，然后从[官网](https://www.eclipse.org/downloads/)：https://www.eclipse.org/downloads/上下载，需要注意的是官网的服务器太差，响应的速度非常慢，需要读者有点耐心，哈哈~~~然后选择第一个，就是我们要安装的eclipse的JDE了。**

![image.png](https://upload-images.jianshu.io/upload_images/14555448-df1edff9688ed43c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**点击下载按钮，将会下载相应的位数和版本的eclipse：**

![image.png](https://upload-images.jianshu.io/upload_images/14555448-70bc47a0dddcc076.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


**二、安装** 

**然后找到下载的文件：**

**![image](http://upload-images.jianshu.io/upload_images/14555448-21b341f363585887.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)** 

**对下载的文件进行解压到相关目录，然后重命名，赋予权限，之后我们进入该文件夹之中，使用其中的./eclipse-inst来启动安装程序，如果只是普通的开发我们选择第一个就可以了：**

```bash
 sudo mv eclipse  /opt
```


### 四 创建eclipse installer桌面快捷图标

*   首先输入指令： **cd /usr/share/applications**
*   然后输入指令： **sudo gedit eclipseinstall.desktop** 

*   最后将下面的代码复制到文件中： 
```bash
[Desktop Entry]
Encoding=UTF-8
Name=Eclipseinstall
Comment=Eclipse
Exec=/opt/eclipse/eclipse-inst
Icon=/opt/eclipse/icon.xpm
Terminal=false
StartupNotify=true
Type=Application
Categories=Application;Development;
```
    **其中“Exec=”后面为eclipse安装目录下的eclipse程序的位置路径，“Icon=”后面为eclipse安装目录下的图标图片的路径** 

3.3 将eclipse变为可执行文件
指令为：sudo chmod u+x eclipse.desktop 


五：启动eclipse 的安装器



![image.png](https://upload-images.jianshu.io/upload_images/14555448-ea8810ce5d7536f4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




选择第一项进行安装

安装完成后将原来的eclipse快捷方式重新修改
```bash
[Desktop Entry]
Encoding=UTF-8
Name=Eclipse
Comment=Eclipse
Exec=/home/dlut/eclipse/java-2019-03/eclipse/eclipse
Icon=/home/dlut/eclipse/java-2019-03/eclipse/icon.xpm
Terminal=false
StartupNotify=true
Type=Application
Categories=Application;Development;
```