### 首先上网下载Mathpix Snipping Tool、Typora与Pandoc。下载地址如下：

https://mathpix.com/

https://www.typora.io/

https://github.com/jgm/pandoc/releases/tag/2.0.5

### 下载完进行安装即可,都是免费软件无需破解

### 概念及功能解释：
####Mathpix Snipping Tool: 
Mathpix Snipping Tool is a Shareware software in the category Miscellaneous developed by Mathpix, Inc.

这个软件本质上是一个OCR软件，将截取的图片转化成LaTeX的代码

####Typora:
 一款简单高效的Markdown编辑器。这里是我们的桥梁，接受LaTeX的代码，转化成可视化的公式。

#### Pandoc:
 A universal document text converter. Typora use it to support file import/export features for several file types including .docx file. 

安装Pandoc是为了以后可以导出成Word，否则将会失败。

#### LaTeX
是一种基于TEX的排版系统，用它写数学公式非常漂亮。

举例演示：
假设论文中有一个这样的简单公式：

![image.png](https://upload-images.jianshu.io/upload_images/14555448-846c5d6b59921fc9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



用Mathpix Snipping Tool得到的识别效果如下图所示：

![image.png](https://upload-images.jianshu.io/upload_images/14555448-52c1f9478199dc96.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


其中Confidence是指软件对自己翻译的公式的有把握程度。

复制上面那个公式，就是点击一下就到剪贴板了。

打开Typora软件，按Ctrl+Shift+M(或者输入$$敲回车)，进入Math Block

![image.png](https://upload-images.jianshu.io/upload_images/14555448-292851964c9e3104.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


在两个$$之间，粘贴刚刚复制的LaTeX表达式公式：

![image.png](https://upload-images.jianshu.io/upload_images/14555448-71fdf7251f169d0e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


在外面空白处点击一下，就有了这个公式：
![image.png](https://upload-images.jianshu.io/upload_images/14555448-3a2b5e869441ba23.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



然后，导出成Word。进入File->Export->Word
![image.png](https://upload-images.jianshu.io/upload_images/14555448-9841a1354f53451a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



打开那个Word你就发现了这个公式：

![image.png](https://upload-images.jianshu.io/upload_images/14555448-50607be68c4bb091.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


所以你可以将别人论文中的公式统统用Mathpix Snipping Tool翻译成LaTeX代码，然后用Typora获得可视化的公式，最后导出到Word中，再做必要的修改。

这个方法的特点是实现了LaTeX代码到Word可编辑公式的转换，实用价值颇高。

##备注
如果自己有Mathtype(或者AXmath)并能放到Word里面则是最好不过的了，这样只需要用Mathpix Snipping Tool，得到LaTeX代码，然后就能直接输入到Mathtype里面，得到Word中可以方便编辑的公式了。
