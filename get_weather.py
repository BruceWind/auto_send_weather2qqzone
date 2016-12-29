#!/usr/bin/env python
# encoding: utf-8

import requests
import json

url = r'http://wthrcdn.etouch.cn/weather_mini?citykey=101020100'

# 返回未转码的 字符串
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


# 返回utf-8转转码之后的 字符串 可用于 print输出
def getWeatherStr():
    jsonStr = requests.get(url).text
    data = eval(json.dumps(jsonStr,ensure_ascii=False))
    exec("Data="+data)
    info = Data["data"]
    weather = info["forecast"]
    forecast = info['forecast']

    today = forecast[0]
    str_today=info['city'].decode("utf-8")+"\n"+today["date"].decode("utf-8") + "\n" + today["high"].decode("utf-8") + "\n" + today["low"].decode("utf-8")+"\n"+today["type"].decode("utf-8")+"\n"+today["fengxiang"].decode("utf-8")
    return str_today

print "\n"
print getWeatherStrUtf8()
print "\n"
