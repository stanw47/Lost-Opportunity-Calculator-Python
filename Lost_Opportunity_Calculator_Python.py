
# typical python stuff, set yourself up for success here
from datetime import datetime
import os
import sys

def loc1():
    print('Welcome to the Lost Opportunity Calculator!')
    print('Did you take a long position or a short position? enter s for short and l for long')
    sorl1 = input()
    if sorl1 == 's':
        print('What was your entry price?')
        sentry1 = int(input())
        print('What was your exit price?')
        sexit1 = int(input())
        print('What was the price at the top of the movement?')
        stop1 = int(input())
        print('What was the price at the bottom of the movement?')
        sbottom1 = int(input())
        print('How many units did you trade?')
        sunits1 = int(input())
        print('Your lost opportunity is')
        print(((stop1 - sbottom1) - (sentry1 - sexit1)) * sunits1)
    elif sorl1 == 'l':
        print('What was your entry price?')
        lentry1 = int(input())
        print('What was your exit price')
        lexit1 = int(input())
        print('What was the price at the bottom of the movement?')
        lbottom1 = int(input())
        print('What was the price at the top of the movement?')
        ltop1 = int(input())
        print('How many units did you trade?')
        lunits1 = int(input())
        print('Your lost opportunity is')
        print(((ltop1 - lbottom1) - (lexit1 - lentry1)) * lunits1)
while True:
    loc1()
    while True:
        exit = str(input("Do you want to calculate more lost opportunities? y/n?"))
        if exit in ('y', 'n'):
            break
        print('Invalid Input, try again.')
        if exit == 'y':
            loc1()
        else:
            print('Thank you for using the calculator! Goodbye!')
            break