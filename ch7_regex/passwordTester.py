#!/usr/bin/env python3

def pstester(ps):
    oneDigitRegex = re.compile(r'\d+')
    oneLowerRegex = re.compile(r'.*[a-z].*')
    oneUpperRegex = re.compile(r'.*[A-Z].*')
    eightCharRegex = re.compile(r'.{8,}')

    weak = "Weak password: "

    if oneDigitRegex.search(ps) == None:
        print(f"{weak}must have at least one digit")
    if oneLowerRegex.search(ps) == None:
        print(f"{weak}must have at least one lower case letter")
    if oneUpperRegex.search(ps) == None:
        print(f"{weak}must have at least one upper case letter")
