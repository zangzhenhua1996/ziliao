# -*- coding: utf-8 -*-
"""
Created on Thu May 30 09:31:53 2019

@author: zangz
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0, 400 - 1, 400, dtype = np.int64)  #画出400个从0-399的点

w = 0.54 - 0.46 * np.cos(2 * np.pi * (x) / (400 - 1))  #汉明窗的构造
plt.plot(w)
plt.show()


time_window = 25
window_length = fs // 1000 * time_window

# 分帧
p_begin = 0
p_end = p_begin + window_length   #帧长
frame = wavsignal[p_begin:p_end]   #取出信号(400个采样点)
plt.plot(frame)
plt.show()  

# 加窗
frame = frame * w  #利用汉明窗对取出的采样点 进行加窗
plt.plot(frame)
plt.show()


from scipy.fftpack import fft

# 进行快速傅里叶变换
frame_fft = np.abs(fft(frame))[:200]  #因为是对称的取一半就可以了[:200],左右对称
plt.plot(frame_fft)
plt.show()

# 取对数，求db
frame_log = np.log(frame_fft)  #取对数
plt.plot(frame_log)
plt.show()
