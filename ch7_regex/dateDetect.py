#!/usr/bin/env python3
#date detector - matches only valid dates in the DD/MM/YYYY format

#NOTE expected ranges of dates
#days range 01-31
#months range 01-12
#years range 1000-2999

#TODO create regex to match format;it'll accept nonexistent dates like '31/02/2020' for example
#TODO store these strings in variables: day, month, year
#TODO detect if altogether this is a valid date
#NOTE April, June, September, and November have 30 days; February has 28 days; every other month 31
#NOTE February has 29 days in leap years
#NOTE leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400
