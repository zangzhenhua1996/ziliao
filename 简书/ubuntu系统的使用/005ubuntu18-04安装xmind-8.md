###1: [XMind_8 linux客户端官网下载](https://www.xmind.cn/xmind/downloads/xmind-8-update8-linux.zip)
###[XMind_8百度云下载——提取码: m55v](https://pan.baidu.com/s/1qn8NaqKMJ7uBuTC9y7JcvA)

###2:  替换脚本: [XMind_amd64.tar.gz](https://pan.baidu.com/s/1pijGyVHFfO1BlDx-ZhtI5g)(提取码: tnkb) -- 包含`XMindCrack.jar`, `XMind.ini`

###3解压客户端到指定目录/opt
```bash
sudo mkdir /opt/XMind_8
sudo chown lwwen:lwwen /opt/XMind_8
unzip ~/Downloads/xmind-8-update8-linux.zip -d /opt/XMind_8
```
###4将### [XMind_amd64.tar.gz](https://pan.baidu.com/s/1pijGyVHFfO1BlDx-ZhtI5g)这个文件解压并将包含的两个文件放到这个文件中.

![image.png](https://upload-images.jianshu.io/upload_images/14555448-4c6e0f83acba230d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


###5 在hosts文件中添加127.0.0.1 [www.xmind.net](http://www.xmind.net/)
```bash
# XMind_8
127.0.0.1 www.xmind.net
```
### 6 打开xmind 8 输入邮箱和序列号
####帮助->序列号

####邮箱：x@iroader.me

####序列号：
```
XAka34A2rVRYJ4XBIU35UZMUEEF64CMMIYZCK2FZZUQNODEKUHGJLFMSLIQMQUCUBXRENLK6NZL37JXP4PZXQFILMQ2RG5R7G4QNDO3PSOEUBOCDRYSSXZGRARV6MGA33TN2AMUBHEL4FXMWYTTJDEINJXUAV4BAYKBDCZQWVF3LWYXSDCXY546U3NBGOI3ZPAP2SO3CSQFNB7VVIY123456789012345
```
###7 重启，完成。


###8 创建一个启动器
####建立运行脚本： 
```bash
cd /opt/xmind_8/XMind_amd64
```   
 转到指定的解压目录下。 
```bash
sudo gedit run.sh
 ```  
建立脚本文件 
在文件中输入下面的内容：
```bash
cd /opt/xmind_8/XMind_amd64
/opt/xmind_8/XMind_amd64/XMind
```
注意，上述的脚本内容需要根据自己实际解压目录的情况而定，这是我自己的目录。这是我在自己的家目录下确定的。第一行必须要有，也就是说，我们必须转到XMind运行文件所在的目录，才能正确运行，否则会报错！！ 
在完成文件的编辑后，输入  ```chmod +x ./run.sh```

#### 建立desktop文件
####建立文件之前，自己去百度一个喜欢的图标，作为XMind快捷方式的图标。
![image](http://upload-images.jianshu.io/upload_images/14555448-c1b4bdc8ddf9b1e7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

 ###输入命名：
   ```cd /usr/share/applications```   转到建立运行程序的目录
    ```sudo gedit xmind.desktop``` 建立图标，xmind是可以自己命名的
    在文件中输入：

```bash
[Desktop Entry] 
Name=XMind 
Exec=/opt/xmind_8/XMind_amd64/run.sh
Icon=/opt/xmind_8/XMind_amd64/xmind.png
Type=Application
Categories=GTK;GNOME;Office; 
```

Exec=后面是我们之前建立脚本的目录
Icon=后面是自己定义的图标的目录
Type=Application 说明这是一个应用程序
Categories=GTK;GNOME;Office; Office表示所属的大目录是Office的分类，大家可以根据实际情况具体更改。

> **注意**，此时需要从/usr/share/applications/文件夹中双击xmind.desktop，才能在按下super键（即Windows的Win键）后，键入xmind可以找到快速启动方式。
