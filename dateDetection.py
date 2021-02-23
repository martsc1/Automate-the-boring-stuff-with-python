# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:41:21 2021

@author: martsc1
"""
# Date detection
import re
import pyperclip

# detect dates in the DD/MM/YYYY format (from clipboard)
dateRegex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')

# store these strings into variables named month, day, and year
text = str(pyperclip.paste())

day = dateRegex.findall(text)[0][0]
month = dateRegex.findall(text)[0][1]
year = dateRegex.findall(text)[0][2]

dateValid = True
# detect if it is a valid date
if day not in range(1,32):
    print('Not a valid day!')
    dateValid = False
elif month not in range(1,13):
    print('Not a valid month!')
    dateValid = False
elif year not in range(1000,2999):
    print('Not a valid year!')
    dateValid = False
    
leapYear = False
if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
    leapYear = True
    
if leapYear:
    if (month in [4, 6, 9, 11] and day > 30) or (month == 2 and day > 29):
        print('Invalid day-month combination!')
        dateValid = False
else:
    if (month in [4, 6, 9, 11] and day > 30) or (month == 2 and day > 28):
        print('Invalid day-month combination!')
        dateValid = False
        
if dateValid:
    print('Valid date found!')
    













