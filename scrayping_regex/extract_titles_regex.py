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

    regex = re.compile(r'<a class="k-card__block-link".*?><span class="k-v">.+?</span></a>')
    subtitles = regex.findall(res.text)

    if len(subtitles) != 0:
        print(f"Total: {len(subtitles)} titles")
        for l in subtitles:
            t = re.search(r'<span.+>(.+)</span>', l).group(1) 
            print(t)
    else:
        print('No article')

except Exception as e:
    print(e)

