# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 07:57:14 2019

@author: zangz
"""

import keras
from keras.layers import Input, Conv2D, BatchNormalization, MaxPooling2D  #输入,2维卷积,数据的标准化?(再查查),最大池化算法
from keras.layers import Reshape, Dense, Lambda 
from keras.optimizers import Adam  #Adam迭代器
from keras import backend as K  #导入底层框架
from keras.models import Model  #训练模型 
from keras.utils import multi_gpu_model  #多GPU使用
