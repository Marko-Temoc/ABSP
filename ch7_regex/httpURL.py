#!/usr/bin/env python3

import pyperclip, re

httRegex = re.compile(r'''(
    (https?://)
    (\w+)
    (\.[a-zA-Z]{2,4}))''', re.VERBOSE)

#why do we have to make this a str type? what is it naturally?
text = pyperclip.paste()

# TODO find all matches in the text
#takes text, uses findall to output matches as tuples in a list, and for every tuple..
for anymatch in httRegex.findall(text):
    #recombine strings in tuple into one big string again

# TODO neatly format matches into a single string to paste as output
# TODO display info if there were no matches
