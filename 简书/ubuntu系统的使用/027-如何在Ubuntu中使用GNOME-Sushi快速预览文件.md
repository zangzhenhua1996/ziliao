不知道大家有没遇到过，要在数千甚至上万个文档中查找特定所需文件的经历。通常情况下，我们都只能通过搜索或一个一个打开查看，当然这样会花费不少时间进行重复劳动。考虑到这一点，我们就有必要想一个办法对

  Ubuntu 文件进行快速预览，以尽可能减少查找文件的时间。

通过费心找寻，终于找到了 GNOME Sushi

工具这种可在不打开文件的前提下，对 Ubuntu 中文件进行快速预览的办法，该方法非常类似于  Mac OS X

中的快速查看功能。下面我们就对此办法进行详细介绍，在此之前也提醒大家注意一下，目前该方法只在 Ubuntu 18.04 LTS 

中进行测试，其它版本和 Ubuntu 用户需要自行试验。

Ubuntu中快速预览文件

由于 Ubuntu 默认不支持快速预览，所以我们必需手动安装一款名为 GNOME Sushi 的快速预览工具，自 GNOME Sushi 官方  GitHub 页面所述，它完全兼容 Nautilus GNOME 桌面文件管理器的快速预览。

GNOME Sushi 已在 Ubuntu 官方源中进行提供，你可以在「Ubuntu 软件」中搜索安装或在终端中使用如下命令进行安装：

`sudo apt install gnome-sushi`

![image](https://upload-images.jianshu.io/upload_images/14555448-3fe271fdcb78813f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

gnome-sushi 安装好之后，Ubuntu 会自动启用快速预览功能，用户可以通过 空格键 对任意选中的文件进行快速预览，其中包括文本、图片、视频甚至  Bash 脚本等。

GNOME Sushi 的预览模式也不仅限于一种，在打开预览窗口后，大家可通过键盘 F 键 来进行预览模式的切换，也可使用 ESC  或再按空格键来结束预览。

除了常见文档类型外，该工具还支持包括 HTML 和 PDF  在内的富文档类型，但对于文件夹来说，它只能显示目录大小、项目数和上次修改的日期和时间等元数据信息。

不用多说，在

Ubuntu 以及其他支持 Nautilus 的 Linux 

发行版上，「快速预览」功能可为你节省大量的时间。如果你的日常工作涉及在大量不同文件类型，GNOME Sushi 

解决方案非常值得一试。最后需要一提，该工具对视频文件的快速预览做得也非常不错，大家亲自一试吧。
