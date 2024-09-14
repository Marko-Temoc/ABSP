#!/usr/bin/env python3

import requests, bs4, os
url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    #download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #skip over specific pages that puts program on hold
    if url.endswith('2198/') or url.endswith('1663/') or url.endswith('1608/'):
        print(f'SKIPPING {url}')
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
        continue
    #find the url of comic page
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        #download the image
        print('Downloading image %s...' % (comicUrl))
        #save the image to ./xkcd, in case it isn't already there
        if os.path.basename(comicUrl) not in os.listdir('xkcd'):
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        #get the prev button's url
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
print('Done.')
