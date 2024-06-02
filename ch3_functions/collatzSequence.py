#!/usr/bin/env python3

def collatz(number):
    if number % 2 == 0: #if even
        number = number // 2
    elif number % 2 != 0: #if odd
        number = 3 * number + 1
    print(number)
    return number


inp = int(input("Input an integer here: \n"))
while inp != 1:
    inp = collatz(inp)
