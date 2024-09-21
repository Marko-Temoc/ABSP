#!/usr/bin/env python3
#squareMoveTo.py traces a square in the upper left corner of your screen with the mouse for 10 seconds
import pyautogui

for i in range(10):
    pyautogui.move(100,0, duration=0.25)
    pyautogui.move(0,100, duration=0.25)
    pyautogui.move(-100,0, duration=0.25)
    pyautogui.move(0,-100, duration=0.25)
