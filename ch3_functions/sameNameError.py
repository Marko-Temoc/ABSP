#!/usr/bin/env python3

def spam():
    print(eggs) #ERROR!
    eggs = 'spam local'
eggs = 'global'
spam()
