#!/usr/bin/env python3

import random

numOfStreaks = 0

for num in range(10000):
    flipResults = []

    for flip in range(100):
        hort = random.randint(0,1)
        if hort == 0:
            flipResults.append('H')
        if hort == 1:
            flipResults.append('T')

    counter = 0
    streaks = 0

    for i, result in enumerate(flipResults):
        #if we're on the last item
        if i == len(flipResults) - 1:
            break
        #if this item is same as next item
        if result == flipResults[i+1]:
            counter += 1
            if counter == 5: #reset once we found 5 more that match
                streaks += 1
                counter = 0
        else:
            counter = 0

    if streaks > 0:
        numOfStreaks += 1
        streaks = 0

print('Chance of streak: %s%%' % (numOfStreaks/100))
print('My chance of streak: ' + str(100*(numOfStreaks/10000)) + "%")
