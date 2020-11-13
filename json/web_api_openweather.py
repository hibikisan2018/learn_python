# -*- coding: utf-8 -*-
"""
Get current weather data from OpenWeather API
"""
import json
import requests
import config

# API key in configy.py
API_KEY = config.API_KEY

# city ID of Tokyo from http://bulk.openweathermap.org/sample/city.list.json.gz
city_id = '1850147'

# API endpoint
url = 'https://api.openweathermap.org/data/2.5/weather'

# Set language to "Japanese" and tempreture's unit to "Celsius"
params = {"id": city_id, "appid" : API_KEY, 'lang': 'ja', 'units':'metric'}

res = requests.get(url, params=params)
data = json.loads(res.text)

#print(json.dumps(data, indent=4, ensure_ascii=False))

location = data['name']
weather = data['weather'][0]['main']
tempreture = data['main']['temp'] 
humidity = data['main']['humidity']

print(f'現在、{location}の天気は{weather}、気温は{tempreture}℃、湿度は{humidity}％です。')
