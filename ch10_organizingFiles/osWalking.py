#!/usr/bin/env python3

import os

for folderName, subfolders, filenames in os.walk('/home/Tony'):
    print('The current folder name is' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')
