#!/usr/bin/env python3
#date detector - matches only valid dates in the DD/MM/YYYY format

#NOTE expected ranges of dates
#days range 01-31
#months range 01-12
#years range 1000-2999

import re, pyperclip

dateRegex = re.compile(r'''(
    ^((0[1-9])|([12]\d)|(3[01]))/   #DD: beginning of date must be 01-31
    ((0[1-9])|(1[012]))/            #MM: 01-12
    ([12]\d{3})                       #YYYY: 1000-2999
    )''', re.VERBOSE)

clipboard = pyperclip.paste()

for amatch in dateRegex.findall(clipboard):
    #each match will be a tuple where group 1-2 is day, 3-4 is day, and 5 is year
    day = amatch[2]
    month = amatch[4]
    year = amatch[5]

    #NOTE April, June, September, and November have 30 days; February has 28 days; every other month 31
    #NOTE February has 29 days in leap years
    if month == ('04' or '06' or '09' or '11') and (day == '31'):
        print("Nope")

    elif (month == '02') and (day == '30' or '31'):
        print("Nope")

    #calculate and find out if its a leap year
    #NOTE leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400
    elif (month == '02') and (day == '29'):
        if (str(year) % 4 == 0) and (
                (str(year) % 100 != 0)
                    or (str(year) % 100 == 0) and (str(year) % 400 == 0)):
            print("Yep")
        else:
            print("Nope")
    else:
        print("Yep")

#TESTCODE
#tester = '22/01/1999'
#mo = dateRegex.findall(tester)
#print(mo)
