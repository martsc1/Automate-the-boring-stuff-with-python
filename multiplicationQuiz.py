# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:36:34 2021

@author: martsc1
"""
# multiplication quizz

import time 
import random

# prompt the user with 10 multiplication questions, ranging from 0 × 0 to 9 × 9.
question = 0
score = []

for iQuestion in range(10):
    num1 = round(random.random()*10)
    num2 = round(random.random()*10)
    answer = num1 * num2
    userAnswer = 0
    tries = 0
    print('%d x %d = ?' % (num1, num2))
    question +=1
    tic = time.time()

# If the user enters the correct answer, the program displays “Correct!” for 1 second and moves on to the next question.
    userAnswer = input()
    tries += 1

    while time.time() - tic < 8:
        if userAnswer != 0 and tries < 4:
            if answer == int(userAnswer):
                print('Correct!')
                score.append('Correct')
                time.sleep(1)
                break
            else:
                print('Wrong answer, try again!')
                userAnswer = input()
                tries += 1
                if time.time() - tic > 8:   
                    print('Too slow')
                    score.append('Incorrect')
                elif tries > 3:
                    print('Too many tries')
                    score.append('Incorrect')
                    
    if time.time() - tic > 8 or userAnswer == 0:   
        print('Too slow')
        score.append('Incorrect')
            
            
print('You answered %d out of 10 questions correctly!' % score.count('Correct'))
                
        

    
        
        

# The user gets three tries to enter the correct answer before the program moves on to the next question.
# Eight seconds after first displaying the question, the question is marked as incorrect even if the user enters the correct answer after the 8-second limit.