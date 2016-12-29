#!/usr/bin/env python
# encoding: utf-8

from scrapyHandler import ScrapyHandler
from qq import QQ
import webHandler
import confReader
import os
import random
import time
import get_weather
import requests
import json

url = r'http://wthrcdn.etouch.cn/weather_mini?citykey=101020100' #城市id 上海 
os.chdir("/home/wei/git/auto_send_weather2qqzone")
web = webHandler.WebHandler()
cf=confReader.ConfReader()

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
    qq = login()  # 登录入口
    qq.publishMessage(getWeatherStrUtf8()+"\n"+getFooter()) # +"\n"+time.ctime()
