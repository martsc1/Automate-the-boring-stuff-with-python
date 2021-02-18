# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:10:46 2021

@author: martsc1
"""
#CoinFlipStreak

import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinFlips = []
    for flip in range(100):
        if random.randint(0, 1) == 1:
            coinFlips.append('heads')
        else:
            coinFlips.append('tails')
    
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for flip in range(len(coinFlips)-5):
        if coinFlips[flip]=='tails' and coinFlips[flip+1]=='tails' and coinFlips[flip+2]=='tails' and coinFlips[flip+3]=='tails' and coinFlips[flip+4]=='tails' and coinFlips[flip+5]=='tails':
            numberOfStreaks += 1
            break
        elif coinFlips[flip]=='heads' and coinFlips[flip+1]=='heads' and coinFlips[flip+2]=='heads' and coinFlips[flip+3]=='heads' and coinFlips[flip+4]=='heads' and coinFlips[flip+5]=='heads':
            numberOfStreaks += 1
            break
            
print('Chance of streak: %s%%' % (numberOfStreaks / 100))