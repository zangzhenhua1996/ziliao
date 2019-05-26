问题描述：

分区格式化的时候不小心删除了引导分区,开机就是grub界面,只能修复引导了

解决方案：

1.制作一个U盘启动盘。下载对应的ubuntu系统，用rufus工具制作Ubuntu U盘启动。

2.打开电脑后选择u盘启动盘，然后选择try ubuntu without install。试用不安装。

3.进入ubuntu系统后，连接好网络，打开终端，输入下面命令，按照提示操作。

```sudo add-apt-repository ppa:yannubuntu/boot-repair && sudo apt-get update  ```

4.完成后，终端中输入下面命令：

```sudo apt-get install -y boot-repair && boot-repair  ```

会出现如下界面，选择recommended repair

![image](https://upload-images.jianshu.io/upload_images/14555448-7c09946eb0e10c34.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

5.按照boot repair提示的操作进行，完成后重启电脑即可完成。
