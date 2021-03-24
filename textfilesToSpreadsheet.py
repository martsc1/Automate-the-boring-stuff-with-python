# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 11:33:19 2021

@author: martsc1
"""
#Text Files to Spreadsheet


from pathlib import Path
import openpyxl

p = Path('C:\\Users\\martsc1\\Documents\\Online courses\\automate the boring stuff')
 
textFiles = list(p.glob('*.txt'))

# create list of alphabet for excel columns
def chars(*args):
    return [chr(i) for a in args for i in range(ord(a[0]), ord(a[1])+1)]

alph = list(chars('AZ'))

# create spreadsheet
wb = openpyxl.Workbook() 
sheet = wb.active

# loop over text files
for iFile in range(len(textFiles)):
    content = open(textFiles[iFile])
    contentLines = content.readlines()
    
    # loop over lines
    for iLine in range(len(contentLines)):
        sheet[alph[iFile]+str(iLine+1)] = contentLines[iLine][0:-1]


wb.save('text2spreadsheet.xlsx')

