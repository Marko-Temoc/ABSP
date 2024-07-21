'''bulletPointAdder.py - Adds Wikipedia bullet points to the start
of each line of text on the clipboard'''
import pyperclip
text = pyperclip.paste()
#TODO: seperate lines and add stars.
pyperclip.copy(text)
