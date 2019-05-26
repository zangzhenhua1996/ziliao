1、  输入命令：
```bash
xrandr
```
将会出现当前设备有效的输入设备名称:比如我的就是DP-2
```bash
Screen 0: minimum 320 x 200, current 1024 x 768, maximum 16384 x 16384
DP-1 disconnected (normal left inverted right x axis y axis)
DP-2 connected primary 1024x768+0+0 (normal left inverted right x axis y axis) 0mm x 0mm
   1024x768      60.00* 
   800x600       60.32    56.25  
   848x480       60.00  
   640x480       59.94  
```



 

2、  上图中就没有我要使用的1440X900，分辨率，所以我要手动添加一个1080P的分辨率，先输入“cvt 1440 900”命令，查询一下1080P分辨率的有效扫描频率，如下图所示

```bash
# 1440x900 59.89 Hz (CVT 1.30MA) hsync: 55.93 kHz; pclk: 106.50 MHz
Modeline "1440x900_60.00"  106.50  1440 1528 1672 1904  900 903 909 934 -hsync +vsync
```

3、  然后通过
```bash
sudo xrandr --newmode "1440x900_60.00"  106.50  1440 1528 1672 1904  900 903 909 934 -hsync +vsync
```
命令新建一种输出分辨率，如下图



4、  把新建的输出分辨率输出到当前设备上

执行命令：
```bash
sudo xrandr --addmode DP-2 "1440x900_60.00"

```
注：这里我的设备为DVI-0 ，可根据你设备名来进行更换

 

5、  把当前分辨率设置为刚添加的1080p分辨率

执行命令：sudo xrandr --output DP-2 --mode "1440x900_60.00"


注：此处的DVI-0 根据你的情况进行更改

6、  使每次启动生效，修改配置文件

执行命令：sudo gedit ~/.profile

在文件的后面添加这些语句：

```bash
cvt 1440 900
xrandr --newmode "1440x900_60.00"  106.50  1440 1528 1672 1904  900 903 909 934 -hsync +vsync
xrandr --addmode DP-2 "1440x900_60.00"
xrandr --output DP-2 --mode "1440x900_60.00"
```
7、  重启电脑试试分辨率是否正常


