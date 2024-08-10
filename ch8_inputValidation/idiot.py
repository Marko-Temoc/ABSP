#!/usr/bin/env python3

import pyinputplus as pyip

while True:
    response = pyip.inputYesNo('Want to know how to keep an idiot busy for hours?\n')
    if response == 'yes':
        continue
    if response == 'no':
        break
print('Oh. Well then. Have a nice day.')
