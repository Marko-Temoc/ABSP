#!/usr/bin/env python3

import re, os, shutil
from pathlib import Path

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
for amerFilename in os.listdir('.'):
    #if file has american date, store in match object
    mo = usaRegex.search(amerFilename)
    if mo == None:
        continue
    else:
        beforePart = mo.group(1)
        monthPart = mo.group(2)
        firstSepPart = mo.group(5)
        dayPart = mo.group(6)
        secondSepPart = mo.group(9)
        yearPart = mo.group(10)
        afterPart = mo.group(11)
        euroFilename = beforePart + dayPart + firstSepPart + monthPart + secondSepPart + yearPart + afterPart
        absWorkingDir = os.path.abspath('.')
        amerFilename = os.path.join(absWorkingDir, amerFilename)
        euroFilename = os.path.join(absWorkingDir, euroFilename)
        print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
        shutil.move(amerFilename, euroFilename)
