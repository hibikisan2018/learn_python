#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 23:00:24 2018
-------
This program is to download Web site including all pages 
linked from original page.
This is referenced by text bokk "Scraping & Machine Learning"
@author: hibikisan
"""
import re, time
import os.path
from urllib.parse import urlparse
from urllib.parse import urljoin
from os import makedirs
import requests
import bs4

# Aleady downloaded savepath
proc_files = {}

# Extract all links in the web site 'html'
def enum_links(html, base):
    soup = bs4.BeautifulSoup(html, 'lxml')
    links = soup.select("link[rel='stylesheet']")
    links += soup.select("a[href]")
    result = []
    for a in links:
        href = a.attrs['href']
        url = urljoin(base, href)
        result.append(url)
    return result

# Download and save files
def download_file(url):
    o = urlparse(url)
    savepath = "./" + o.netloc + o.path
    # check if savepath is directory or not
    if re.search(r'/$', savepath):
        savepath += "index.html"
    savedir = os.path.dirname(savepath)
    
    # check if the files are already downloaded
    if os.path.exists(savepath):
        return savepath
    
    # Make directory for save downloaded files
    if not os.path.exists(savedir):
        print('mkdir=', savedir)
        makedirs(savedir)
    
    # download files
    try:
        print('download=', url)
        res = requests.get(url)
        res.raise_for_status()
        with open(savepath, 'w') as f:
            f.write(res.text)
        
        time.sleep(1)
        return savepath
        
    except requests.RequestException as e:
        print('failed to download:', e)
        return None   
    
# Parse HTML and download html data
def analize_html(url, root_url):
    savepath = download_file(url) 
    if savepath is None: return
    if savepath in proc_files: return
    proc_files[savepath] = True
    print("analize_html=", url)

    html = open(savepath, 'r', encoding='utf-8').read()
    links = enum_links(html, url)
    
    for link_url in links:
        if link_url.find(root_url) != 0:
            if not re.search(r'.css$', link_url):
                continue
        if re.search(r'.(html|html)$', link_url):
            analize_html(link_url, root_url)
            continue
        download_file(link_url)

if __name__ == '__main__':
    url = "https://docs.python.jp/3/library/"
    analize_html(url, url)
