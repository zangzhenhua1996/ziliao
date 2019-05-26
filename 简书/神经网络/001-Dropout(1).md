> 深度学习经典论文Top100(Most Cited Deep Learning Papers) 阅读笔记. 论文集地址:<https://github.com/terryum/awesome-deep-learning-papers>.
>  本文摘要：本文介绍了Dropout的基本概念和基本方法，以及一些使用的注意事项;
>  关键词：过拟合; Dropout

### 相关论文

2012 Improving neural networks by preventing co-adaptation of feature detectors
 <https://arxiv.org/pdf/1207.0580.pdf>
 [2014 JMLR] Dropout: A Simple Way to Prevent Neural Networks from Overfitting
 <http://jmlr.org/papers/volume15/srivastava14a.old/srivastava14a.pdf>

### I.问题

文中提到：深度神经网络非常的有效， 但是在在少量样本的情况下，使用（深度）神经网络很容易过拟合。

### II.方法原理

#### 1.基本概念

Dropout：如下图所示, 在训练的时候，使部分神经元暂时被隔离或者被忽略，减少一些某些特征的协同作用（co-adaptation），这样可以让每一个神经元独立地学习到一个特征，这样在测试的时候，可以组合出更多的内部的上下文（interal contexts），也就是组合特征。


![dropout](https://upload-images.jianshu.io/upload_images/14555448-7d7d261304668c11.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)





下面是论文中提到的关于Dropout的直观解释：

- 在训练阶段，每一个隐层神经元都以一定的概率被随机的忽略，因此不能保证每两个神经元总是同时出现，这样权值的更新就不在依赖固定关系隐含节点的共同作用，让每一个神经元学习到独立的特征，这样进行测试的时候，可以组合出更多的表示。
- 在测试阶段，所有的节点都是连接着的，此时可以看做是对dropout所有情况的平均。如果有N个节点，每个节点有两种选择（连接或者不连接），在训练的阶段采取dropout, 总共有$2^N$次种情况。文中提到测试阶段的全连接相当于对这些网络的平均，而采取多个网络是提升performance的一个有效的方法，但是有一些问题（见Section III），而这里的平均相当于综合了之前$2^N$种网络，但是同时避免了III中说到的那些问题。



![训练阶段和测试阶段](https://upload-images.jianshu.io/upload_images/14555448-53f3f5f2ed24cbe5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




- Dropout和Naive Bayes (NB) 的关系.
   NB一个很强的假设：特征相互独立。在训练NB时，特征单独学习，Dropout除了实现特征单独学习，还包含了多个特征联合学习的情况，所涉及的情况更多，也就是说NB可以看做是Dropout的一个特例。
- Dropout和Bagging的关系
   Bagging是通过随机采样N个子数据集,然后训练多个多分类器进行集成学习.根据上面的直观解释, 每次迭代都加入dropout的模型都训练了一个不同的架构，参数更新只关注激活的神经元.这种正则化方法可以看成是一种集成方法，即集成每个批量所训练的不同网络架构, 也就是说Dropout可以看做是Bagging.

> 下面是我的理解：训练的时候，让每个节点独当一面，测试的时候一块用。

#### 2.基本方法
标准的网络:

![Standard neural network](https://upload-images.jianshu.io/upload_images/9060795-09501cb74460101b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/515/format/webp)

加入dropout:

![NN with dropout](https://upload-images.jianshu.io/upload_images/9060795-e8ba7126d9a3574d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/503/format/webp)

也就是下面这个图的内容:

![NN and NN with dropout](https://upload-images.jianshu.io/upload_images/9060795-10be78152b5703cb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)




### III.相似的工作

1.多个独立的模型的Combination
 文中提到这种结合的方法的缺点：

- 代价方法很大；
- 训练较困难，原因是模型多意味着参数量大，找到最优解的难度大，时间复杂度也高；
- 不同的网络要使用全集中的子集，不够分
   （疑问：数据是否可以重叠着分给不同的网络；多个独立的模型代价比较大的话，是否可以采用多支路的方式）

2.解决过拟合的方法

- Early stop: 当模型在验证集上的表现开始变差的时候停止训练
- Weight penalties: L1, L2, soft weight sharing.

### IV.关键信息

#### 1.Dropout 配置

- 对于隐层, 通常使用的范围是(0.2~0.5), 0.2是一个比较好的起点，过高的rate可能导致网络学习能力下降而无法收敛; 对于输入层, 取决于数据,如果是image或者speech frame, 0.2是一个好的选择.
- 一般来说，在大的网络上，使用dropout能够出现更多有效的组合方式,使用dropout可能获得好的表现;
- 使用dropout会降低训练时网络的容量大小, 如果一个网络在$n$个神经元上表现的很好,那么在使用dropout的网络中,神经元的个数扩大为n/p,表现比较好.
- Dropout一般可以加在输入层,隐藏层; 但是对于卷积层,效果可能不是很明显,原因是卷积核的参数有限:

> One may have presumed that since the convolutional layers don’t have a lot of parameters, overfitting is not a problem and therefore dropout would not have much effect.

- 使用的过程中采用带有衰减的学习率,以及较大的动量(具体原因在下面有解释);
- 对权重进行一定的Norm constraint.
- 在文本上使用,效果不是很明显:

> We found that the improvement was much smaller compared to that for the vision and speech datasets. This might be explained by the fact that this data set is quite big (more than 200,000 training examples) and overfitting is not a very serious problem.

#### 2.配置说明

尽管Dropout在解决过拟合的时候能够取得很好的效果,但是往往需要与其他的方法进行结合,比如 max-norm regularization, large decaying learning rates and high momentum. Dropout会引入大量的噪声,如果采用原来的学习率,训练时间会加倍,因此一般采用10~100倍原来的学习率.另外的一种方法是使用高动量进行训练,可以加速搜索.

- Max-norm regulation: 对神经网络的权重进行限制,使得权重的搜索空间在一个固定半径$c$的圆球内$c$的取值一般为3~4,$c$是可训练的参数), 这样的话, 使用较大的学习率可以搜索更多的球内空间而不会出现weights blowing up.
- Learning rates decay使得搜索的空间的步伐慢慢降低,快速到达一个(局部的)最小点
- Dropout也可以用在finetune nets,文中提到训练的时候,加载的预训练权重应当缩小为原来的$1/p$.

#### 3.Global contrast normalization

Global contrast normalization means that for image and each colour channel in that image, we compute the mean of the pixel intensities and subtract it from the channel.

#### 4.ZCA whitening

ZCA whitening means that we mean center the data, rotate it onto its principle components, normalize each component and then rotate it back.

#### 5. 使用高斯分布(Multiplicative Gaussian Noise Dropout)

$h_i \to h_i + h_i r, r-N(1,\sigma^2)$
 这里的$\sigma$是一个可学习的参数

### VI. 其他

Applying dropout to a neural network amounts to sampling a "thinned" network from it.
 采取dropout等价于一个神经网络从其中采样了一个瘦的网络.

As the learning rate decays, the optimization takes shorter steps, thereby doing less exploration and eventually settles into a minimum.
 随着学习率的衰减,优化步骤也会缩短,从而减少了更少的搜索,最终会到达一个最小值

### VII.References

<https://blog.csdn.net/hjimce/article/details/50413257>
 <https://machinelearningmastery.com/dropout-regularization-deep-learning-models-keras/>
 <https://www.jiqizhixin.com/technologies/1c91194a-1732-4fb3-90c9-e0135c69027e>

转载:
作者：转身之后_UCAS

链接：https://www.jianshu.com/p/689a75950339

