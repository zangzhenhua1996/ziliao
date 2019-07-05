　　在了解$DNN$的反向传播算法前，我们先要知道$DNN$反向传播算法要解决的问题，也就是说，什么时候我们需要这个反向传播算法？
　回到我们监督学习的一般问题，假设我们有$m$个训练样本：$\left\{\left(x_{1}, y_{1}\right),\left(x_{2}, y_{2}\right), \ldots,\left(x_{m}, y_{m}\right)\right\}$
,其中$x$为输入向量，特征维度为$n\_in$,而$y$为输出向量，特征维度为$n\_out$。我们需要利用这$m$个样本训练出一个模型，当有一个新的测试样本($x_{test},?$)来到时, 我们可以预测$y_{test}$向量的输出。

　如果我们采用$DNN$的模型，即我们使输入层有$n\_in$个神经元，而输出层有$n\_out$个神经元。再加上一些含有若干神经元的隐藏层。此时我们需要找到合适的所有隐藏层和输出层对应的线性系数矩阵$W$,偏置向量$b$,让所有的训练样本输入计算出的输出尽可能的等于或很接近样本输出。怎么找到合适的参数呢？　

　　　　如果大家对传统的机器学习的算法优化过程熟悉的话，这里就很容易联想到我们可以用一个合适的损失函数来度量训练样本的输出损失，接着对这个损失函数进行优化求最小化的极值，对应的一系列线性系数矩阵$W$,偏置向量$b$即为我们的最终结果。在$DNN$中，损失函数优化极值求解的过程最常见的一般是通过梯度下降法来一步步迭代完成的，当然也可以是其他的迭代方法比如牛顿法与拟牛顿法。如果大家对梯度下降法不熟悉，建议先阅读我之前写的[梯度下降（Gradient Descent）小结](http://www.cnblogs.com/pinard/p/5970503.html)。
对DNN的损失函数用梯度下降法进行迭代优化求极小值的过程即为我们的反向传播算法。
本篇使用了矩阵向量求导，如果你对这一块不熟悉，请先阅读下我写的[矩阵向量求导系列文章](https://www.cnblogs.com/pinard/p/10750718.html)。

## 2. DNN反向传播算法的基本思路
　在进行$DNN$反向传播算法前，我们需要选择一个损失函数，来度量训练样本计算出的输出和真实的训练样本输出之间的损失。你也许会问：训练样本计算出的输出是怎么得来的？这 个输出是随机选择一系列$ W, b$,用我们上一节的前向传播算法计算出来的。即通过一系列的计算：$a^{l}=\sigma\left(z^{l}\right)=\sigma\left(W^{l} a^{l-1}+b^{l}\right)$
计算到输出层第$L$层对应的$a^L$即为前向传播算法计算出来的输出。
回到损失函数，$DNN$可选择的损失函数有不少，为了专注算法，这里我们使用最常见的均方差来度量损失。即对于每个样本，我们期望最小化下式：$$
J(W, b, x, y)=\frac{1}{2}\left\|a^{L}-y\right\|_{2}^{2}
$$
其中，$a^{L}$和$y$为特征维度为$n\_out$的向量,而$\|S\|_{2}$为$S$的$L2$范数　损失函数有了，现在我们开始用梯度下降法迭代求解每一层的$W,b$。
首先是输出层第$L$层。注意到输出层的$W,b$满足下式：
$$a^{L}=\sigma\left(z^{L}\right)=\sigma\left(W^{L} a^{L-1}+b^{L}\right)$$
这样对于输出层的参数，我们的损失函数变为：$$
J(W, b, x, y)=\frac{1}{2}\left\|a^{L}-y\right\|_{2}^{2}=\frac{1}{2}\left\|\sigma\left(W^{L} a^{L-1}+b^{L}\right)-y\right\|_{2}^{2}
$$ (将范数展开成$X^TX$)

这样求解$W,b$的梯度就简单了：$$
\begin{array}{c}{\frac{\partial J(W, b, x, y)}{\partial W^{L}}=\left[\left(a^{L}-y\right) \odot \sigma^{\prime}\left(z^{L}\right)\right]\left(a^{L-1}\right)^{T}} \\ {\frac{\partial J(W, b, x, y)}{\partial b^{L}}=\left(a^{L}-y\right) \odot \sigma^{\prime}\left(z^{L}\right)}\end{array}
$$
这样求解W,b的梯度就简单了：$$
\begin{array}{c}{\frac{\partial J(W, b, x, y)}{\partial W^{L}}=\left[\left(a^{L}-y\right) \odot \sigma^{\prime}\left(z^{L}\right)\right]\left(a^{L-1}\right)^{T}} \\ {\frac{\partial J(W, b, x, y)}{\partial b^{L}}=\left(a^{L}-y\right) \odot \sigma^{\prime}\left(z^{L}\right)}\end{array}
$$
注意上式中有一个符号$⊙$,它代表Hadamard积，对于两个维度相同的向量$A\left(a_{1}, a_{2}, \dots a_{n}\right)^{T}$和$B\left(b_{1}, b_{2}, \dots b_{n}\right)^{T}$,则$A \odot B=\left(a_{1} b_{1}, a_{2} b_{2}, \ldots a_{n} b_{n}\right)^{T}$(对应位置相乘)

我们注意到在求解输出层的$W,b$的时候，有中间依赖部分$\frac{\partial J(W, b, x, y)}{\partial z^{L}}$因此我们可以把公共的部分即对$z^L$先算出来，记为：
$$
\delta^{L}=\frac{\partial J(W, b, x, y)}{\partial z^{L}}=\left(a^{L}-y\right) \odot \sigma^{\prime}\left(z^{L}\right)
$$
　现在我们终于把输出层的梯度算出来了，那么如何计算上一层$L−1$层的梯度，上上层$L−2$层的梯度呢？这里我们需要一步步的递推，注意到对于第$l$层的未激活输出$z^l$，它的梯度可以表示为:
$$
\delta^{l}=\frac{\partial J(W, b, x, y)}{\partial z^{l}}=\left(\frac{\partial z^{L}}{\partial z^{L-1}} \frac{\partial z^{L-1}}{\partial z^{L-2}} \ldots \frac{\partial z^{l+1}}{\partial z^{l}}\right)^{T} \frac{\partial J(W, b, x, y)}{\partial z^{L}}
$$
　如果我们可以依次计算出第l层的$δ^l$,则该层的$W^l,b^l$很容易计算？为什么呢？注意到根据前向传播算法，我们有：
$$
z^{l}=W^{l} a^{l-1}+b^{l}
$$
所以根据上式我们可以很方便的计算出第$l$层的$W^l$,$b^l$的梯度如下：
$$
\frac{\partial J(W, b, x, y)}{\partial W^{l}}=\delta^{l}\left(a^{l-1}\right)^{T}
$$
$$
\frac{\partial J(W, b, x, y)}{\partial b^{l}}=\delta^{l}
$$

　其中，第一个式子的推导可以参考[机器学习中的矩阵向量求导(四) 矩阵向量求导链式法则](https://www.cnblogs.com/pinard/p/10825264.html)中第三节的最后一个公式。

那么现在问题的关键就是要求出$δ^l$了。这里我们用数学归纳法，第$L$层的$δ^L$上面我们已经求出， 假设第$l+1$层的$δ^{l+1}$已经求出来了，那么我们如何求出第$l$层的$δ^l$呢？我们注意到：
$$
\delta^{l}=\frac{\partial J(W, b, x, y)}{\partial z^{l}}=\left(\frac{\partial z^{l+1}}{\partial z^{l}}\right)^{T} \frac{\partial J(W, b, x, y)}{\partial z^{l+1}}=\left(\frac{\partial z^{l+1}}{\partial z^{l}}\right)^{T} \delta^{l+1}
$$
　可见，用归纳法递推$\delta^{l+1}$ 和$\delta^{l}$的关键在于求解$\frac{\partial z^{l+1}}{\partial z^{l}}$
而$z^{l+1}$和$ z^l$的关系其实很容易找出：$$
z^{l+1}=W^{l+1} a^{l}+b^{l+1}=W^{l+1} \sigma\left(z^{l}\right)+b^{l+1}
$$
　这样很容易求出：
$$
\frac{\partial z^{l+1}}{\partial z^{l}}=W^{l+1} \operatorname{diag}\left(\sigma^{\prime}\left(z^{l}\right)\right)
$$
　　将上式带入上面$δ^{l+1}$和$δ^l$关系式我们得到：
$$
\delta^{l}=\left(\frac{\partial z^{l+1}}{\partial z^{l}}\right)^{T} \frac{\partial J(W, b, x, y)}{\partial z^{l+1}}=\operatorname{diag}\left(\sigma^{\prime}\left(z^{l}\right)\right)\left(W^{l+1}\right)^{T} \delta^{l+1}=\left(W^{l+1}\right)^{T} \delta^{l+1} \odot \sigma^{\prime}\left(z^{l}\right)
$$
现在我们得到了$δ^l$的递推关系式，只要求出了某一层的$δ^l$，求解$W^l,b^l$的对应梯度就很简单的。
## 3. DNN反向传播算法过程
　　　　现在我们总结下$DNN$反向传播算法的过程。由于梯度下降法有批量$（Batch）$，小批量$(mini-Batch)$，随机三个变种，为了简化描述，这里我们以最基本的批量梯度下降法为例来描述反向传播算法。实际上在业界使用最多的是$mini-Batch$的梯度下降法。不过区别仅仅在于迭代时训练样本的选择而已。

　　　　输入: 总层数$L$，以及各隐藏层与输出层的神经元个数，激活函数，损失函数，迭代步长$α$,最大迭代次数$MAX$与停止迭代阈值$ϵ$，输入的$m$个训练样本 
$
\left\{\left(x_{1}, y_{1}\right),\left(x_{2}, y_{2}\right), \ldots,\left(x_{m}, y_{m}\right)\right\}
$
　　输出：各隐藏层与输出层的线性关系系数矩阵$W$和偏倚向量$b$
1) 初始化各隐藏层与输出层的线性关系系数矩阵$W$和偏倚向量$b$的值为一个随机值。
2）for iter to 1 to MAX：
2-1) for i =1 to m：
*  a) 将$DNN$输入$a^1$设置为$x_i$
* b) for l=2 to L，进行前向传播算法计算$a^{i, l}=\sigma\left(z^{i, l}\right)=\sigma\left(W^{l} a^{i, l-1}+b^{l}\right)
$
* 　c) 通过损失函数计算输出层的$δ^{i,L}$
* d) for l= L-1 to 2, 进行反向传播算法计算$$
\delta^{i, l}=\left(W^{l+1}\right)^{T} \delta^{i, l+1} \odot \sigma^{\prime}\left(z^{i, l}\right)
$$
* 2-2) for l = 2 to L，更新第$l$层的$W^l,b^l$:
$$
\begin{array}{c}{W^{l}=W^{l}-\alpha \sum_{i=1}^{m} \delta^{i, l}\left(a^{i, l-1}\right)^{T}} \\ {b^{l}=b^{l}-\alpha \sum_{i=1}^{m} \delta^{i, l}}\end{array}
$$

* 2-3) 如果所有$W，b$的变化值都小于停止迭代阈值$ϵ$，则跳出迭代循环到步骤3。
* 3） 输出各隐藏层与输出层的线性关系系数矩阵W和偏倚向量b。
