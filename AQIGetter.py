# encoding: utf-8
#!/usr/bin/env python

import requests
import json
class AQIGetter(object):


# 返回未转码的 字符串
    def getAQIStr(self,city):
        url = r'http://www.pm25.in/api/querys/pm2_5.json?city='+unicode(city, "utf-8")+'&token=fVtxPUxgpzQTnVNta5JL&stations=no'
        # url = r'http://www.pm25.in/api/querys/pm2_5.json?city=%E4%BA%B3%E5%B7%9E&token=5j1znBVAsnSf5xQyNQyq&avg'
        temp = requests.get(url).text
        l=len(temp)-1
        jsonStr=temp[1:l]
        data = eval(json.dumps(jsonStr,ensure_ascii=False))
        exec("Data="+data)
        area =Data['area']
        aqi = str(Data['aqi']).encode('utf-8')
        pm2_5_24h=str(Data['pm2_5_24h']).encode('utf-8')
        quality = Data['quality']

    # str = area+"\tAQI:"+aqi+" \t 各监测点平均PM2.5:"+pm2_5_24h +"\t "+quality
        return area+"\tAQI:"+aqi+"\t PM2.5平均值:"+pm2_5_24h +"\t 空气质量 "+quality



# print  AQIGetter().getAQIStr('shanghai')
