#!/usr/bin/env python3
import sys

spam = ['apples', 'bananas', 'tofu', 'cats']
empty = []
one = ['hello']

def printList(someList):
    result = ''
    #if its an empty list
    if someList == []:
        print('This is just an empty list')
        sys.exit()
    for item in someList:
        #if list has just one item, print the item
        if len(someList) == 1:
            result += someList[0]
            break
        #if item is last in list
        elif item == someList[-1]:
            result += 'and ' + item
            break
    #append item to result string with a following comma and space
        result += item + ', '
    print(result)

printList(one)
