# ubuntu安装mysql没有让我设置密码

终端输入： sudo cat /etc/mysql/debian.cnf

显示内容：

# Automatically generated for Debian scripts. DO NOT TOUCH!
[client]
host     = localhost
user     = debian-sys-maint
password = PGBiNPneSGXRlayQ
socket   = /var/run/mysqld/mysqld.sock
[mysql_upgrade]
host     = localhost
user     = debian-sys-maint
password = PGBiNPneSGXRlayQ
socket   = /var/run/mysqld/mysqld.sock

其中有user和password可以用来登录，登录后再修改密码；

终端输入：mysql -u debian-sys-maint -p ，再输入密码后，进入ｍｙｓｑｌ中

mysql> 

在mysql客户端中输入依次输入以下内容：

mysql> show databases;
mysql> use mysql;
mysql> update user set authentication_string=PASSWORD("root") where user="root";

mysql> update user set plugin="mysql_native_password";
mysql> flush privileges;
mysql> quit;

其中PASSWORD后面的root可以为其他自定义的密码，

在终端中输入　sudo /etc/init.d/mysql restart;　命令，重启ｍｙｓｑｌ服务

使用新密码登录ｍｙｓｑｌ：mysql -u root -p

**卸载ｍｙｓｑｌ的命令：**

sudo apt purge mysql-*

 sudo rm -rf /etc/mysql/  /var/lib/mysql

sudo apt autoremove

**安装ｍｙｓｑｌ的命令**

sudo apt-get install mysql-client  mysql-server

**查看mysql状态**

sudo service mysql status

**查看mysql服务器端口**

sudo netstat -tap |grep mysql

**开启、停止和重启mysql服务**

sudo service mysql  start

sudo service mysql  stop

sudo service mysql  restart
