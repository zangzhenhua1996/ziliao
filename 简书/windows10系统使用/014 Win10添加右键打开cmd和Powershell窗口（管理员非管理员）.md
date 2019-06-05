# [Win10添加右键在此处打开命令行](https://www.cnblogs.com/ssooking/p/8536468.html)

通过添加注册表项,实现右击**“在此处打开命令行功能”**

注册表位置：`HKEY_CLASSES_ROOT\Directory\Background\shell\`

win10系统用标识右键菜单打开命令行的键，键值639bc8（十六进制）：

`ShowBasedOnVelocityId`（显示标识）

`HideBasedOnVelocityId`（隐藏标识）

**效果**

　　直接右键即可看到该选项，无需同时按住shift键。当然，按住右键也能显示，并且不影响右键打开powershell的功能。

![image](http://upload-images.jianshu.io/upload_images/14555448-aa3035c51b6945c0.gif?imageMogr2/auto-orient/strip)

# 方法一：

一键自动导入设置。将以下内容保存成reg文件，如a.reg，双击该文件自动导入设置。
```bash
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\Background\shell\OpenCMDHere]
"ShowBasedOnVelocityId"=dword:00639bc8

[HKEY_CLASSES_ROOT\Directory\Background\shell\OpenCMDHere\command]
@="cmd.exe /s /k pushd \"%V\""
```
# 方法二：手工设置

1\. 我们用regedit或者其他注册表编辑器定位到HKEY_CLASSES_ROOT\Directory\Background\shell\处，右击新建项“OpenCMDHere”，并在该项下，右击新建项“command”。

![image](http://upload-images.jianshu.io/upload_images/14555448-a12ccef0ed585b2a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2.我们在右边OpenCMDHere项下，右击新建REG_DWORD类型整数值。设置键名为“ShowBasedOnVelocityId”，键值为“639bc8”。

![image](http://upload-images.jianshu.io/upload_images/14555448-4758fceda2bb5a71.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image](http://upload-images.jianshu.io/upload_images/14555448-0de69fc6224a47ec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

3.进入command项下，设置键值为cmd.exe /s /k pushd "%V"

![image](http://upload-images.jianshu.io/upload_images/14555448-22bc0dd81d3e691d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**版权声明：**