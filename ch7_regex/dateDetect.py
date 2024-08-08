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
    #each match will be a tuple where amatch[1] is day, [5] is month, and [8] is year
    xday = amatch[1]
    xmonth = amatch[5]
    xyear = amatch[8]
    print(f'{xday}/{xmonth}/{xyear}')

    #NOTE April, June, September, and November have 30 days; February has 28 days; every other month 31
    #NOTE February has 29 days in leap years
    if (xmonth == ('04' or '06' or '09' or '11')) and (xday == '31'):
        print("Invalid date: this month only has 30 days")

    elif (xmonth == '02') and (xday == ('30' or '31')):
        print("Invalid date: this month only goes up to 29 (on leap years)")

    #calculate and find out if its a leap year
    #NOTE leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400
    elif (xmonth == '02') and (xday == '29'):
        if (int(xyear) % 4 == 0) and (
                (int(xyear) % 100 != 0)
                    or (int(xyear) % 100 == 0) and (int(xyear) % 400 == 0)):
            print("Leap Valid date")
        else:
            print("Leap Invalid date")
    else:
        print("Valid date")
