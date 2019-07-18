# Transformer详解（一）：从RNN到Attention机制

[转载]([https://www.jianshu.com/p/c5723c3bb921](https://www.jianshu.com/p/c5723c3bb921)
)[https://www.jianshu.com/u/66e78ebcecc7](https://www.jianshu.com/u/66e78ebcecc7)

对于《Attention is all you need》这篇文章中提到的transformer模型，自己最初阅读的时候并不是很理解，于是决定从头开始，一点一点梳理transformer模型的由来。整个文章计划分成三个部分，第一部分，也就是本文，将重点介绍一下NLP方面对于seq2seq的基本发展。第二部分，将讲解attention机制的各个细节。最后一部分，将介绍transformer模型的具体结构。

### 基本RNN结构

对于自然语言处理中的问题，相比较传统的词袋模型和普通的前馈神经网络结构，RNN结构可以更好的考虑到句子中词的先后顺序所带来的不同影响。
RNN的基本结构如下图所示。



![img](https://upload-images.jianshu.io/upload_images/6963844-b6003fb2c504ad43.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/720/format/webp)


整个RNN分成3个部分，输入，输出，和中间的隐状态（hidden state）。隐状态与传统神经网络最大的不同是会接受上一时刻的隐状态。对于$h_1$而言，



$$h_t$$

，需要2个输入。一个是当前的输入

$$x_t$$
，另外一个就是上一时刻的隐状态

$$h_{t-1}$$

这里有一个地方需要注意，在RNN中，$U,W,b$这三个参数在不同的隐状态中也是相同的。也就是说参数是共享的。计算得到隐状态后，要计算当前时刻的输出。

$$y_t = Softmax(Vh_t+c)$$


注意这里的参数$V和c$也是共享的。以上就是最基本的RNN模型，这个模型中，输入的个数严格的等于输出。是标准的N对N。下面将介绍几种RNN的常见变种。

### RNN变种

##### N vs 1

相比于以前每一个输入对应一个输出，当前模型只在最后的一个时刻输出。





![img](https://upload-images.jianshu.io/upload_images/6963844-e4a2646cff524e48.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/720/format/webp)



最常见的使用场景就是做文本分类，将最后一个时刻的输出作为类别的判断。

##### 1 vs N

与上一个模型相反，这次是输入只有一个。
一种情况是把输入作为最初阶段的输入：





![img](https://upload-images.jianshu.io/upload_images/6963844-c3f187af8697b45d.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)



另一种情况是在每个阶段，都把X作为输入：





![img](https://upload-images.jianshu.io/upload_images/6963844-7505eadd57873c0e.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/720/format/webp)


这种结构可以应用的场景有： 图像生成文字等

接下来就要引出本文的核心结构了，当RNN的输入和输出是$N $ $vs$  $M$这种结构时，这种结构也被称作$Encoder-Decoder$ 模型，也可以被称作 seq2seq模型。

### Encoder-Decoder 模型

对于Encoder-decoder 模型，最抽象的一种表示如下图所示



![img](https://upload-images.jianshu.io/upload_images/6963844-44aed20730d1e928.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/701/format/webp)


Encoder网络负责将输入进行编码，得到语义的编码$C$。 Decoder网络负责根据得到的编码$C$，进行解码，解码后输出结果。一个很常见的$encoder-decoder$的例子就是机器翻译，例如中译英，讲中文作为输入放进encode网络，再将其解码后输出英文。对于作为输入的中文，我们把它看成给定的输入句子，Source。经过解码后输出的英文，就是目标句子Target。整个流程可以总结为
$$Source =<x_1,x_2,x_3,...,x_n>$$

$$C = f(Souce)$$


$$y_i = g(C,y_1,y_2,...,y_{i-1})$$


$$ Target = <y_1,y_2,y_3,...,y_m>$$


以上的流程就是基本的encoder-decoder模型的流程，把编码后的C作为最初的输入给decoder网络。decoder网络会根据C和上一个时间点的输出，输出当前时间点的输出。直到最后输出终止符的时候，停止输出。对于编码后的C，有时也会把C作为输入，输入给每一个$y$。对于C的不同使用，见下图示例，但是通常都是把C当做初始状态$h_0$。



![img](https://upload-images.jianshu.io/upload_images/6963844-b83936c024a97262.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/756/format/webp)

c作为decoder的初始状态$h_0$







![img](https://upload-images.jianshu.io/upload_images/6963844-529cf11783c9e5ae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/756/format/webp)

c作为decoder的每一步输入


当然，对于C的计算，也有很多种方法。最简单的方法就是把最后一个时刻的隐状态赋值给C。也就是，也可以对最后一步的隐状态变化后再赋值，或者可以对全部的隐状态都做一个变换。以上就是最常见的Encoder-Decode网络的结构，那么缺点也很明显。首先，对于输入的句子没有区分，在decoder输出时，会把整个输入的句子平等看待。而以人翻译句子的习惯来看，这是不正常的。 第二个问题，如果仅仅把C作为初始状态进行输入，随着RNN网络的推进，传到后面时前面的信息已经非常小了。对于以上情况的改进，就是下一篇文章要提出的attention机制。

### 参考文献

[1][完全图解RNN、RNN变体、Seq2Seq、Attention机制](https://zhuanlan.zhihu.com/p/28054589)
[2][深度学习中的注意力模型（2017版）](https://zhuanlan.zhihu.com/p/37601161)
[3][从Encoder到Decoder实现Seq2Seq模型](https://zhuanlan.zhihu.com/p/27608348)
