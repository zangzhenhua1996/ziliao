Transformer结构是谷歌那篇<Attention is all you need>论文中提到的。论文中提出了transformer这么一种新的结构，将其应用在机器翻译的领域上，取得了很好的效果。本文将分析一下Transformer结构的具体组成部分。

整体结构
Transformer 整体结构宏观上看是一个Encoder-Decoder结构，只不过这个结构完全抛弃了常见的RNN,LSTM等结构。
![image.png](https://upload-images.jianshu.io/upload_images/14555448-88dcd8255de27b6a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

图中左边部分为Encoder 部分，右边部分为Decoder部分和最后的线性输出层。其中Encoder和Decoder各有6层。
![image.png](https://upload-images.jianshu.io/upload_images/14555448-3476a4d550b2cc61.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Encoder部分

对于Encoder部分来说，整个的Encoder结构里包含6层，每一层里面有两层。分别是一层self-attention层和一层全连接层。需要注意的是，这里的self-attention并不是只有一层。模型中使用的是multi-head-Attention。其实就是多个self-attention，可以把每个self-attention理解为一个head，多个self-attention自然就是多头了。在上一篇文章中我们已经提到了self-attention的计算，经过计算，一个self-attention会输出一个结果z。那么，multi-head-attention的输出是什么呢？ 答案是把每一个self-attention的输出结果拼接起来。然后输入给后面的全连接网络。

![image.png](https://upload-images.jianshu.io/upload_images/14555448-84f9c00de9b9329e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
全连接网络层是一个两层的网络，第一层是Relu激活函数，第二层是一个线性的激活函数。
这里附上pytorch版本的multi-head attention版本
```python
class MultiHeadedAttention(nn.Module):
    def __init__(self, h, d_model, dropout=0.1):
        "Take in model size and number of heads."
        super(MultiHeadedAttention, self).__init__()
        assert d_model % h == 0
        # We assume d_v always equals d_k
        self.d_k = d_model // h
        self.h = h
        self.linears = clones(nn.Linear(d_model, d_model), 4)
        self.attn = None
        self.dropout = nn.Dropout(p=dropout)
        
    def forward(self, query, key, value, mask=None):
        "Implements Figure 2"
        if mask is not None:
            # Same mask applied to all h heads.
            mask = mask.unsqueeze(1)
        nbatches = query.size(0)
        
        # 1) Do all the linear projections in batch from d_model => h x d_k 
        query, key, value = \
            [l(x).view(nbatches, -1, self.h, self.d_k).transpose(1, 2)
             for l, x in zip(self.linears, (query, key, value))]
        
        # 2) Apply attention on all the projected vectors in batch. 
        x, self.attn = attention(query, key, value, mask=mask, 
                                 dropout=self.dropout)
        
        # 3) "Concat" using a view and apply a final linear. 
        x = x.transpose(1, 2).contiguous() \
             .view(nbatches, -1, self.h * self.d_k)
        return self.linears[-1](x)
```
前面几层的encoder的输出，会作为输入给下一层的encoder。这里要注意，每一个encoder里的两层的输出，都会进入一个add&Norm。最后的encoder会输出给后面的decoder模型。
![image.png](https://upload-images.jianshu.io/upload_images/14555448-95982b1324a34e4d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Decoder部分

Decoder部分和Encoder一样，也是有6层，但是每一个单独的decoder与encoder相比，在self-attention层（decoder层中叫masked self-attention）和全连接网络层之间，多了一层Encoder-Decoder-Attention 层。
![image.png](https://upload-images.jianshu.io/upload_images/14555448-afcb535f811d20b2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
decoder结构中，第一层是一个multi-head-self-attention层，这个与encoder中的区别是这里是masked-multi-head-self-attention。使用mask的原因是因为在预测句子的时候，当前时刻是无法获取到未来时刻的信息的。上一篇文章提到self-attention会生成一个attention map,并以‘I have a dream’为例生成了一个44的attention map，这次生成的44的attention map因为有mask的原因，未来的信息全部被隐藏掉了。

![当前预测的时候是无法获取未来信息的](https://upload-images.jianshu.io/upload_images/14555448-6ccdf93a83bff240.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

decoder中的第二层attention层就是一个正常的multi-head attention层。但是这里Q,K,V来源不同。Q来自于上一个decoder的输出，而K,V则来自于encoder的输出。剩下的计算就没有其他的不同了。
关于这两个attention层，可以理解为 mask-self-attention是计算当前翻译的内容和已经翻译的前文之间的关系，而encoder-decoder-attention 是计算当前翻译内容和编码的特征向量之间的关系。
最后再经过一个全连接层，输出decoder的结果。
个人表达能力有限，这里用博客 The Illustrated Transformer中动图来表示decoder阶段，输出第一个词和输出剩下词的过程。
![6963844-66aa45a6172cd37f.gif](https://upload-images.jianshu.io/upload_images/14555448-f6a6b803c101dc96.gif?imageMogr2/auto-orient/strip)
![22.gif](https://upload-images.jianshu.io/upload_images/14555448-677620f0cfd16c0f.gif?imageMogr2/auto-orient/strip)


Generator部分
最后生成的部分相比之下简单很多。由一个线性层再加一个softmax层完成最后的输出。
![image.png](https://upload-images.jianshu.io/upload_images/14555448-5aa48aee691d2760.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Positional Encoding

按照目前的模型，我们对于输入句子的处理其实忽略了词序问题。
因为按照attention的计算公式，我们只不过是计算了两两之间的attention值。‘I have a dream’ 和 ‘Dream have a I’这两句话对于attention而言是一样。那么截止目前为止，模型还不过是一个复杂的词袋模型，没有考虑到词序。而RNN这种模型的一大特点就是考虑到了词序。为了解决这个问题，transformer模型在数据预处理时就提出了位置编码这个概念。
原文中对于这个位置编码提出了两种方式，第一种是训练出一个位置编码，第二种是原文使用的用三角函数编码的方法。具体公式如下
$$
P E(p o s, 2 i)=\sin \left(\frac{p o s}{10000^{\frac{2 i}{d_{m o d l e l}}}}\right)
$$
$$
P E(\text { pos }, 2 i+1)=\cos \left(\frac{\text { pos }}{10000^{\frac{2 i}{d_{\text {model}}}}}\right)
$$
这里的pos表示单词的位置， i表示embedding的维度.
![image.png](https://upload-images.jianshu.io/upload_images/14555448-265ffa5acc01d180.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
至于为什么使用三角函数，是三角函数的两条性质可以既考虑到绝对位置又可以考虑到相对位置。
$$
\cos (\alpha+\beta)=\cos (\alpha) * \cos (\beta)-\sin (\alpha) \sin (\beta)
$$
$$
\sin (\alpha+\beta)=\sin (\alpha) \cos (\beta)+\cos (\alpha) \sin (\beta)
$$
通过这个公式可以用位置k的线性表达来表示位置k+x。
附上pytorch的代码帮助一下理解。
```python
class PositionalEncoding(nn.Module):
    "Implement the PE function."
    def __init__(self, d_model, dropout, max_len=5000):
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(p=dropout)
        
        # Compute the positional encodings once in log space.
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2) *
                             -(math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)
        
    def forward(self, x):
        x = x + Variable(self.pe[:, :x.size(1)], 
                         requires_grad=False)
        return self.dropout(x)
```
总结
以上就是transformer结构的基本讲解。更深入细节的了解还是要继续研读论文和代码了。
### 参考文献

[1][Attention Is All You Need](http://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf)
[2][详解Transformer （Attention Is All You Need）](https://zhuanlan.zhihu.com/p/48508221)
[3][The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
[4][Visualizing A Neural Machine Translation Model](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/)
[5][在NLP中广泛应用的transformer（Self-Attention）剖析笔记](https://blog.csdn.net/dakenz/article/details/85150676)
[6][Attention is all you need模型笔记](https://zhuanlan.zhihu.com/p/39034683)
[7][The Annotated Transformer](http://nlp.seas.harvard.edu/2018/04/03/attention.html)

转载自:作者：Max_7
链接：https://www.jianshu.com/p/0c196df57323
来源：简书
