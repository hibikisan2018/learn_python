#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
news_titles.py
"""
import requests
import re

url = 'https://www.nikkei.com/'

res = requests.get(url)
try:
    res.raise_for_status()

    subtitles = re.findall(r'<span class="m-miM\d{2}_titleL".*>.+</span></a>', res.text)
    if len(subtitles) != 0:
        for l in subtitles:
            subtitles_ = re.search(r'<span class="m-miM\d{2}_titleL".*>(.+)</span>', l).group(1)
            print(subtitles_)
    else:
        print('No article')

except Exception as e:
    print(e)

