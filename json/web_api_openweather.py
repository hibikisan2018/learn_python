# -*- coding: utf-8 -*-
"""
Get current weather data from OpenWeather API
"""
import json
import requests
import config

# API keyはconfigy.pyから読み出す
API_KEY = config.API_KEY

# 東京のcity ID(http://bulk.openweathermap.org/sample/city.list.json.gz)
city_id = '1850147'

# API endpoint
url = 'https://api.openweathermap.org/data/2.5/weather'

# 言語は日本語、温度の単位は℃に設定
params = {"id": city_id, "appid" : API_KEY, 'lang': 'ja', 'units':'metric'}

res = requests.get(url, params=params)

# JSONフォーマットをPythonオブジェクト（辞書型）に変換
data = json.loads(res.text)

# 辞書データから所望の値を取り出す
location = data['name']
weather = data['weather'][0]['main']
tempreture = data['main']['temp'] 
humidity = data['main']['humidity']

print(f'現在、{location}の天気は{weather}、気温は{tempreture}℃、湿度は{humidity}％です。')
