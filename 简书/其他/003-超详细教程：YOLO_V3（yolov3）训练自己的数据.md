## 前言：
最近刚好做一个项目需要做detection，选择的算法是yolo v3，因为它既有速度又有精度，还非常灵活，简直是工业界良心。做项目免不了需要用到自己的数据集，所以得从头一个脚印的来，走通了之后决定写一个帖子，让需要用的人少走歪路，节约时间。
官网上已经教我们如何跑起来yolo v3，因此大部分时间其实花在制作数据集上。总体来说，分为四个步骤，分别是：标注数据，利用voc制作自己的数据集，下载并编译源码，局部修改和大功告成（前两步可以在方便操作的环境下（windows或linux）进行，后面几步在linux环境进行）

## 一、标注数据
### 1. 工具：
使用的标注工具是labelimg，其他标注工具也行，但是生成的标注label文件要是xml。这里给一个labelimg软件的传送门 https://pan.baidu.com/s/1tuIQmuyedRHP1WeGVVSx_Q 提取码: ejgx 。

### 2.数据集编号：
为了规划自己的数据，减少出错的可能性，最好自己先给自己的图片编一个合理的序号，比如0001~0999。

### 3.标注数据：
利用软件把自己的数据标注好。每一个图片名对应的有一个相应名字的label.xml。
![image.png](https://upload-images.jianshu.io/upload_images/14555448-f79ecbf6158483f9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
xml中的数据如下所示。这时候的path不用管他，在训练的时候不会用到这里的数据，这里后面会说到。
![image.png](https://upload-images.jianshu.io/upload_images/14555448-45e9ec05e692d4ad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
## 二、利用voc制作自己的数据集
在目录下新建VOC2007，并在VOC2007下新建Annotations，ImageSets和JPEGImages三个文件夹。在ImageSets下新建Main文件夹。文件目录如下所示：
![image.png](https://upload-images.jianshu.io/upload_images/14555448-cd53e732d44488c4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
将自己的数据集图片拷贝到JPEGImages目录下。将数据集label文件拷贝到Annotations目录下。在VOC2007下新建test.py文件夹，将下面代码拷贝进去运行，将生成四个文件：train.txt,val.txt,test.txt和trainval.txt。
```python
import os
import random

trainval_percent = 0.1
train_percent = 0.9
xmlfilepath = 'Annotations'
txtsavepath = 'ImageSets\Main'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('ImageSets/Main/trainval.txt', 'w')
ftest = open('ImageSets/Main/test.txt', 'w')
ftrain = open('ImageSets/Main/train.txt', 'w')
fval = open('ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()

```
生成后的目录结构如下所示：
![image.png](https://upload-images.jianshu.io/upload_images/14555448-71a01828ceebc727.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
## 三、下载并编译源码

YOLOV3的主页：[https://pjreddie.com/darknet/yolo/](https://pjreddie.com/darknet/yolo/)
1、下载代码：让它默认下载到home文件夹中就好(打开终端直接复制粘贴)
```python
git clone https://github.com/pjreddie/darknet
```
2、编译代码：
YOLOV3使用一个开源的神经网络框架Darknet53，使用C和CUDA，有CPU和GPU两种模式。默认使用的是CPU模式，需要切换GPU模型的话，vim修改Makefile文件。
```python
cd darknet
vim Makefile  #如果使用CPU模式。则不用修改Makefile文件
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-39d6fd6d5aea8171.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
将前面三行置1，其他不用动。
```python
make
```
编译成功后，可以先下载预训练模型测试一下效果。
下载模型(如果没有下载到darknet就将下载好的模型拖到这个文件夹中)
```bash
wget https://pjreddie.com/media/files/yolov3.weights
```
进入到darknet文件夹中
```bash
cd darknet
```
进行测试
```bash

./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg

 ```
测试的结果如下:
![image.png](https://upload-images.jianshu.io/upload_images/14555448-fac45c77abda7a7f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
可以看到YOLO的detection图。到这里，YOLOV3已经走通了，是时候加入自己的数据了。
### 3、加入自己的数据集
在代码的darknet目录下新建VOCdevkit文件夹，然后把刚才制作的VOC2007文件夹拷贝到该文件夹下。
有的读者可能了解过YOLOV3的label，YOLOV3的label标注的一行五个数分别代表类别（从 0 开始编号）， BoundingBox 中心 X 坐标，中心 Y 坐标，宽，高。这些坐标都是 0～1 的相对坐标。和我们刚才标注的label不同，因此我们需要下面的py文件帮我们转换label。

终端显示的路径在哪就下载到哪了

```python
wget https://pjreddie.com/media/files/voc_label.py
```
这里需要修改两个地方，sets和classes，classes根据自己需要修改。
![image.png](https://upload-images.jianshu.io/upload_images/14555448-4e9f11b16085b3b1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
接下来运行该文件，我们的目录下会生成三个txt文件2007_train.txt,2007_val.txt,2007_test.txt，VOCdevkit下的VOC2007也会多生成一个labels文件夹，下面是真正会使用到的label，点开看发现已经转化成YOLOV3需要的格式了。这时候自己的数据集正式完成。

```python
python voc_label.py
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-2e2740bd530d2884.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/14555448-7f64c4385a64bfdf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
## 四、局部修改
1、 修改cfg/voc.data
![image.png](https://upload-images.jianshu.io/upload_images/14555448-9693b3b0ddf84e59.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

根据自己的路径修改。

2、修改data/voc.names和coco.names
打开对应的文件都是原本数据集里的类，改成自己的类就行。
![image.png](https://upload-images.jianshu.io/upload_images/14555448-af018ff98981e59f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

3、修改参数文件cfg/yolov3-voc.cfg
ctrl+f搜 yolo, 总共会搜出3个含有yolo的地方。
每个地方都必须要改2处， filters：3*（5+len（classes））；
其中：classes: len(classes) = 1，这里以单个类dog为例
filters = 18
classes = 1
可修改：random = 1：原来是1，显存小改为0。（是否要多尺度输出。）
![image.png](https://upload-images.jianshu.io/upload_images/14555448-ba0ee1d1b1314d6c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
参数文件开头的地方可以选训练的batchsize，要注意！
![image.png](https://upload-images.jianshu.io/upload_images/14555448-7f6e11a43b5c071a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
## 五、大功告成
如果读者按照步骤已经耐心的到这里了，可以舒一口气了，离成功只差一步了。
下载darknet53的预训练模型。
