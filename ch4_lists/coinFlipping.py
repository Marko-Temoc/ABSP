#!/usr/bin/env python3

import random

#flip a coin 100 times and record results in this list
flipResults = []

for flip in range(100):
    hort = random.randint(0,1)
    if hort == 0:
        flipResults.append('H')
    if hort == 1:
        flipResults.append('T')
print(flipResults)
#find out how many streaks of 6 heads or tails were in that list
#look at first item, check if second item is the same
#if it is the same, set counter to +1 (if counter is 5, win)
#then check from the next position
#if next item isn't the same, reset counter
counter = 0
streaks = 0

#took me a while to remember enumerate() was what I wanted
for i, result in enumerate(flipResults):
    #if we're on the last item
    if i == len(flipResults) - 1:
        break
    if result == flipResults[i+1]: #if this item is same as next item
        counter += 1
        if counter == 5: #reset once we found 5 more that match
            streaks += 1
            counter = 0
    else:
        counter = 0

print('Numbers of streaks: ' + str(streaks))
