#!/usr/bin/python

from urllib import request, parse
import json

'reference: http://www.oschina.net/code/snippet_1993738_53664'

class Weather():
    def __init__(self):

        #cities dict, key is city name and value is city id
        self.cities = {
            '成都' : '01012703',
            '西充' : "0101271407"
        }
        self.city = '成都'

        #query interface
        self.uri = 'http://www.zuimeitianqi.com/zuimei/queryWeather'


    def query(self, city='成都'):
        #print("The city will be queryed is %s" %city)
        #check city
        if city not in self.cities:
            print("dosn't support current city[%s]" %city)
            return

        self.city = city
        reqData = parse.urlencode({'cityCode':self.cities[city]}).encode('utf-8')
        req = request.Request(self.uri)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36')
        with request.urlopen(req, reqData) as f:
            rep = f.read().decode('utf-8')

        # parse json
        self.parseJson(rep)

    def parseJson(self, rep):
        target = json.loads(rep)
        high_temp = target['data'][0]['actual']['high']
        low_temp = target['data'][0]['actual']['low']
        current_temp = target['data'][0]['actual']['tmp']
        today_wea = target['data'][0]['actual']['wea']
        air_desc = target['data'][0]['actual']['desc']
        # 上海 6~-2°C 现在温度 1°C 湿度：53 空气质量不好，注意防霾。 
        print('%s: %s~%s°C 现在温度 %s°C 湿度：%s %s'%(self.city,high_temp,low_temp,current_temp,today_wea,air_desc))
        print('**************%s 近期的天气***************' %self.city)
        for forecast in target['data'][0]['forecast']:
            date = forecast['date']
            high = forecast['high']
            low = forecast['low']
            wea = forecast['wea']
            print('日期： %s： 温度：%s~%s， 湿度： %s' %(date, low, high, wea))

if __name__ == '__main__':
    weather = Weather()
    weather.query('西充')
