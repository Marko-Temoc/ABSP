#!/usr/bin/env python3
#example of why and how you'd use the inputCustom() function from pyinputplus to create your own custom validation logic

import pyinputplus as pyip

def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %(sum(numbersList)))
    return int(numbers) # Return an int form of numbers

pyip.inputCustom(addsUpToTen)
