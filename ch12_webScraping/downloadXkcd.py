#!/usr/bin/env python3

import requests, bs4, webbrowser

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    #TODO download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #TODO find the url of comic page
    #TODO download the image
    #TODO save the image to ./xkcd
    #TODO get the prev button's url
print('Done.')
