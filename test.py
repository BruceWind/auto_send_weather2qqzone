#!/usr/bin/env python
# encoding: utf-8

from scrapyHandler import ScrapyHandler
from qq import QQ
import webHandler
import ConfigParser
import os
import random
import time
import get_weather
import requests
import json


url = r'http://wthrcdn.etouch.cn/weather_mini?citykey=101020100'



web = webHandler.WebHandler()

cf = ConfigParser.ConfigParser()
cf.read('info.conf')


def getWeatherStrUtf8():
    jsonStr = requests.get(url).text
    data = eval(json.dumps(jsonStr,ensure_ascii=False))
    exec("Data="+data)
    info = Data["data"]
    weather = info["forecast"]
    forecast = info['forecast']

    today = forecast[0]
    str_today=info['city']+"\n"+today["type"]+"\t\t"+today["fengxiang"] + "\n" + today["high"] + "\t" + today["low"]+"\n"+info["ganmao"]
    return str_today

def parse():
    '''
    从info.conf中读取配置信息
    '''
    qq = cf.get('info', 'qq')
    pwd = cf.get('info', 'pwd')
    footer = cf.get('info', 'footer')
    return qq, pwd

def getFooter():
    return cf.get('info', 'footer')


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
    # method ='2' # raw_input('选择方式登录:1.二维码;2.帐号密码;\n')
    # if method == '1':
    #     qq = QQ(method='1')
    #     qq.login()
    # elif method == '2':  # 从配置文件读取信息
    #     qqNum, pwd = parse()
    #     #  qqNum = raw_input('输入QQ号:')
    #     #  qqPwd = raw_input('输入密码:')
    #     qq = QQ(qqNum, pwd)
    #     qq.login()
    # else:
    #     print '请输入1,或者2'
    qqNum, pwd = parse()
    qq = QQ(qqNum, pwd)
    qq.login()
    return qq

if __name__ == '__main__':

    qq = login()  # 登录入口
    qq.publishMessage(getWeatherStrUtf8()+"\n"+getFooter()) # +"\n"+time.ctime()
