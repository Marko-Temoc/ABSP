#!/usr/bin/env python3
#the book's content about selenium's methods are out of date, so it looks different

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element(By.CLASS_NAME, 'cover-thumb')
    print(f'Found {elem.tag_name} with that class name!')
except:
    print('Was not able to find an element with that name.')
