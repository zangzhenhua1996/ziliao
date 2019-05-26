[转载自](https://www.jianshu.com/p/b416d5617b0c)
# 语谱图，滤波器组（Filter banks、MFCC）



> [Speech Processing for Machine Learning: Filter banks, Mel-Frequency Cepstral Coefficients (MFCCs) and What's In-Between （2016.4）](https://links.jianshu.com/go?to=https%3A%2F%2Fhaythamfayek.com%2F2016%2F04%2F21%2Fspeech-processing-for-machine-learning.html)

> [MFCC特征提取（知乎）-demo操作](https://links.jianshu.com/go?to=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F27416870)

> **语谱图**（语音频率图，时频图）**：**
>
> 频谱只能表示一小段声音。如果想观察一整段语音信号的频域特性，我们可以把一整段语音信号截成许多帧，把它们各自的频谱“竖”起来（即用纵轴表示频率），用颜色的深浅来代替频谱强度，再把所有帧的频谱横向并排起来（即用横轴表示时间），就得到了语谱图，它可以称为声音的时频域表示。

> ​       机器学习第一步是特征提取，语音领域也不例外。目前使用最多的莫过于Filter banks和MFCC，两者整体相似，MFCC多了一步DCT（离散余弦变换）。       
>
> ​       就目前来说，用的多得是Fbank，因为fbank的信息多余MFCC，MFCC多了一步DCT，某种程度上是对语音信息的损变，而且因为多了一步，计算量更大。



![“MFCC=Fbank+DCT”](https://upload-images.jianshu.io/upload_images/13931179-449ce9ced97b479b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/453/format/webp)



### 1、预处理

> **1.1、预加重、预增强：**
>
> 预增强以帧为单位进行，目的在于加强高频。去除口唇辐射的影响，增加语音的高频分辨率。因为高频端大约在800Hz以上按6dB/oct (倍频程)衰减，频率越高相应的成分越小，为此要在对语音信号进行分析之前对其高频部分加以提升，也可以改善高频信噪比。 
>
> 经预加重后的结果为：   $s ( x ) = s ( x ) - k * s ( x - 1 ) \quad \forall x \in \mathbb { X }$

> k是预增强系数，范围为[0, 1)，常用0.97，x是提取的wav时域数组的项，从公式可以看出每一帧的第一个数需要特殊处理。 



![](https://upload-images.jianshu.io/upload_images/13931179-95de1292858ca1ec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/382/format/webp)

> **1.2、分帧：**
>
> 分帧是将不定长的音频切分成固定长度的小段。为了避免窗边界对信号的遗漏，因此对帧做偏移时候，帧间要有帧迭(帧与帧之间需要重叠一部分)。通常的选择是帧长25ms（下图绿色），帧移为10ms（下图黄色）。接下来的操作是对单帧进行的。要分帧是因为语音信号是快速变化的，而傅里叶变换适用于分析平稳的信号。帧和帧之间的时间差常常取为10ms，这样帧与帧之间会有重叠（下图红色），否则，由于帧与帧连接处的信号会因为加窗而被弱化，这部分的信息就丢失了。



![](https://upload-images.jianshu.io/upload_images/13931179-0bdcf5b3392aeb7f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/771/format/webp)

> **1.3、加窗：**
>
> 傅里叶变换要求输入信号是平稳的，但是语音信号从整体上来讲是不平稳的。每帧信号通常要与一个平滑的窗函数相乘，让帧两端平滑地衰减到零，这样可以降低傅里叶变换后旁瓣的强度，取得更高质量的频谱  。
>
> 虽然语音信号具有时变特性，但是在一个短时间范围内（一般认为在10~30ms，即帧长），其特性基本保持不变即相对稳定，因而可以将其看作是一个准稳态过程，即语音信号具有短时平稳性。常用的窗函数有汉宁窗、汉明窗、矩形窗等，根据窗函数的频域特性，常采用**汉明窗**，其对应的窗函数如下： 



$w ( n ) = \left\{ \begin{array} { l l } { 0.54 - 0.46 \cos [ 2 \pi n / ( N - 1 ) ] , } & { 0 \leq n \leq N } \\ { 0 } \end{array} \right.$

> 注意：预增强和加窗同时使用时，要首先进行预增强 

> **1.4、添加随机噪声：**
>
> 有时候我们需要进行数据增强，会手动合成一些音频。某些人工合成(使用软件)的音频可能会造成一些数字错误，诸如underflow或者overflow。 这种情况下，通过添加随机噪声可以解决这一类问题。公式如下：    $  w ( n ) = w ( n ) + q * \text { rand } ( ) $
q 用于控制添加噪声的强度，rand() 产生[-1.0, 1.0)的随机数。

### 

### **2、提取Fbank特征**

> ​        人耳对声音频谱的响应是非线性的，经验表明：如果我们能够设计一种前端处理算法，以类似于人耳的方式对音频进行处理，可以提高语音识别的性能。FilterBank就是这样的一种算法。FBank特征提取要在预处理之后进行，这时语音已经分帧，我们需要逐帧提取FBank特征。

> **2.1、快速傅里叶变换fft**
>
> 我们分帧之后得到的仍然是时域信号，为了提取fbank特征，首先需要将时域信号转换为频域信号。傅里叶变换可以将**信号从时域转到频域**。因为我们用的是数字音频（而非模拟音频），所以我们用到的是离散傅里叶变换。我们现在可以在每一帧上做N点FFT来计算频谱，也称为短时傅里叶变换(Short-Time Fourier-Transform, STFT)，其中N通常为256或512,NFFT = 512.
>
> ​  $ P = \frac { \left| F F T \left( x _ { i } \right) \right| ^ { 2 } } { N } $
$x_i$为信号$x$的第$i$帧

> **2.2、Mel滤波器组**
>
> Mel滤波的过程如下图：
>其中$Hertz(f)$and $Mel(m)$
>
> $\begin{array} { c } { m = 2595 \cdot \log _ { 10 } \left( 1 + \frac { f } { 700 } \right) } \\ { f = 700 \left( 10 ^ { m / 2595 } - 1 \right) } \end{array}$

![](https://upload-images.jianshu.io/upload_images/13931179-fedd1e4706cd381e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/562/format/webp)



![](https://upload-images.jianshu.io/upload_images/13931179-2579b5a3a253006b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/603/format/webp)



![img](https://upload-images.jianshu.io/upload_images/13931179-9491dd53f9f637a5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/163/format/webp)

> **2.3、**计算fbank的最后一步是在得到的功率谱上应用三角形滤波器，通常是40个滤波器。
>
> 将滤波器组应用于信号的功率谱(周期图)，得到如下谱图（时频图）：



![](https://upload-images.jianshu.io/upload_images/13931179-e8219d695fcb6f3a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)



致此Fbank结束。

剩余的MFCC的步骤可参照以下两篇

参考文章:   [语音识别--MFCC](https://links.jianshu.com/go?to=https%3A%2F%2Fblog.csdn.net%2Fnsh119%2Farticle%2Fdetails%2F79459416)

​                  [MFCC特征参数提取（知乎）](https://links.jianshu.com/go?to=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F27416870)

以及说得最清楚的一篇英文：[Filter banks, Mel-Frequency Cepstral Coefficients (MFCCs) and What's In-Between](https://links.jianshu.com/go?to=https%3A%2F%2Fhaythamfayek.com%2F2016%2F04%2F21%2Fspeech-processing-for-machine-learning.html)
