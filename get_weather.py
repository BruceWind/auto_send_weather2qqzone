#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json

url="http://wthrcdn.etouch.cn/weather_mini?citykey=101210101"

def getHtml():
	return requests.get(url).text

data = json.loads(getHtml())
weather = data["data"]

print ("city:",weather["city"])
print ("prompt",weather["ganmao"])
