# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 11:01:24 2021

@author: martsc1
"""
# Debugging coin toss

import random
guess = ''
coin = ['heads','tails']
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    
toss = random.randint(0, 1) # 0 is tails, 1 is heads
toss = coin[toss]

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')