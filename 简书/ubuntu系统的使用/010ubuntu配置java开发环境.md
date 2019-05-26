##JDK安装及配置
###jdk1.8.0_201  下载
####下载后缀名为.tar.gz的软件包： jdk-8u201-linux-x64.tar.gz
####下载的地址为: [https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
![image.png](https://upload-images.jianshu.io/upload_images/14555448-ca1e9044e3ba3981.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###解压并安装
解压下载的文件，并移动解压后的软件包至/usr/lib完成安装。库目录中，/lib是内核级别的，/usr/lib是系统级别的，/usr/local/lib是用户级别的，后两者均可放置jdk，建议放在/usr/lib。
```
tar -zxvf jdk-10.0.1_linux-x64_bin.tar.gz
sudo mv jdk-10.0.1 /usr/lib/
```
###环境变量配置:
修改全局配置文件，作用于所有用户：(不是很建议,建议第二种配置方法)

####这里使用gedit，vim同理
```sudo gedit /etc/profile```
  ####或者修改当前用户配置文件，作用于当前用户(建议使用)：

```sudo gedit ~/.bashrc```

 #### 在文件中添加：
```
export JAVA_HOME=/usr/lib/jdk1.8.0_201
export CLASSPATH=.:${JAVA_HOME}/lib
export PATH=.:${JAVA_HOME}bin:$PATH
```
 ##注意: 环境变量中的路径和实际路径一致。

  ####使修改的配置生效：

#####二选一，视上文决定
```source /etc/profile```
或者
```source ～/.bashrc```

  ###最后检查安装结果

java -version

![image.png](https://upload-images.jianshu.io/upload_images/14555448-a4b8e78e205a48ad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#可以使用了,还是在linux下配置环境方便阿
