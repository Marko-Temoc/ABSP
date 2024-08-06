#!/usr/bin/env python3
#https? url finder - works for the average url

import pyperclip, re

httRegex = re.compile(r'''(
    (https?://)                                  #http or https followed by //:
    ([a-zA-Z]{2,4}\.)?                           #one or more www. or docs. fields
    ([\w~.:;?#!$&*+%=-]+)                        #body of url
    (\.[a-zA-Z]{2,4})+                           #one or mroe .com endings
    (/[\w~:;?#!$&*+%=-]+)*                       #optional one or more '/text' fields at end
    [^.\])]                                      #don't match ending period or parentheses
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for amatch in httRegex.findall(text):
    matches.append(amatch[0])
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print("No urls starting with 'http://' or 'https://' detected.")
