# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 10:55:04 2021

@author: martsc1
"""
#Table Printer

def printTable(yourList):
    colWidths = [0]*len(yourList)
    counter = 1
            
    for i in range(len(yourList[0])):
        for elem in range(len(colWidths)):
            colWidths[elem] = len(max(yourList[elem], key = len))
            if counter < len(colWidths):
                print(yourList[elem][i].rjust(colWidths[elem]),end=" ")
                counter += 1
            else:
                print(yourList[elem][i].rjust(colWidths[elem]))
                counter = 1
      
# test        
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)