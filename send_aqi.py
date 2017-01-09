#!/usr/bin/env python
# encoding: utf-8

from scrapyHandler import ScrapyHandler
from qq import QQ
import webHandler
import confReader
import os
import random
import time
import get_aqi_for_city
import requests
import json
import getpass

os.chdir("/home/"+getpass.getuser()+"/git/auto_send_weather2qqzone")
web = webHandler.WebHandler()
cf=confReader.ConfReader()

def getAQIStr():
    str=get_aqi_for_city.AQIGetter().getAQIStr('shanghai')+"\n"+get_aqi_for_city.AQIGetter().getAQIStr('nanjing')+"\n"+get_aqi_for_city.AQIGetter().getAQIStr('bozhou')
    return str.encode('utf-8')


def getFooter():
    return cf.getFooter()


def func(hostqq, url, tp):
    try:
        data = web.Request(url, type=tp)
        pic = file('%s/%s.%s' %(hostqq, str(random.random()), tp), 'wb')
        pic.write(data)
        pic.close()
    except Exception, e:
        print str(e)


def multi(qq):
    '''
    多线程爬取
    '''
    numthread = cf.get('info', 'numthread')
    s = ScrapyHandler(qq.picUrl, int(numthread), func)
    s.wait_allfinish()



def login():
    qqNum = cf.getQQ()
    pwd = cf.getPwd()

    qq = QQ(qqNum, pwd)
    qq.login()
    return qq



if __name__ == '__main__':


    time.sleep(1)
    # print(getAQIStr()+"\n"+getFooter())
    qq = login()  # 登录入口
    qq.publishMessage(getAQIStr()+"\n"+getFooter()) # +"\n"+time.ctime()