###使用linux系统真的是什么奇奇怪怪的问题，最近需要安装cuda，自己的显卡cuda只支持到16.04，只能换一个系统了又降级回了16.04

*   确定无线网卡芯片是否是`0bda:8179`，通过下面 `lsusb`

*   `lsusb` 信息
    `Bus 001 Device 010: ID 0bda:8179 Realtek Semiconductor Corp.`     `主要是后面的信息`

*   下载驱动 ，并按照其中README.md步骤安装驱动

    [https://github.com/lwfinger/rtl8188eu/tree/v4.1.8_9499](https://github.com/lwfinger/rtl8188eu/tree/v4.1.8_9499)
####首先将压缩包下载下来，然后解压
####执行 `make all`
####执行`sudo make install`
就安装完毕了。
然后继续执行下面的操作

*   打开8188eu.conf

*   ` sudo gedit /etc/modprobe.d/8188eu.conf`

*   添加下面的代码     :    
```

  #加点参数, 禁用自动休眠        

options 8188eu rtw_power_mgnt=0
```
#最后完成，重启！终于不用再忍受时刻断网的困扰了。
