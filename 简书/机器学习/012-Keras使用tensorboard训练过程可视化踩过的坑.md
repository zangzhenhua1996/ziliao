《Python深度学习》看到第七章，由于时间跨度较大，前面内容有点记不太清楚了，好在演示代码都挨着运行成功了一遍，也参照教程使用CNN写了个简单的验证码识别模型出来。
在使用tensorboard做可视化的过程中，遇到一些坑，在这里记录下解决问题的心路历程，后面换电脑的话也有个参考：

#### 问题一：No module named 'google.protobuf.pyext'
解决方式： 管理员模式打开cmd :
`pip install protobuf -i https://pypi.tuna.tsinghua.edu.cn/simple`
当然pip源可以选个自己喜欢的。这个问题完全没有必要写的啊 但事实上确实困扰了我一两个小时，之前总觉得是google包出了问题，怎么装都没法解决。尴尬，先挂到这里起警示作用吧！

#### 问题二：Allocation of 6400000000 exceeds 10% of system memory.
啰嗦：之前单独使用一维卷积训练imdb的时候运行还比较正常，怎么添加了callback后就内存不足了呢。看来使用tensorboard回调是一件占用内存挺高的操作。回去对比了一下，演示代码的max_features也比之前的大了一倍，难怪我的小内存笔记本有点吃不消了。
解决方式：max_features = 500, 减少特征数量，从而减少网络的大小。
对，这里还是把书中代码修改的地方标注一下吧：
```python
import keras
from keras import layers
from keras.datasets import imdb
from keras.preprocessing import sequence
max_features = 500 # 原文为2000
max_len = 500
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
x_train = sequence.pad_sequences(x_train, maxlen=max_len)
x_test = sequence.pad_sequences(x_test, maxlen=max_len)
model = keras.models.Sequential()
model.add(layers.Embedding(max_features, 128, input_length=max_len, name='embed'))
model.add(layers.Conv1D(32, 7, activation='relu'))
model.add(layers.MaxPooling1D(5))
model.add(layers.Conv1D(32, 7, activation='relu'))
model.add(layers.GlobalMaxPooling1D())
model.add(layers.Dense(1))
model.summary()
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
callbacks = [keras.callbacks.TensorBoard(
                      log_dir='my_log_dir',
                      histogram_freq=1,
                      embeddings_freq=1,
                      embeddings_data = x_train[:100].astype("float32")
)]
history = model.fit(x_train, y_train,  epochs=20, batch_size=128, validation_split=0.2, callbacks=callbacks)  
```
#### 问题三：ValueError: To visualize embeddings, embeddings_data must be provided.
啰唆：字面意思应该是回掉的TensorBoard类中没有指定
embeddings_data的值，按理说这么经典的书应该不会出这种问题，可能是版本的差异吧。
解决方式：添加embeddings_data=x_train试试... 仍然会报错，但是这次的错误比较明显，embeddings_data需要是float类型的，而我们的x_train还是int32。使用astype转换成float类型再次填写参数。
见证奇迹的时刻终于到了~浏览器可以正常访问 tensorboard，使用PCA计算出Embedding 的结果，结果大概就是下面的样子（还是有些酷炫的嘛）。
![image.png](https://upload-images.jianshu.io/upload_images/14555448-cfeaf160d2fbabff.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
