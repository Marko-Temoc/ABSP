#!/usr/bin/env python3

#linkVerifier.py takes a given url and attempts to download all linked pages, flagging any 404 links and printing

import bs4, requests, sys, os

if len(sys.argv) > 2 :
    raise Exception('Only one argument allowed: please enter the full url')
if len(sys.argv) < 2 :
    raise Exception('One argument required: please enter the full url')
url = sys.argv[1]

#find every link on the page and put into a list as Tag objects
responseO = requests.get(url)
responseO.raise_for_status()
bsO = bs4.BeautifulSoup(responseO.text, 'html.parser')
#list of Tag objects for each a element
tagO = bsO.select('a[href]')

os.makedirs('link_list', exist_ok=True)
#iterate through tag list and try to download every link
for tag in tagO:
    link = tag.get('href')
    if link == '/':
        continue
    if link.startswith('/') == True:
        linkResponse = requests.get(url + link)
        newURL = url + link
    if link.startswith('http') == True:
        linkResponse = requests.get(link)
        newURL = link
    if linkResponse.status_code == 404:
        print(f'''{newURL} returned a 404 error and wasn't found''')
    if linkResponse.status_code == 403:
        print(f'''{newURL} returned a 403 error and was forbidden''')
    writeFile = open(os.path.join('link_list', os.path.basename(newURL) + '.html'), 'w')
    writeFile.write(linkResponse.text)
    writeFile.close()
