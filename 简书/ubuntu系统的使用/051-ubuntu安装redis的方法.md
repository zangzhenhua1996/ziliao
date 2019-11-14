1.安装
`sudo  apt-get install redis-server `
2.检查Redis服务器系统进程
`ps -agx|grep redis`
3.查看tcp 连接
`netstat -ap | grep 6379`

4.启动：
服务：`redis-server      `

客户端：` redis-cli`
5.配置
修改 配置文件允许局域网内的其他电脑连接redis

文件位置：/etc/redis/redis.conf 如果无法编辑或者无法保存 请先修改权限
