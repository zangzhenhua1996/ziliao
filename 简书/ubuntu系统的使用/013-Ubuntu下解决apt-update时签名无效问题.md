Ubuntu 18.04在执行`apt-get update`时出现一下报错：

![image](https://upload-images.jianshu.io/upload_images/14555448-de1a7d6a83954525.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

解决办法：

`sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8C718D3B5072E1F5`

`sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 58712A2291FA4AD5`

![image](https://upload-images.jianshu.io/upload_images/14555448-80a273f07de98b34.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
