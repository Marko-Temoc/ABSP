#!/usr/bin/env python3

import time, sys
indent = 0 #how many spaces to indent
indentIncreasing = True #whether indentation is increasing or not
try:
    while True: #main program loop
        print(' ' * indent, end='')
        print('*' * 8)
        time.sleep(0.01) #pause for 1/10th of a second
        if indentIncreasing:
            #increasing number of spaces:
            indent += 1
            if indent == 150:
                #change direction
                indentIncreasing = False
        else:
            #decrease number of spaces
            indent -= 1
            if indent == 0:
                #change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
