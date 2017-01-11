利用 模拟登录qq空间的工具，发送说说，把当前的天气或者AQI发出去。树莓派可以利用crontab功能发送。

**所有python代码，以及自动化设置的shell脚本都在这个[github地址](https://github.com/weizongwei5/auto_send_weather2qqzone)。**

## 核心功能介绍 -> [点我跳转](https://github.com/ShomyLiu/qqzone)

## 普通x86 x64 机器使用 :

1.先手动修改info.conf中的qq 和 密码

2.运行 setup.sh文件

完成之后，每小时发一条说说到qq空间，但是如果两条内容相同，会干掉之前的那条，发出新的这条,没有刷屏的垃圾信息。 不要设置的过于频繁，过于频繁 会导致 qq空间拒绝。


## arm机器 或者 树莓派使用

![](https://github.com/weizongwei5/my_blog_datasave/raw/eea7eb1b0698b380975a804cf2b812ae409b72a7/img/no_display_install_rpi.png)

setup.sh文件中有个`wget xxxlinux-x86_x64.zip` 的过程无法再用，这个文件是x86x64架构下的依赖库，arm平台需要手动编译pyv8。

树莓派下编译，需要增大swap空间，增大虚拟内存，不然内存会不够，如果不先修改swap空间，然后看着板子温度跑到85度花了20分钟时间,结果报错，然后你又要重新编译，就哭吧！

编译教程如下：[https://buffer.github.io/thug/doc/build.html](https://buffer.github.io/thug/doc/build.html)


## 更多玩法
这个这个仓库，没有什么真实的中心功能，中心不是取天气，也不AQI，也不是发说说，也不是contable，核心功能就是玩法。

玩家可以自由替换，比如把天气发到qq空间，改为发送到短信，找第三方短信平台，发送到微博各种搭配，可以自由玩。
