#!/usr/bin/env python3
#Coin gets tossed, Player gets two guesses
import random, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
guess = ''

print('Guess the coin toss! Enter heads or tails:')
guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 0:
    toss = 'tails'
if toss == 1:
    toss = 'heads'
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
