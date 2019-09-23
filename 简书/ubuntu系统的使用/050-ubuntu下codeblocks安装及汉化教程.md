ubuntu下codeblocks安装及汉化教程

一、安装codeblocks

sudo apt-get install codeblocks codeblocks-dev

二、汉化方法

1、下载中文mo包

简体中文mo包

2、创建中文包目录

cd /usr/share/codeblocks/

sudo mkdir locale

cd locale

sudo mkdir zh_CN

cd zh_CN

cp CodeBlocks.mo .

chmod 777 CodeBlocks.mo



大功告成！


