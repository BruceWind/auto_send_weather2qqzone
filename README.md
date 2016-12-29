
## Base on:[https://github.com/ShomyLiu/qqzone](https://github.com/ShomyLiu/qqzone)
利用 模拟登录qq空间的工具，发送说说，把当前的天气发出去

## 核心功能介绍 -> [点我跳转](https://github.com/ShomyLiu/qqzone)

## 普通x86 x64 机器使用 :

1.先手动修改info.conf中的qq 和 密码

2.运行 setup.sh文件

完成之后，每小时发一条说说到qq空间，但是如果两条内容相同，会干掉之前的那条，发出新的这条,没有刷屏的垃圾信息。 不要设置的过于频繁，过于频繁 会导致 qq空间拒绝。


## arm机器 或者 树莓派使用

![](https://github.com/weizongwei5/my_blog_datasave/raw/eea7eb1b0698b380975a804cf2b812ae409b72a7/img/no_display_install_rpi.png)

setup.sh文件中有个`wget xxxlinux-x86_x64.zip` 的过程无法再用，arm平台需要手动编译pyv8。

树莓派下编译，需要增大swap空间，增大虚拟内存，不然内存会不够，如果不先修改swap空间，然后看着板子温度跑到85度花了20分钟时间,结果报错，然后你又要重新编译，就哭吧！

编译教程如下：[https://buffer.github.io/thug/doc/build.html](https://buffer.github.io/thug/doc/build.html)
