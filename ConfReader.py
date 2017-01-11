#!/usr/bin/env python
# encoding: utf-8
######################
# 由于在linux下做硬链接 执行命令时的pwd 是/home/username下  所以这里需要先childdir
import ConfigParser

class ConfReader(object):

    cf = ConfigParser.ConfigParser()

    def __init__(self):
        self.cf.read('info.conf')


    def getQQ(self):

        return self.cf.get('info', 'qq')


    def getPwd(self):
        return self.cf.get('info', 'pwd')


    def getFooter(self):
        return self.cf.get('info', 'footer')
