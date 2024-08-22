#!/usr/bin/env python3

import pyinputplus as pyip

numOfQs = 10

#this is the main game loop: get asked X amount of questions before seeing your score at the end
for question in range(1,numOfQs+1):
    print(f"This is number {question}")
