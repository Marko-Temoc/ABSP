#!/usr/bin/env python3

import random, time

for questionNumber in range(1,11):
    num1 = random.randint(2,9)
    num2 = random.randint(2,9)
    prompt = f'Q{questionNumber}: {num1} x {num2} = '
    attempts = 0
    while attempts < 3:
        answer = input(prompt)
        if answer == str(num1 * num2):
            print('Correct!')
            time.sleep(1)
            attempts = 0
            break
        else:
            print('Incorrect!')
            attempts += 1
            time.sleep(1)
            continue

#TODO find out how to give user 8 seconds to answer questions, before its marked wrong
#even if they answer correctly after the timer
