# encoding: utf-8
#!/usr/bin/env python

import requests
import json
class AQIGetter(object):


# 返回未转码的 字符串
    def getAQIStr(self,city):
        url = r'http://www.pm25.in/api/querys/pm2_5.json?city='+unicode(city, "utf-8")+'&token=fVtxPUxgpzQTnVNta5JL'
        # url = r'http://www.pm25.in/api/querys/pm2_5.json?city=%E4%BA%B3%E5%B7%9E&token=5j1znBVAsnSf5xQyNQyq&avg'
        jsonStr = requests.get(url).text

    # print jsonStr

        apiarr = json.loads(jsonStr)
        if(len(apiarr) > 0):
            lastobj=apiarr[0]
            area =lastobj['area']
            aqi = str(lastobj['aqi']).encode("utf-8")
            pm2_5_24h=str(lastobj['pm2_5_24h'])
            quality = lastobj['quality']

        # str = area+"\tAQI:"+aqi+" \t 各监测点平均PM2.5:"+pm2_5_24h +"\t "+quality
            return area+'\t\tAQI:'+aqi +u'\t\tPM2.5平均值：'.encode('utf-8').decode('utf-8')+pm2_5_24h+'\t\t'+quality


print  AQIGetter().getAQIStr('shanghai')
