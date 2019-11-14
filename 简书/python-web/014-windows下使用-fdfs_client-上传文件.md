# windows下使用 fdfs_client 上传文件

**目录**

*   windows 下使用 fdfs_client 实现文件上传
    *   1、安装 fdfs_client 模块
    *   2、修改 fdfs_client/storage_client.py 文件
    *   3、安装 mutagen 和 requests
    *   4、修改 fastdfs 配置文件: client_config
    *   5、文件上传测试

* * *

> 在上一篇中介绍了使用 FastDFS 与 Nginx 在 Linux 系统上实现分布式图片服务器，现在介绍在 windows 系统下使用该分布式图片服务器。
> 需要安装 fdfs_client 模块和配置 client.conf 配置文件。
> 下载 fdfs_client 模块和 client.conf 配置文件：[点我下载](https://files.cnblogs.com/files/kindleheart/windows%E4%B8%8B%E4%BD%BF%E7%94%A8fdfs.zip)


## windows 下使用 fdfs_client 实现文件上传

### 1、安装 fdfs_client 模块

在 windows 环境下使用 `pip install fdfs_client` 会报错，所以直接安装是不行的，但是可以直接把已经下载好的 fdfs_client 模块 copy 到 python解释器的 /lib 文件夹中。

### 2、修改 fdfs_client/storage_client.py 文件

需要修改 fdfs_client 模块中的 storage_client.py 文件，将第12行删除或注释（否则使用时会报错 ImportError: No module named sendfile）

### 3、安装 mutagen 和 requests

```
pip install mutagen
pip install requests
```

### 4、修改 fastdfs 配置文件: client_config

① 修改 base_path 为你 windows 电脑一个真实存在的文件夹

例如：

```
base_path=E:\fdfs_log
```

② 修改 tracker_server 为你 Linux 系统的 IP 地址 + :22122

例如：

```
tracker_server=192.168.159.140:22122
```

```
# connect timeout in seconds
# default value is 30s
connect_timeout=30

# network timeout in seconds
# default value is 30s
network_timeout=60

# the base path to store log files
base_path=E:\fdfs_log

# tracker_server can ocur more than once, and tracker_server format is
#  "host:port", host can be hostname or ip address
tracker_server=192.168.159.140:22122

#standard log level as syslog, case insensitive, value list:
### emerg for emergency
### alert
### crit for critical
### error
### warn for warning
### notice
### info
### debug
log_level=info

# if use connection pool
# default value is false
# since V4.05
use_connection_pool = false

# connections whose the idle time exceeds this time will be closed
# unit: second
# default value is 3600
# since V4.05
connection_pool_max_idle_time = 3600

# if load FastDFS parameters from tracker server
# since V4.05
# default value is false
load_fdfs_parameters_from_tracker=false

# if use storage ID instead of IP address
# same as tracker.conf
# valid only when load_fdfs_parameters_from_tracker is false
# default value is false
# since V4.05
use_storage_id = false

# specify storage ids filename, can use relative or absolute path
# same as tracker.conf
# valid only when load_fdfs_parameters_from_tracker is false
# since V4.05
storage_ids_filename = storage_ids.conf

#HTTP settings
http.tracker_server_port=80

#use "#include" directive to include HTTP other settiongs
##include http.conf

```

### 5、文件上传测试

```
导入模块：
from fdfs_client.client import Fdfs_client

导入配置文件：
注意：windows环境下绝对路径会发生转义，需要加上 "r" 说明是原生字符串
client = Fdfs_client(r'配置文件绝对路径')

上传图片：
注意：windows环境下绝对路径会发生转义，需要加上 "r" 说明是原生字符串
client.upload_by_filename(r'图片文件绝对路径')
```

如果你看到如下画面你就成功了！！！

![image](https://upload-images.jianshu.io/upload_images/14555448-f4399ee455d0def7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
