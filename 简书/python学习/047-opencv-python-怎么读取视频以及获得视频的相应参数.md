# opencv-python 怎么读取视频以及获得视频的相应参数

在做基于视频的深度学习，需要对视频数据进行切割处理，刚敲了三行代码就卡在了如何获得视频属性的坎上，记录一下免得自己下次要用又忘记了。

先放上opencv2.4的官方文档链接: https://docs.opencv.org/2.4/index.html

下面是代码例子

```python

import cv2  #导入opencv的包
 
cap=cv2.VideoCapture(path) #调用VideoCapture函数获取视频的各项信息,path是路径

frames_num=cap.get(7)#get方法参数按顺序对应下表（从0开始编号，比如这里为了获取视频的总帧数，在下表是排第八个的CV_CAP_PROP_FRAME_COUNT


```

## #下面是各种参数的信



- **0 CV_CAP_PROP_POS_MSEC**      	 视频文件的当前位置（毫秒）或视频捕获时间戳。
- **1 CV_CAP_PROP_POS_FRAMES**       下一步要解码/捕获的帧的索引
- **2 CV_CAP_PROP_POS_AVI_RATIO**       视频文件的相对位置：0-电影开始，1-电影结束。
- 3 **CV_CAP_PROP_FRAME_WIDTH**      视频流中帧的宽度。
- 4 **CV_CAP_PROP_FRAME_HEIGHT**       视频流中帧的高度。
- 5 **CV_CAP_PROP_FPS**        帧速率。
- 6**CV_CAP_PROP_FOURCC**     编解码器的4字符代码
- 7 **CV_CAP_PROP_FRAME_COUNT**     视频文件中的帧数。
- 8 **CV_CAP_PROP_FORMAT**     返回的mat对象的格式。
- 9 **CV_CAP_PROP_MODE**     后端特定值，指示当前捕获模式。
- 10 **CV_CAP_PROP_BRIGHTNESS**    图像亮度（仅适用于相机）
- 11**CV_CAP_PROP_CONTRAST**      图像对比度（仅适用于相机）。
- 12 **CV_CAP_PROP_SATURATION**     图像饱和度（仅适用于相机）。
- 13 **CV_CAP_PROP_HUE**                 图像色调（仅适用于相机）。
- 14 **CV_CAP_PROP_GAIN**                 图像增益（仅适用于相机）。
- 15 **CV_CAP_PROP_EXPOSURE**               曝光（仅适用于相机）。
-  16 **CV_CAP_PROP_CONVERT_RGB**            指示图像是否应转换为rgb的布尔标志。
-  17 **CV_CAP_PROP_WHITE_BALANCE_U**         白平衡设置的u值（注：目前仅支持dc1394 v 2.x后端）
- 18 **CV_CAP_PROP_WHITE_BALANCE_V**           白平衡设置的v值（注：目前仅支持dc1394 v 2.x后端）
- 19 **CV_CAP_PROP_RECTIFICATION**            立体摄像机校正标志（注：目前仅支持DC1394 v 2.x后端）
- 20 **CV_CAP_PROP_ISO_SPEED**              相机的iso速度（注：目前只有dc1394 v 2.x后端支持）
- 21 **CV_CAP_PROP_BUFFERSIZE**           存储在内部缓冲区内存中的帧数量（注意：目前只有dc1394 v 2.x后端支持）
