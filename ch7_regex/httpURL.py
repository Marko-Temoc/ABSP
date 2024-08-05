#!/usr/bin/env python3

import pyperclip, re

httRegex = re.compile(r'''(
    (https?://)
    ([a-zA-Z]{2,4}\.)?
    ([\w-]+)
    (\.[a-zA-Z]{2,4}))''', re.VERBOSE)

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
