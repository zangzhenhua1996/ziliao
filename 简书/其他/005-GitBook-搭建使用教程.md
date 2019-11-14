## GitBook 简介

*   [GitBook 官网](https://link.jianshu.com/?t=https%3A%2F%2Fwww.gitbook.com)
*   [GitBook 文档](https://link.jianshu.com/?t=https%3A%2F%2Fgithub.com%2FGitbookIO%2Fgitbook)
## GitBook 准备工作

### 安装 Node.js

GitBook 是一个基于 Node.js 的命令行工具，下载安装 [Node.js](https://link.jianshu.com/?t=https%3A%2F%2Fnodejs.org%2Fen)，安装完成之后，你可以使用下面的命令来检验是否安装成功。
```bash
$ node -v
v12.13.0
```
下面看一下安装node.js的过程  
1. 下载安装包  
![image.png](https://upload-images.jianshu.io/upload_images/14555448-ad0ec9f8a21385e9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2.安装
![image.png](https://upload-images.jianshu.io/upload_images/14555448-7169cdfd738fc88c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/14555448-472099ccf45cae4a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/14555448-ba91289424548d62.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/14555448-cddbc14ad5b4bf7b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/14555448-9e47ca979a8997f4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/14555448-6e82a09410911fce.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/14555448-1221cfd06767716e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/14555448-eaff3971ce01b10d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/14555448-a800c9eb7f446b69.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
### 安装gitbook
输入下面的命令来安装 GitBook。
```bash
npm install gitbook-cli -g
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-1e83cd1c9ceb8c06.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
安装过程较为缓慢请耐心等待
![image.png](https://upload-images.jianshu.io/upload_images/14555448-b00815478d255ae4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
安装完成之后，你可以使用下面的命令来检验是否安装成功。
```
$ gitbook -V
CLI version: 2.3.2
GitBook version: 3.2.3
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-16cf5ae84fb65b87.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/14555448-9e9834896b554661.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
更多详情请参照 [GitBook 安装文档](https://github.com/GitbookIO/gitbook/blob/master/docs/setup.md) 来安装 GitBook。

### 安装 GitBook 编辑器

去 [GitBook 官网](https://www.gitbook.com/) 下载 GitBook 编辑器；如果是 Mac 用户且安装过 `brew cask` 的话可以使用 `brew cask install gitbook-editor` 命令行来安装 GitBook 编辑器。
我没有下载到,在这个网址进行的下载[https://www.jb51.net/softs/502206.html#downintro2](https://www.jb51.net/softs/502206.html#downintro2)


### 先睹为快
GitBook 准备工作做好之后，我们进入一个你要写书的目录，输入如下命令。
```bash
$ gitbook init
warn: no summary file in this book
info: create README.md
info: create SUMMARY.md
info: initialization is finished
```
可以看到他会创建 README.md 和 SUMMARY.md 这两个文件，README.md 应该不陌生，就是说明文档，而 SUMMARY.md 其实就是书的章节目录，其默认内容如下所示：

```bash
# Summary

* [Introduction](README.md)
```
接下来，我们输入 `gitbook serve` 命令，然后在浏览器地址栏中输入` http://localhost:4000` 便可预览书籍。

效果如下所示：

![image.png](https://upload-images.jianshu.io/upload_images/14555448-0e8e975135e9f5c3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

运行下面的命令后会在书籍的文件夹中生成一个 _book 文件夹, 里面的内容即为生成的 html 文件，我们可以使用下面命令来生成网页而不开启服务器。
```bash
gitbook build
```

下面我们来详细介绍下 GitBook 目录结构及相关文件。


### 目录结构
GitBook 基本的目录结构如下所示：
```bash
.
├── book.json
├── README.md
├── SUMMARY.md
├── chapter-1/
|   ├── README.md
|   └── something.md
└── chapter-2/
    ├── README.md
    └── something.md
```
下面我们主要来讲讲 book.json 和 SUMMARY.md 文件。
#### book.json
该文件主要用来存放配置信息，我先放出我的配置文件。

```bash
{
    "title": "Blankj's Glory",
    "author": "Blankj",
    "description": "select * from learn",
    "language": "zh-hans",
    "gitbook": "3.2.3",
    "styles": {
        "website": "/styles/website.css"
    },
    "structure": {
        "readme": "README.md"
    },
    "links": {
        "sidebar": {
            "我的狗窝": "https://blankj.com"
        }
    },
    "plugins": [
        "-sharing",
        "splitter",
        "expandable-chapters-small",
        "anchors",

        "github",
        "github-buttons",
        "donate",
        "sharing-plus",
        "anchor-navigation-ex",
        "favicon"
    ],
    "pluginsConfig": {
        "github": {
            "url": "https://github.com/Blankj"
        },
        "github-buttons": {
            "buttons": [{
                "user": "Blankj",
                "repo": "glory",
                "type": "star",
                "size": "small",
                "count": true
                }
            ]
        },
        "donate": {
            "alipay": "https://blankj.com/gitbook/source/images/donate.png",
            "title": "",
            "button": "赞赏",
            "alipayText": " "
        },
        "sharing": {
            "douban": false,
            "facebook": false,
            "google": false,
            "hatenaBookmark": false,
            "instapaper": false,
            "line": false,
            "linkedin": false,
            "messenger": false,
            "pocket": false,
            "qq": false,
            "qzone": false,
            "stumbleupon": false,
            "twitter": false,
            "viber": false,
            "vk": false,
            "weibo": false,
            "whatsapp": false,
            "all": [
                "google", "facebook", "weibo", "twitter",
                "qq", "qzone", "linkedin", "pocket"
            ]
        },
        "anchor-navigation-ex": {
            "showLevel": false
        },
        "favicon":{
            "shortcut": "./source/images/favicon-32x32.webp",
            "bookmark": "./source/images/favicon-32x32.webp",
            "appleTouch": "./source/images/apple-touch-icon.webp"
        }
    }
}
```

相信很多节点自己也能猜到是什么意思，我还是简单介绍下吧。

#### title
本书标题

#### author
本书作者

#### description
本书描述

#### language
本书语言，中文设置 "zh-hans" 即可

#### gitbook
指定使用的 GitBook 版本

#### styles
自定义页面样式

#### structure
指定 Readme、Summary、Glossary 和 Languages 对应的文件名

#### links
在左侧导航栏添加链接信息

#### plugins
配置使用的插件

#### pluginsConfig
配置插件的属性


## 更加详细的解释
## 4\. gitbook的配置文件讲解

如果你想对你的网站有更详细的个性化配置或使用插件，那么需要使用配置文件。
配置文件写完后，需要重启服务或者重新打包才能应用配置。
gitbook的配置文件名是`book.json`，首先在项目的根目录中创建`book.json`文件。
`book.json`主要内容：

```
{
    "title": "我的一本书",
    "author" : "yu",
    "description" : "我第一本书的描述，很好",
    "language" : "zh-hans",
    "structure": {
        "readme": "introduction.md"
    },
    "plugins": [
        "-lunr",
        "-search",
        "search-pro",
        "back-to-top-button"
    ],
    "pluginsConfig": {
        "anchor-navigation-ex": {
            "isShowTocTitleIcon": true
        }
    },
    "links" : {
        "sidebar" : {
            "个性链接1" : "https://www.baidu.com",
            "个性链接2" : "https://www.baidu.com"
        }
    },
    "styles": {
        "website": "styles/website.css",
        "ebook": "styles/ebook.css",
        "pdf": "styles/pdf.css",
        "mobi": "styles/mobi.css",
        "epub": "styles/epub.css"
    }
}
```

更多的配置参数：[https://github.com/GitbookIO/...](https://github.com/GitbookIO/gitbook/blob/master/docs/config.md)

### 4.1 book.json中一些主要参数说明

*   title
    标题
*   author
    作者
*   description
    描述，对应gitbook网站的description
*   language
    使用的语言，`zh-hans`是简体中文，会对应到页面的`<html lang="zh-hans" >`
*   structure
    指定 Readme、Summary、Glossary 和 Languages 对应的文件名，下面是这几个文件对应变量以及默认值：

    | Variable | Description |
    | --- | --- |
    | `structure.readme` | Readme file name (defaults to `README.md`) |
    | `structure.summary` | Summary file name (defaults to `SUMMARY.md`) |
    | `structure.glossary` | Glossary file name (defaults to `GLOSSARY.md`) |
    | `structure.languages` | Languages file name (defaults to `LANGS.md`) |

    比如想把readme文件个名字，则可以使用如下配置

    ```
    "structure": {
        "readme": "introduction.md"
    },
    ```

    使用这个配置后，gitbook服务就不会找readme文件，而去找`introduction`文件当项目说明，这样就可以把readme文件完全当成代码仓库说明文档了。

*   plugins
    使用的插件列表，所有的插件都在这里写出来，然后使用`gitbook install`来安装。
![image.png](https://upload-images.jianshu.io/upload_images/14555448-137142e5a9555a82.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

*   pluginsConfig
    插件的配置信息，如果插件需要配置参数，那么在这里填写。
*   links
    目前可以给侧导航栏添加链接信息

    ```
    "links" : {
        "sidebar" : {
            "个性链接1" : "https://www.baidu.com"
        }
    }
    ```

*   styles
    自定义页面样式，各种格式对应各自的css文件

    ```
    "styles": {
        "website": "styles/website.css",
        "ebook": "styles/ebook.css",
        "pdf": "styles/pdf.css",
        "mobi": "styles/mobi.css",
        "epub": "styles/epub.css"
    }
    ```

### 4.1 配置默认主题

默认的主题可以通过配置来做一下效果。
比如侧边栏菜单显示标题数字，可以在配置文件的`pluginsConfig`参数中写入如下字段：

```
{
    "pluginsConfig": {
        "theme-default": {
            "showLevel": true
        }
    }
}
```

效果如下图：

![image.png](https://upload-images.jianshu.io/upload_images/14555448-b21d338d1f32273b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
## 5\. gitbook的一些实用插件

gitbook插件可以解决一些网站不太方便的地方，如侧边栏导航不能收缩，自带搜索不支持中文等。
用了插件书籍网站会更灵活和美观。

由于插件很多，请参考这篇文章：[https://segmentfault.com/a/11...](https://segmentfault.com/a/1190000019806829)


### SUMMARY.md
这个文件主要决定 GitBook 的章节目录，它通过 Markdown 中的列表语法来表示文件的父子关系，下面是一个简单的示例：
```bash
# Summary

* [Introduction](README.md)
* [Part I](part1/README.md)
    * [Writing is nice](part1/writing.md)
    * [GitBook is nice](part1/gitbook.md)
* [Part II](part2/README.md)
    * [We love feedback](part2/feedback_please.md)
    * [Better tools for authors](part2/better_tools.md)
```
这个配置对应的目录结构如下所示:

![image.png](https://upload-images.jianshu.io/upload_images/14555448-8eecd1cfa02b03c5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
我们通过使用 标题 或者 水平分割线 将 GitBook 分为几个不同的部分，如下所示：
```bash
# Summary

### Part I

* [Introduction](README.md)
* [Writing is nice](part1/writing.md)
* [GitBook is nice](part1/gitbook.md)

### Part II

* [We love feedback](part2/feedback_please.md)
* [Better tools for authors](part2/better_tools.md)

---

* [Last part without title](part3/title.md)
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-3fd6e0527b75951e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

如果SUMMARY.md文件里面有如下内容：
```bash
* [项目介绍](README.md)
* http
    * [http说明](doc/http/http解析.md)
        * [tcp说明](doc/http/tcp/tcp说明.md)
            * [udp说明](doc/http/tcp/udp/udp说明.md)
* HTML
    * [HTML5-特性说明](doc/html/HTML5-特性说明.md)
```
那么在使用gitbook init时，如果目录里面的文件不存在，则会创建目录中的文件：
```bash
~ gitbook init

info: create doc/http/http解析.md 
info: create doc/http/tcp/tcp说明.md 
info: create doc/http/tcp/udp/udp说明.md 
info: create doc/html/HTML5-特性说明.md 
info: create SUMMARY.md 
info: initialization is finished 
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-2bf7fdabb903514e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 插件

GitBook 有 [插件官网](https://plugins.gitbook.com/)，默认带有 5 个插件，highlight、search、sharing、font-settings、livereload，如果要去除自带的插件， 可以在插件名称前面加 `-`，比如：
```bash
"plugins": [
    "-search"
]
```
如果要配置使用的插件可以在 book.json 文件中加入即可，比如我们添加 [plugin-github](https://plugins.gitbook.com/plugin/github)，我们在 book.json 中加入配置如下即可：
```bash
{
    "plugins": [ "github" ],
    "pluginsConfig": {
        "github": {
            "url": "https://github.com/your/repo"
        }
    }
}
```
然后在终端输入 gitbook install ./ 即可。

如果要指定插件的版本可以使用 plugin@0.3.1，因为一些插件可能不会随着 GitBook 版本的升级而升级。

## 项目部署到GitHub Pages
这部分需要使用git和github网站，如果你不会，请自行在网上搜索文档查看。

由于gitbook生成的项目跟文档的源码是两个部分，所以可以把文档放到master分支上，部署的网站放到gh-pages 分支。

#### 1. 在github上创建一个仓库

这个仓库用于存放你编写的项目，和部署项目，如何创建请自行查找。

#### 2. 本地项目提交到github仓库

在项目中创建一个`.gitignore`文件，内容如下：

```
# 忽略gitbook生成的项目目录
_book
```

然后终端打开项目，输入如下命令,来提交文档项目到github上：

```
~ git init
~ git add .
~ git commit -m '初始化gitbook本地项目'
~ git remote add origin https://github.com/yulilong/book.git 
~ git push -u origin master
```

上面命令执行结束后，就会把代码提交到github上的仓库。
***注意仓库地址要替换成你自己的链接。***

#### 3. 生成项目并上传到github仓库的gh-pages分支

由于打包命令太多，为了简单化，现在写一个脚本命令来自动执行。当然你也可以终端自己执行这些命令。

为了部署方便，可以创建一个脚本文件`deploy.sh`,内容如下：

```
#!/usr/bin/env sh

echo '开始执行命令'
# 生成静态文件
echo '执行命令：gitbook build .'
gitbook build .

# 进入生成的文件夹
echo "执行命令：cd ./_book\n"
cd ./_book

# 初始化一个仓库，仅仅是做了一个初始化的操作，项目里的文件还没有被跟踪
echo "执行命令：git init\n"
git init

# 保存所有的修改
echo "执行命令：git add -A"
git add -A

# 把修改的文件提交
echo "执行命令：commit -m 'deploy'"
git commit -m 'deploy'

# 如果发布到 https://<USERNAME>.github.io/<REPO>
echo "执行命令：git push -f https://github.com/yulilong/book.git master:gh-pages"
git push -f https://github.com/yulilong/book.git master:gh-pages

# 返回到上一次的工作目录
echo "回到刚才工作目录"
cd -
```

注意脚本文件代码中仓库地址要替换成你自己的地址。

文件保存后，在终端执行如下命令开始把最终项推送到`gh-pages`分支：

```
bash deploy.sh
```

执行成功后，打开你的github仓库，然后选择`branch`分支，会发现多了一个`gh-pages`分支，打开这个分之后，里面会有一个`index.html`文件。说明部署的代码上传成功了。
**注意：如果没有`gh-pages`分支说明没有部署成功请查看刚才执行的终端看哪里报错了，解决报错直到成功部署。**

#### 4. 配置GitHub Pages显示网站

在github网站上的仓库里面点击`Settings` -> `GitHub Pages`选项中 -> `Source`里面选择`gh-pages branch` 然后点击`Save`按钮，然后在`GitHub Pages`下面就会看见一个网址，这个网址就是最终的网站。
最终效果如下图所示：
![image.png](https://upload-images.jianshu.io/upload_images/14555448-b4dab5788972fa32.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


### 5. 一些部署到GitHub Pages的例子

[https://github.com/yodaos-pro...](https://github.com/yodaos-project/yoda-book)

[http://gitbook.zhangjikai.com...](http://gitbook.zhangjikai.com/plugins.html)
