**ubuntu****系统下matplotlib中文乱码问题**



**在**[**ubuntu**](https://www.baidu.com/s?wd=ubuntu&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)  **下利用matplotlib 绘图的时候，图像上中文无法显示。以下是我的解决办法：**

**1\. 下载中文字体simhei.ttf, 网址**为[http://fontzone.net/download/simhei](http://fontzone.net/download/simhei)

**2\. 搜索 matplotlib 字体的安装位置**

`$locate -b '\mpl-data'`

会得到 这个路径`/usr/share/matplotlib/mpl-data`下面有`fonts/ttf`这个目录，进入这个目录，把刚才下载的simhei.ttf 字体复制到这个目录下，注意权限和归属是否与其它字体一致，我的是归于[root](https://www.baidu.com/s?wd=root&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)用户的，所以用root 用户复制过来。

**3\. 删除当前用户matplotlib 的缓冲文件（如果没有直接进入第四步）**
``` shell
$cd ~/.cache/matplotlib
 $rm -rf *.*
```
**4.代码中调整字体**
``` python
#!/usr/bin/env  python

#coding:utf-8

"""a demo  of matplotlib"""

import matplotlib as  mpl

from matplotlib  import pyplot as plt

mpl.rcParams[u'font.sans-serif'] = ['simhei']

mpl.rcParams['axes.unicode_minus'] = False

years = [1950, 1960,  1970, 1980,  1990, 2000,  2010]

gdp = [300.2, 543.3,  1075.9, 2862.5,  5979.6, 10289.7,  14958.3]

#创建一副线图,x轴是年份,y轴是gdp

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

#添加一个标题

plt.title(u'名义GDP')

#给y轴加标记

plt.ylabel(u'十亿美元')

plt.show()
```

*   其中`#coding:utf-8 `说明文件编码格式

*  ` mpl.rcParams[u'font.sans-serif'] = ['simhei'] `用`simhei `字体显示中文

*  ` mpl.rcParams['axes.unicode_minus'] = False` 这个用来正常显示负号

*  ` plt.title(u'名义GDP')`这里的`u `最好不要少主要是让其编码是`utf-8`


