###ubuntu更新（sudo apt-get update）时，
出现错误：
```
“Failed to fetch http://dl.google.com/linux/chrome/deb/dists/stable/Release Unable to find expected entry ‘main/binary-i386/Packages’ in Release file (Wrong sources.list entry or malformed file)”
```
###解决方式：
####1.打开 /etc/apt/sources.list.d/google-chrome.list 文件（用vim或者gedit等均可）：
```sudo gedit /etc/apt/sources.list.d/google-chrome.list```

####2，修改文件内容：
#####原来是：
```deb http://dl.google.com/linux/chrome/deb/ stable main```
#####改为：
```deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main```

####3, 再次执行 更新命令即可通过了
```sudo apt-get update```
#注意:
如果本来就是
```deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main```    报错了
那么先改回
```deb http://dl.google.com/linux/chrome/deb/ stable main```
然后进行更新.
然后再重新改回来```deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main```
再次更新就可以了.
![image.png](https://upload-images.jianshu.io/upload_images/14555448-f9f2e3aa409b8832.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

