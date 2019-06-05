# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:35:03 2019

@author: zangz
"""

import numpy as np
import scipy.io.wavfile as wav
from scipy.fftpack import fft
import matplotlib.pyplot as plt

# 获取信号的时频图
def compute_fbank(file):
	x=np.linspace(0, 400 - 1, 400, dtype = np.int64)  #生成一个0-399的x坐标
	w = 0.54 - 0.46 * np.cos(2 * np.pi * (x) / (400 - 1) ) # 汉明窗公式
	fs, wavsignal = wav.read(file)  #返回采样频率及信号
	# wav波形 加时间窗以及时移10ms
	time_window = 25 # 单位ms每一帧是25ms
	window_length = fs / 1000 * time_window # 计算窗长度的公式，目前全部为400固定值
	wav_arr = np.array(wavsignal)
	wav_length = len(wavsignal)   #输入的语音的长度
	range0_end = int(wav_length/fs*1000 - time_window) // 10 # 计算循环终止的位置，也就是最终生成的窗数
	data_input = np.zeros((range0_end, 200), dtype = np.float) # 用于存放最终的频率特征数据
	data_line = np.zeros((1, 400), dtype = np.float)
	for i in range(0, range0_end):
		p_start = i * 160
		p_end = p_start + int(window_length)   #window_length目前就是固定的400,这里必须是整型
		data_line = wav_arr[p_start:p_end]	
		data_line = data_line * w # 加窗
		data_line = np.abs(fft(data_line))
		data_input[i]=data_line[0:200] # 设置为400除以2的值（即200）是取一半数据，因为是对称的
	data_input = np.log(data_input + 1)
	#data_input = data_input[::]
	return data_input

if __name__ == '__main__' :
    filepath = 'test.wav'   #文件路径
    a = compute_fbank(filepath)  #获取信号的时频图
    #取转置的原因我们需要将横坐标是时间,纵坐标是每一帧对应得取了傅里叶变换及对数的值
    #origin = 'lower'的作用就是让纵坐标从低向上,如果不加默认的是从高往低(200---0)
    plt.imshow(a.T, origin = 'lower')  #以时间为横坐标,就是25ms一帧对应一个横坐标.这一帧对应的200个点为纵坐标
    plt.show()