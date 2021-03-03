# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:57:33 2021

@author: martsc1
"""
# selective copy
import os,shutil

# Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). 
# Copy these files from whatever location they are in to a new folder.


print('Enter folder tree directory:')
folderTree = input()
print('Enter file extension you want to copy:')
fileExtenstion = input()
print('Enter copy destination directory:')
destinationFolder = input()


for folderName, subfolders, filenames in os.walk(folderTree):
    for file in filenames:        
        if fileExtenstion in file:
            print('Copied file '+file)
            shutil.copy(folderName+'/'+file, destinationFolder+'/'+file)
    










