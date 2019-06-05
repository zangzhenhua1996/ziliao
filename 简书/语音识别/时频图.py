# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:20:02 2019

@author: zangz
"""

import numpy as np
import scipy.io.wavfile as wav
from scipy.fftpack import fft


# 获取信号的时频图
def compute_fbank(file): #传入的是文件的路径
	x=np.linspace(0, 400 - 1, 400, dtype = np.int64)
	w = 0.54 - 0.46 * np.cos(2 * np.pi * (x) / (400 - 1) ) # 汉明窗
	fs, wavsignal = wav.read(file)
    
	# wav波形 加时间窗以及时移10ms
	time_window = 25 # 单位ms
	window_length = fs / 1000 * time_window # 计算窗长度的公式，目前全部为400固定值
    
	wav_arr = np.array(wavsignal) #将信号转换成数组
	wav_length = len(wavsignal)  #长度
	range0_end = int(len(wavsignal)/fs*1000 - time_window) // 10 # 计算循环终止的位置，也就是最终生成的窗数,取整摄取最后的不能整除的部分
	data_input = np.zeros((range0_end, 200), dtype = np.float) # 用于存放最终的频率特征数据
	data_line = np.zeros((1, 400), dtype = np.float)
	for i in range(0, range0_end):
		p_start = i * 160     #10ms移动的采样点是16000/1000 *10 =160
		p_end = p_start + 400
		data_line = wav_arr[p_start:p_end]	
		data_line = data_line * w # 加窗
		data_line = np.abs(fft(data_line))
		data_input[i]=data_line[0:200] # 设置为400除以2的值（即200）是取一半数据，因为是对称的
	data_input = np.log(data_input + 1)  #这里加1的原因是保证取完log全是正数
	#data_input = data_input[::]
	return data_input


import matplotlib.pyplot as plt
filepath = 'test.wav'   #文件路径

a = compute_fbank(filepath)  #获取信号的时频图
#取转置的原因我们需要将横坐标是时间,纵坐标是每一帧对应得取了傅里叶变换及对数的值
#origin = 'lower'的作用就是让纵坐标从低向上,如果不加默认的是从高往低(200---0)
plt.imshow(a.T, origin = 'lower')  #以时间为横坐标,就是25ms一帧对应一个横坐标.这一帧对应的200个点为纵坐标
plt.show()