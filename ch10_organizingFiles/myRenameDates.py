#!/usr/bin/env python3

import re, os, shutil
from pathlib import Path

cwd = Path.cwd()
usaRegex = re.compile(r'''
    (.*)                    #g1:before-date
    ((0[\d])|(1[012]))      #g2:01-12 for month, g3:01-09, g4:10-12
    ([_-])                  #g5:first sep
    (([0-2][\d])|(3[01]))   #g6:01-31 for month, g7:01-29, g8:30-31
    ([_-])                  #g9:second sep
    (\d{4})                 #g10:any 4 digits = year
    (.*)                    #g11:after-date
    ''', re.VERBOSE)
#this regex is NOT used, it's just helpful to look at for me
eurRegex = re.compile(r'''
    (.*)                    #g1:before-date
    (([0-2][\d])|(3[01]))   #g2:01-31 for month, g3:01-29, g4:30-31
    ([_-])                  #g5:first sep
    ((0[\d])|(1[012]))      #g6:01-12 for month, g7:01-09, g8:10-12
    ([_-])                  #g9:second sep
    (\d{4})                 #g10:any 4 digits = year
    (.*)                    #g11:after-date
    ''', re.VERBOSE)

#go through every file in current working directory
for file in os.listdir(cwd):
    #if file has american date, store in match object
    mo = usaRegex.search(file)
    if mo == None:
        continue
    newName = mo.group(1) + mo.group(6) + mo.group(5) + mo.group(2) + mo.group(9) + mo.group(10) + mo.group(11)
    print(f'''Renaming {file} to {newName}...''')
    shutil.move(file, newName)
