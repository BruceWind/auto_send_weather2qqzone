import requests
import json
url = r'http://wthrcdn.etouch.cn/weather_mini?citykey=101021300'
jsonStr = requests.get(url).text
data = eval(json.dumps(jsonStr,ensure_ascii=False))
exec("Data="+data)
info = Data["data"]
weather = info["forecast"]
print(info['city'].decode("utf-8"))
forecast = info['forecast']

today = forecast[0]
print (today["date"].decode("utf-8"))
print (today["high"].decode("utf-8"))
print (today["low"].decode("utf-8"))
print (today["type"].decode("utf-8"))
print (today["fengxiang"].decode("utf-8"))
today = forecast[1]
print (today["date"].decode("utf-8"))
print (today["high"].decode("utf-8"))
print (today["low"].decode("utf-8"))
print (today["type"].decode("utf-8"))
print (today["fengxiang"].decode("utf-8"))
