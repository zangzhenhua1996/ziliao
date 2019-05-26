### **1.安装包准备**

TeXLive 的版本是 2017，可以从官方站点下载[安装包](http://mirror.ctan.org/systems/texlive/Images/texlive2017.iso), 。
2.TeXLive2017安装
```bash
sudo apt-get install perl
sudo apt-get install perl-tk
```
进入texlive2017安装包所在目录,执行以下命令安装texlive:
```bash
sudo mount -o loop ./texlive.iso /mnt/
cd /mnt
sudo ./install-tl
```
大概需要安装十多分钟,默认按照/usr/local/texlive目录,安装完毕然后执行以下命令配置环境变量:
```bash
sudo gedit ~/.bashrc
```
在.bashrc文件末尾添加
```bash
export PATH=/usr/local/texlive/2017/bin/x86_64-linux:$PATH
export MANPATH=/usr/local/texlive/2017/texmf-dist/doc/man:$MANPATH 
export INFOPATH=/usr/local/texlive/2017/texmf-dist/doc/info:$INFOPATH 
```
3.TexStudio安装
可以下载texStudio的deb安装包,点击安装,也可以执行以下命令进行安装:
```bash
sudo apt-get install texstudio
```
