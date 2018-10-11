#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Livedoor weather_hacks webservice
"""
import json
import requests
import pprint

#base_url='http://weather.livedoor.com/forecast/webservice/json/v1?city={city}'
base_url='http://weather.livedoor.com/forecast/webservice/json/v1'
city_id = '140010'

params = {'city': city_id}

#url = base_url.format(city = city_id)

res = requests.get(base_url, params=params)
res.raise_for_status()

data = json.loads(res.text)
#pprint.pprint(data)

print("**** Weather Information@Kanagawa ****")
print("[TIME]")
print(data["description"]["publicTime"])
print("[INFOMATION]")
print(data["description"]["text"])
print("[FORECASTS]")
for i in range(3):
    print("DATE:{} / {}".format(data["forecasts"][i]["date"], data["forecasts"][i]["telop"]))

