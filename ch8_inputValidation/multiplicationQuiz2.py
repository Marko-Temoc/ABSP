#!/usr/bin/env python3

import pyinputplus as pyip
import random, time

numofQuestions = 10
correctAnswers = 0

for questionNumber in range(numofQuestions):
    #pick two random numbers:
    num1 = random.randint(2,9)
    num2 = random.randint(2,9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    try:
        #right answers handled by allowRegexes
        #wrong answers handled by blockRegexes, with a custom message
        pyip.inputStr(prompt, allowRegexes=[('^%s$' % (num1 * num2))],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    except KeyboardInterrupt:
        print('\nThanks for playing!')
        break
    else:
        # This block runs if no exceptions were raised in the try block
        print('Correct!')
        correctAnswers +=1
    time.sleep(1) # Brief pause to let user see the result
print('Score: %s / %s' % (correctAnswers, numofQuestions))
