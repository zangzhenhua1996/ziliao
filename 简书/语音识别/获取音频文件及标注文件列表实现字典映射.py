# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:54:10 2019

@author: zangz
"""
import os
import matplotlib.pyplot as plt
from shipintu import compute_fbank 
import numpy as np
def source_get(source_file):  #需要获取的文件路径
    train_file = source_file + '/data'   #这个路径下的data文件夹保存的是音频问价及标注文件
    
    label_lst = []  #存储的是标准文件
    wav_lst = []   #存储的音频文件名
    for root, dirs, files in os.walk(train_file):
        for file in files:
            if file.endswith('.wav') or file.endswith('.WAV'):
                wav_file = os.sep.join([root, file])
                label_file = wav_file + '.trn'  
                wav_lst.append(wav_file)
                label_lst.append(label_file)
            
    return label_lst, wav_lst

label_lst, wav_lst = source_get('F:\\语音识别\\语音数据集\\data_thchs30')

print(label_lst[:10])  #标注文件
print(wav_lst[:10])   #音频文件的路径及其名称


for i in range(10000):
    wavname = (wav_lst[i].split('/')[-1]).split('.')[0]   #获取的就是前面的前缀名称,但是没有什么太大的意义
    labelname = (label_lst[i].split('/')[-1]).split('.')[0]
    if wavname != labelname:
        print('error')

#这里要搭配上面定义的函数一起使用
#定义读取该文件的文字
def read_label(label_file):
    with open(label_file, 'r', encoding='utf8') as f:
        data = f.readlines()  #readlines()方法读取整个文件所有行，保存在一个列表(list)变量中，每行作为一个元素，但读取大文件会比较占内存
        return data[1]   #这里返回的是拼音这一行(第二行)

print(read_label(label_lst[0]))  #这里打印第一个文件测试一下

def gen_label_data(label_lst):
    label_data = []
    for label_file in label_lst:
        pny = read_label(label_file)
        label_data.append(pny.strip('\n'))
    return label_data   #这里返回的是一个list存储了所有的拼音串

label_data = gen_label_data(label_lst)
print(len(label_data))




#为label建立拼音到id的映射，即词典
def mk_vocab(label_data):  #传入的就是前面做好的包含所有拼音串的列表
    vocab = []  #新建一个空的list
    for line in label_data:  #从拼音串列表中每行取出
        line = line.split(' ')  #以空格进行分割,存储成一个多行的list每个拼音是一行
        for pny in line:  #对这一个单独的拼音list进行遍历
            if pny not in vocab:  #如果这个单独的拼音不在总的拼音字符中就进行添加,这样就可以去除重复,保留的都是不相同的拼音
                vocab.append(pny)
    vocab.append('_')   #最后添加一个_作为终止符
    return vocab

vocab = mk_vocab(label_data)
print(len(vocab))

#有了词典就能将读取到的label映射到对应的id
def word2id(line, vocab):  #输入的是需要转换成id的line,以及词典
    return [vocab.index(pny) for pny in line.split(' ')] #使用的是列表生成器


label_id = word2id(label_data[0], vocab)  #这里测试的数据的第一行
print(label_data[0])
print(label_id)

fbank = compute_fbank(wav_lst[0])  #将第一个音频文件转换成视频图

print(fbank.shape)  #打印时频矩阵的形状


plt.imshow(fbank.T, origin = 'lower')
plt.show()

fbank = fbank[:fbank.shape[0]//8*8, :]
print(fbank.shape)


from random import shuffle
shuffle_list = [i for i in range(10000)]   #先生称0-10000的顺序列表
shuffle(shuffle_list)  #进行打乱

#数据生成器,需要传入的每次训练数据的大小,乱序的列表,音频文件路径,标注文件路径,建立好的词典映射
def get_batch(batch_size, shuffle_list, wav_lst, label_data, vocab):
    for i in range(10000//batch_size):  #10000//batch_size 一个周期循环取这么多次
        wav_data_lst = []  #每次循环建立一个空的存放音频文件路径的列表
        label_data_lst = []   #每次循环建立一个空的存放标注文件路径的列表
        begin = i * batch_size  #每次取数据的起始索引
        end = begin + batch_size #每次取数据的结束索引
        sub_list = shuffle_list[begin:end]  #取出乱序的索引
        for index in sub_list:  #按照乱序的索引取数据
            fbank = compute_fbank(wav_lst[index]) #取出音频生成时频矩阵
            fbank = fbank[:fbank.shape[0] // 8 * 8, :] #对时频矩阵进行处理保证能被8整除
            label = word2id(label_data[index], vocab) #取出标注数据转换成字典映射
            wav_data_lst.append(fbank)  
            label_data_lst.append(label)  #将处理好的时频矩阵及字典映射好的标签进行存储
        yield wav_data_lst, label_data_lst    #使用yield生成器进行存储,类似于链表

batch = get_batch(4, shuffle_list, wav_lst, label_data, vocab)   

wav_data_lst, label_data_lst = next(batch)  #每次取数据使用的是next函数(对应的是yield生成器),每次执行都会取出下一个对应的数据类似链表的作用
#循环打印一下取出的4个数据组
for wav_data in wav_data_lst:
    print(wav_data.shape)
for label_data in label_data_lst:
    print(label_data)


lens = [len(wav) for wav in wav_data_lst]  #取出的四个数据中时频矩阵的行的大小
print(max(lens))     #查找最大的一个
print(lens)

def wav_padding(wav_data_lst):
    wav_lens = [len(data) for data in wav_data_lst]
    wav_max_len = max(wav_lens)
    wav_lens = np.array([leng//8 for leng in wav_lens])  #将四个时频矩阵的行长度除以8再进行存储,因为卷积后长度缩小8倍输入给CTC需要给定长度,所以需要将长度提前存成缩小为8倍的
    new_wav_data_lst = np.zeros((len(wav_data_lst), wav_max_len, 200, 1)) #这里需要生成的传递给tensorflow的数组,第一位是每次训练的数据量,第二维是,四个数据时频矩阵的最大长度(需要统一长度,不够的默认补零),第三维就是时频矩阵的列维度(200),第四维是通道数(这里是1)
    for i in range(len(wav_data_lst)): #循环存储
        new_wav_data_lst[i, :wav_data_lst[i].shape[0], :, 0] = wav_data_lst[i]#赋值给第二列
    return new_wav_data_lst, wav_lens  #返回处理好的一训练需要的传递给tensorflow的数据及音频除以8的音频长度

pad_wav_data_lst, wav_lens = wav_padding(wav_data_lst)
print(pad_wav_data_lst.shape)
print(wav_lens)


def label_padding(label_data_lst):  #传入的是标注矩阵
    label_lens = np.array([len(label) for label in label_data_lst]) #获取每个label矩阵的长度
    max_label_len = max(label_lens) #最大长度
    new_label_data_lst = np.zeros((len(label_data_lst), max_label_len))  #生成一个4行的label矩阵(其他的不够长度的补零跟前面一致)
    for i in range(len(label_data_lst)):
        new_label_data_lst[i][:len(label_data_lst[i])] = label_data_lst[i]
    return new_label_data_lst, label_lens

pad_label_data_lst, label_lens = label_padding(label_data_lst)
print(pad_label_data_lst.shape)
print(label_lens)
print(pad_label_data_lst)



def data_generator(batch_size, shuffle_list, wav_lst, label_data, vocab):
    for i in range(len(wav_lst)//batch_size):
        wav_data_lst = []
        label_data_lst = []
        begin = i * batch_size
        end = begin + batch_size
        sub_list = shuffle_list[begin:end]
        for index in sub_list:
            fbank = compute_fbank(wav_lst[index])
            pad_fbank = np.zeros((fbank.shape[0]//8*8+8, fbank.shape[1]))
            pad_fbank[:fbank.shape[0], :] = fbank
            label = word2id(label_data[index], vocab)
            wav_data_lst.append(pad_fbank)
            label_data_lst.append(label)
        pad_wav_data, input_length = wav_padding(wav_data_lst)
        pad_label_data, label_length = label_padding(label_data_lst)
        inputs = {'the_inputs': pad_wav_data,  
                  'the_labels': pad_label_data,
                  'input_length': input_length,
                  'label_length': label_length,
                 }
        outputs = {'ctc': np.zeros(pad_wav_data.shape[0],)} 
        yield inputs, outputs