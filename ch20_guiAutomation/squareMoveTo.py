#!/usr/bin/env python3
#squareMoveTo.py traces a square in the upper left corner of your screen with the mouse for 10 seconds
import pyautogui

for i in range(10):
    pyautogui.moveTo(100,100, duration=0.25)
    pyautogui.moveTo(200,100, duration=0.25)
    pyautogui.moveTo(200,200, duration=0.25)
    pyautogui.moveTo(100,200, duration=0.25)
