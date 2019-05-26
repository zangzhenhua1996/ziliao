在局域网内`Ubuntu`和`Windows`之间实现共享文件教程

在局域网内Ubuntu和Windows之间也是可以实现共享文件的，那么Ubuntu和Windows之间怎么共享文件，下面以图文的形式为大家详细介绍下

　　很多人对Ubuntu共享文件盒Windows共享文件都比较熟悉，也知道怎么在局域网内Ubuntu和Windows各自的系统之间怎么共享文件。其实在局域网内Ubuntu和Windows之间也是可以实现共享文件的，那么Ubuntu和Windows之间怎么共享文件呢？

在Ubuntu上实现局域网共享文件夹

　　如果你的系统是Ubuntu 14.04、14.10或12.04，有两个方法可以使你通过局域网在搭载Windows或其他Linux的电脑上共享本地文件。

　　对局域网中的每个用户提供无密码共享

　　仅限特定访问，提供文件夹密码保护

　　这篇文章包括两种方法，你可以选择你想用的那种

1. 局域网无密码共享文件夹

　　步骤一：

　　为了在Ubuntu上实现局域网共享文件夹，右键点击打算共享的文件夹，并选择“Local Network Share（本地网络共享）”：

可能有用的故障解决方案：如果在右键菜单中看不到“Local Network Share”的选项，那就新建一个终端，使用下面的命令去安装nautlius-share插件：

　`　sudo apt-get install nautilus-share`

　　然后重启Nautilus。可以选择注销再登录，或者使用这个命令：

`　　nautilus -q`

　　步骤二：

　　一旦点击“Local Network Share”，就会出现共享文件夹的选项。只需选中“Share this folder（共享该文件夹）”这一项：

　　可能的故障解决方案：如果提示共享服务还未安装，就像下图所示，那就点击安装服务，按照提示操作。

　　步骤三：

　　当选中“Share this folder”的选项，就会看到按钮“Create

Share（创建共享）”变得可以点击了。你也可以“Allow others to create and delete fies in this

folder（允许其他用户在共享文件夹中编辑文件）”。选项“Guest access（允许访客访问）”也是如此。

　　你会看到文件夹图标已经显示为共享的。如果要停止共享文件夹，只需取消“Share this floder”这个选项。

这个方法就是这么简单，使得局域网中的任何人都可以访问共享文件夹中的文件。在正常情况下，你会选择这种方式。因为，家用局域网中的电脑通常都是可信电脑。但情况也不总是这样。如果你只是想特定的用户才能访问怎么办？这个时候就需要Samba服务器了。我们在本文的第二部分讨论这种方法。上一页12下一页共2页

　　2. 在Ubuntu上使用密码保护实现局域网共享文件夹

　　为了达到这个目的，首先需要配置Samba服务器。事实上，在这篇教程的前一部分我们已经用到了Samba，只是我们没有刻意强调。在介绍如何在Ubuntu上搭建Samba服务器实现局域网共享的方法之前，先快速预览一下Samba到底是什么。

　Samba是什么？

　　Samba是一个允许用户通过网络共享文件、文档和打印机的软件包，无论是在Linux、Windows，还是Mac上。它适用于所有的主流平台，可以在所有支持系统上流畅运行。下面是维基百科的介绍：

　　Samba是一款重新实现SMB/CIFS网络协议的自由软件，最初由安德鲁·垂鸠开发。在第三版中，Smaba不仅支持通过不同的Windows客户端访问及分享SMB的文件夹及打印机，还可以集成到Windows

Server域，作为主域控制器（PDC）或者域成员。它也可以作为活动目录域的一部分。

　　在Ubuntu上安装Samba服务器

　　你可以很方便地在Ubuntu电脑上安装Samba。安装前，请先更新系统以便安装任何可用的更新。

`　　sudo apt-get update && apt-get upgrade`

　　然后按照这条命令安装samba和少量所需的软件包：

`　　sudo apt-get install samba samba-common system-config-samba python-glade2 gksu`

　　一旦安装完成Samba服务器，就可以从图形界面配置Samba来分享文件。

　　Ubuntu和Windows之间怎么共享文件就为大家介绍到这里了。其实不仅是Ubuntu系统，在Linux其他系统上这个方法也是同样有用的。
