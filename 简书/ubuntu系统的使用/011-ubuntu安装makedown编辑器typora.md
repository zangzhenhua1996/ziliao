参考官方链接:[https://support.typora.io/Typora-on-Linux/](https://support.typora.io/Typora-on-Linux/)
Debian/Ubuntu
# or use
# sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE

#安装公钥:推荐这种
 ```wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -```

# 添加Typora仓库
```sudo add-apt-repository 'deb https://typora.io/linux ./```
#软件源更新
```sudo apt-get update```

# 安装typora
```sudo apt-get install typora```
