1.安装:在终端中输入以下命令:

`sudo apt-get install terminator`

2.设置默认终端 为 Terminator
```bash
gsettings  set org.gnome.desktop.default-applications.terminal  exec  /usr/bin/terminator

gsettings  set  org.gnome.desktop.default-applications.terminal   exec-arg  "-x"
```
注意:设置默认终端 为 gnome-terminal
```bash
gsetting set org.gnome.desktop.default-applications.terminal exec /usr/bin/gnome-terminal

gsettings set org.gnome.desktop.default-applications.terminal exec-arg "-x"
```
注:也可以不设置默认终端,其实没有必要.

在右键菜单打开终端时打开的依旧是默认的乌班图终端.

但是使用快捷键 ctrl+alt+T打开的是我们安装好的终端Terminator.我们把它添加到收藏夹即可.

3.修改配色方案

在终端空白处中打开右键菜单->配置文件首选项

剩下的怎么配置看自己心情了

4常用快捷键

Ctrl+Alt+T 打开终端

Ctrl+l 相当于clear，即清屏

Shift+Ctrl+T 打开新的标签页

Shift+Ctrl+W 关闭标签页

Shift+Ctrl+C 复制

Shift+Ctrl+V 粘贴

Shift+Ctrl+N 打开新的终端窗口

Shift+Ctrl+o 上下拆分屏幕

Shift+Ctrl+e 左右拆分屏幕

Shift+Ctrl+w 关闭当前窗口

Shift+Ctrl+q 关闭整个终端

F11 全屏切换

Ctrl + Page Down/ Page Up 切换标签页

5.看看效果吧(透明的背景)

![image](https://upload-images.jianshu.io/upload_images/14555448-6a151821e3df6b70.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
