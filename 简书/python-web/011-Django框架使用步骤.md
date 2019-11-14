### 1.创建项目
```python
django-admin startproject 项目名称
例：
django-admin startproject test1
```
### 2. 创建应用
```python
python manage.py startapp booktest
```
### 3.安装应用]
![image.png](https://upload-images.jianshu.io/upload_images/14555448-98ce01f489685b85.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
### 4.建立模板目录 templates
![image.png](https://upload-images.jianshu.io/upload_images/14555448-069c1b8d1fcc439b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
### 5. 添加模板目录的路径
![image.png](https://upload-images.jianshu.io/upload_images/14555448-5cdaee4a34d55f8a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
### 6. 数据库的修改(使用mysql数据库)
#### (1)创建一个新的数据库
![image.png](https://upload-images.jianshu.io/upload_images/14555448-7c59e788fca3317d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
(2) setting文件的配置

![数据库的配置](https://upload-images.jianshu.io/upload_images/14555448-1ed0b329cc5d68ae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
(3)__init__文件的配置
![image.png](https://upload-images.jianshu.io/upload_images/14555448-953d6245bbeb5962.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
(4) 迁移数据库
迁移由两步完成:
1.生成迁移文件：根据模型类生成创建表的迁移文件。
2.执行迁移：根据第一步生成的迁移文件在数据库中创建表。

生成迁移文件命令如下：
`python manage.py makemigrations`
执行迁移命令如下：(一开始没有模型类,只要迁移就行了不用创建迁移文件)
`python manage.py migrate`
![image.png](https://upload-images.jianshu.io/upload_images/14555448-235a2c8ed00d0c69.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 7.语言及地区的修改
![image.png](https://upload-images.jianshu.io/upload_images/14555448-022775eaea6b570e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
### 8. urls 路由的设置
#### (1)父路由
![image.png](https://upload-images.jianshu.io/upload_images/14555448-925040190a8ca650.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/14555448-b814e1befa025840.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#### (2)子路由
01 拷贝父路由到 booktest 这个应用文件夹
![image.png](https://upload-images.jianshu.io/upload_images/14555448-0318622fd50bfa86.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
02 路由的配置
删除不用的东西干干净净的
![image.png](https://upload-images.jianshu.io/upload_images/14555448-c7b92500ea7ef3ec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 9. 绑定ip跟端口开启服务器
![image.png](https://upload-images.jianshu.io/upload_images/14555448-8351a0eaffb2b30f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/14555448-96b2076637253357.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
出现这里是因为没有迁移数据库(到前面的地方检查)
由于没有创建模型类,因此只需要迁移就行
![image.png](https://upload-images.jianshu.io/upload_images/14555448-937fa917690b30a3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 10.浏览器输入ip
![image.png](https://upload-images.jianshu.io/upload_images/14555448-e36d74d9c3d67833.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



啰里啰嗦的使用过程
### 11 模型类的创建
![image.png](https://upload-images.jianshu.io/upload_images/14555448-35843298b28580ab.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


#### 富文本编辑器的使用参考html文档

富文本编辑器
借助富文本编辑器，网站的编辑人员能够像使用offfice一样编写出漂亮的、所见即所得的页面。此处以tinymce为例，其它富文本编辑器的使用也是类似的。

在虚拟环境中安装包。

`pip install django-tinymce==2.6.0`
安装完成后，可以使用在Admin管理中，也可以自定义表单使用。

示例
1）在test6/settings.py中为INSTALLED_APPS添加编辑器应用。
```
INSTALLED_APPS = (
    ...
    'tinymce',
)
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-d011e1a3702dbebc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2）在test6/settings.py中添加编辑器配置。
```
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 600,
    'height': 400,
}
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-4158ed2ca6071fcf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

3）在test6/urls.py中配置编辑器url。
```
urlpatterns = [
    ...
    url(r'^tinymce/', include('tinymce.urls')),
]
```
![image.png](https://upload-images.jianshu.io/upload_images/14555448-54df95c64acbe006.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

接下来介绍在Admin页面、自定义表单页面的使用方式。
### 在Admin中使用
1）在booktest/models.py中，定义模型的属性为HTMLField()类型。
![image.png](https://upload-images.jianshu.io/upload_images/14555448-e4a8fe5f70fc27d4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 数据库迁移
![image.png](https://upload-images.jianshu.io/upload_images/14555448-dca4b69b5d1fe5c4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/14555448-c754b9b4990bcd0d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#### 后台注册
![image.png](https://upload-images.jianshu.io/upload_images/14555448-ebd4058ebcc5e520.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#### 后台管理员的创建
1.创建管理员
创建管理员的命令如下，按提示输入用户名、邮箱、密码。
`python manage.py createsuperuser`
![image.png](https://upload-images.jianshu.io/upload_images/14555448-4c4a640b38af6c1f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2. 登录后台管理
![image.png](https://upload-images.jianshu.io/upload_images/14555448-b0f6895693796202.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/14555448-2f0226fc908c88e9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/14555448-55a07b16ccaa03b3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
3. 进入goods tests 进行添加(一个商品状态,一个商品详情)
![image.png](https://upload-images.jianshu.io/upload_images/14555448-6a07785e1d2f072d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
4. 使得显示更加人性化
![image.png](https://upload-images.jianshu.io/upload_images/14555448-150058613c99df18.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/14555448-46e1c4799b912448.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
