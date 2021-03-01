# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 11:13:34 2021

@author: martsc1
"""
# Mad Libs
import os

# read in text file
print('Enter file path:')
filePath = input()
print('Enter file name:')
fileName = input()

inputFile = open(filePath+'\\'+fileName)
os.chdir(filePath)

# create output file
outputFile = open('updated_'+fileName, 'w') 

# check content for ADJECTIVE, NOUN, VERB
inputContent = inputFile.read()

# find last word, needed to copy end of text 
lastWord = inputContent.rfind('ADJECTIVE')

if inputContent.rfind('NOUN') > lastWord:
    lastWord = inputContent.rfind('NOUN')
elif inputContent.rfind('VERB') > lastWord:
    lastWord = inputContent.rfind('VERB')
    
# create dictionary with words of interest and their location    
searchWords = {"ADJECTIVE": 0, "NOUN": 0, "VERB": 0}
if inputContent.find('ADJECTIVE') > 0:
    searchWords.update({"ADJECTIVE" : inputContent.find('ADJECTIVE')}) 
else:
    searchWords.update({"ADJECTIVE" : 0})
        
if inputContent.find('NOUN') > 0:
    searchWords.update({"NOUN" : inputContent.find('NOUN')})
else:
    searchWords.update({"NOUN" : 0})
        
if inputContent.find('VERB') > 0:
    searchWords.update({"VERB" : inputContent.find('VERB')})
else:
    searchWords.update({"VERB" : 0})

# create variables with the current word of interest and its location
searchTerm = sorted(searchWords.items(), key=lambda t: t[1])[0][0]
searchLocation = sorted(searchWords.items(), key=lambda t: t[1])[0][1]

# Copy the beginning of the file
outputFile.write(inputContent[0:searchLocation])
outputFile.close()
outputFile = open('updated_'+fileName, 'a')

# Go through the text and replace all words of interest
while len(searchWords) > 0:
        
    searchTerm = sorted(searchWords.items(), key=lambda t: t[1])[0][0]
    searchLocation = sorted(searchWords.items(), key=lambda t: t[1])[0][1]

    print('Enter a %s:' % searchTerm)
    wordInput = input()
    outputFile.write(wordInput)   # add replacement word
    if len(searchWords) > 1: # add text between words of interest
        outputFile.write(inputContent[(searchLocation + len(searchTerm)):sorted(searchWords.items(), key=lambda t: t[1])[1][1]])
        
    # update word of interest list 
    if inputContent.find(searchTerm, (searchLocation+1)) > 0:
        searchWords.update({searchTerm : inputContent.find(searchTerm, (inputContent.find(searchTerm)+1))})
    else:
        searchWords.pop(searchTerm)
        

outputFile.write(inputContent[(lastWord + len(searchTerm)):len(inputContent)])
        
        
outputFile.close()
outputFile = open('updated_'+fileName) 
madLibs = outputFile.read() 
inputFile.close()
print(madLibs)
    