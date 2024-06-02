#!/usr/bin/env python3

import sys

def collatz(number):
    if number % 2 == 0: #if even
        number = number // 2
    elif number % 2 != 0: #if odd
        number = 3 * number + 1
    print(number)
    return number


try:
    inp = int(input("Input a positive integer here: \n"))
    if inp < 1:
        print('Please enter a positive integer')
        sys.exit()
    while inp != 1:
        inp = collatz(inp)
except ValueError:
    print('Must enter a positive integer')
