#!/usr/bin/env python3

def pstester(ps):
    oneDigitRegex = re.compile(r'\d+')
    oneLowerRegex = re.compile(r'.*[a-z].*')
    oneUpperRegex = re.compile(r'.*[A-Z].*')
    eightCharRegex = re.compile(r'.{8,}')

    output = []
    shouldweoutput = 0
    weak = "Weak password: must have at least"
    output.append(weak)

    if oneDigitRegex.search(ps) == None:
        output.append(r'\n1 digit')
        shouldweoutput += 1
    if oneLowerRegex.search(ps) == None:
        output.append(r'\n1 lower case letter')
        shouldweoutput += 1
    if oneUpperRegex.search(ps) == None:
        output.append(r'\n1 upper case letter')
        shouldweoutput += 1
    if eightCharRegex.search(ps) == None:
        output.append(r'\n8 characters')
        shouldweoutput += 1
    if shouldweoutput > 0:
        print('\n'.join(output))
    else:
        print("Strong password")
