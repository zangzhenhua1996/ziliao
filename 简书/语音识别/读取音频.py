# -*- coding: utf-8 -*-
"""
Created on Thu May 30 09:17:13 2019

@author: zangz
"""
import scipy.io.wavfile as wav  #scipy中专门处理wav的函数
import matplotlib.pyplot as plt
import os

# 随意搞个音频做实验
filepath = 'test.wav'  #文件路径

fs, wavsignal = wav.read(filepath)   #读取音频,并返回fs(频率),及信号大小

plt.plot(wavsignal)
plt.show()


