#!/usr/bin/env python3

# mcb.pyw - Saves and loads pieces of text to the clipboard for 30 seconds, before wiping clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
    # py.exe mcb.pyw remove <keyword> - Removes a keyword and its contents from memeory.
    # py.exe mcb.pyw remove all - Removes all keywords and contents from memeory.
    # py.exe mcb.pyw <keyword> - Loads keyword's contents to clipboard.
    # py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve, pyperclip, sys, time

mcbShelf = shelve.open('mcb')

#if there are 3 arguments, that means save or remove were used
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        #take the clipboard contents and put into shelf labeled as argument after save
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'remove':
        if sys.argv[2].lower() == 'all':
            for key in list(mcbShelf.keys()):
                del mcbShelf[str(key)]
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    #list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    time.sleep(30)
    pyperclip.copy('')

mcbShelf.close()
