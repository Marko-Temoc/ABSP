#!/usr/bin/env python3
#spiralDraw.py draws a spiral square when in a paint program with the mouse equipped with a brush

import time, pyautogui

time.sleep(5) #give time to switch to paint program
pyautogui.click() #make window active

distance = 300
change = 20

while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2) #move right
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.2) #move down
    pyautogui.drag(-distance, 0, duration=0.2) #move left
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.2) #move up
