# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 11:23:26 2021

@author: martsc1
"""
# Deleting Unneeded Files
import os

# Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, 
# ones that have a file size of more than 100MB. Print these files with their absolute path to the screen.


print('Enter folder tree directory:')
folderTree = input()
print('Enter file size in bytes that you are looking for:')
fileSize = int(input())

for folderName, subfolders, filenames in os.walk(folderTree):
    for file in filenames:   
        try: 
            os.path.getsize(folderName+'\\'+file) 
            if os.path.getsize(folderName+'\\'+file) > fileSize:
                print('Found  '+file+' of size '+str(os.path.getsize(folderName+'\\'+file))+' bytes at location: '+folderName)
        except OSError:
            print("File '%s' does not exists or is inaccessible" %file) 
    
        
        
    










