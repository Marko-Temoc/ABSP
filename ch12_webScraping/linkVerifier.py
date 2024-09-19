#!/usr/bin/env python3

#linkVerifier.py takes a given url and attempts to download all linked pages, flagging any 404 links and printing them out
#pass the p argument first to print the broken links but don't actually download the linked pages
#TODO implement p feature

import bs4, sys

if len(sys.argv) > 2 :
    raise Exception('Only one argument allowed: please enter the full url')
url = sys.argv[1]

#TODO find every link on the page, probably searching a tags and their href attribute values
#TODO use requests module to download and check for broken links
#TODO download all these files to your current directory in a folder
#TODO have a list of all broken links in a .txt file in that folder as well
