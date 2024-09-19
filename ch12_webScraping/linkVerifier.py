#!/usr/bin/env python3

#linkVerifier.py takes a given url and attempts to download all linked pages, flagging any 404 links and printing them out

import bs4, sys

if len(sys.argv) > 2 :
    raise Exception('Only one argument allowed: please enter the full url')
url = sys.argv[1]
print(url)
