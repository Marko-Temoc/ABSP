#!/usr/bin/env python3

#linkVerifier.py takes a given url and attempts to download all linked pages, flagging any 404 links and printing them out
#pass the p argument first to print the broken links but don't actually download the linked pages
#TODO implement p feature

import bs4, requests, sys, os

if len(sys.argv) > 2 :
    raise Exception('Only one argument allowed: please enter the full url')
if len(sys.argv) < 2 :
    raise Exception('One argument required: please enter the full url')
url = sys.argv[1]
print(type(url))
assert type(url) == str, 'url should be type str obviouvlys, this is just a first check to make sure that is how it works'

#find every link on the page and put into a list as Tag objects
responseO = requests.get(url)
responseO.raise_for_status()
bsO = bs4.BeautifulSoup(url, 'html.parser')
#list of Tag objects for each a element
tagO = bsO.select('a[href]')
assert type(tagO) == list, 'this should be a list right?'

os.makedirs('./link_list')
#iterate through tag list and try to download every link
for tag in tagO:
    link = tag.get('href')
    assert type(link) == str, 'pretty sure the href should return as a string'
    assert type(url + link) == str, 'does this url + link thingy work right?'
    linkResponse = requests.get(url + link)
    linkResponse.raise_for_status()
    if linkResponse.status_code == 404:
        #TODO print a file in folder with list of 404 broken links
        print(f'''{url}{link} returned a 404 error and wasn't found''')
    writeFile = open(url + href + '.html', 'wb')
    for chunk in linkResponse.iter_content(100000):
        writeFile.write(chunk)
