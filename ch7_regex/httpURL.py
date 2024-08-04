#!/usr/bin/env python3

import pyperclip, re

httRegex = re.compile(r'''(
    (https?://)
    ([a-zA-Z]{2,3}\.)?
    (\w+)
    (\.[a-zA-Z]{2,4}))''', re.VERBOSE)

#take clipboard contents and put in text var
text = str(pyperclip.paste())
#init empty list to store our matches into as strs
matches = []
# TODO find all the url addresses that were found
#take every tuple in the list, reconstruct into the html, and add to a list
mo = httRegex.findall(text)
print(mo)
# TODO put all the results in one tidy string with newlines at the end
# TODO print out string if matches were there, and print something else otherwise










# TODO find all matches in the text
#takes text, uses findall to output matches as tuples in a list, and for every tuple..
#for anymatch in httRegex.findall(text):
    #recombine strings in tuple into one big string again

# TODO neatly format matches into a single string to paste as output
# TODO display info if there were no matches
