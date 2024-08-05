#!/usr/bin/env python3

import pyperclip, re

httRegex = re.compile(r'''(
    (https?://)                                 #http or https, //:
    ([a-zA-Z]{2,4}\.)?                          #2-4 www. field
    ([\w-]+)                                    #main body of url
    (\.[a-zA-Z]{2,4})                           #end of main body, .com field
    ((/[\w]+)?)+                                #optional one or more '/text' fields at end
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

#TODO better comment the parts of the url sections
#TODO improve regex to capture rest of the url with forward slashes
