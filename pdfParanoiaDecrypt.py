# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:39:38 2021

@author: martsc1
"""
# PDF paranoia decrypt

import os, PyPDF2

print('Enter folder tree directory in which you want to decrypt PDFs:')
folderTree = input()
print('Enter the password you want to decrypt PDFs with:')
password = input()


for folderName, subfolders, filenames in os.walk(folderTree):
    for file in filenames:        
        if '_encrypted.pdf' in file:
            # create decrypted copy
            pdfFile = open(folderName+'\\'+file, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfReader.decrypt(password)
            
            # check whether decryption worked
            if pdfReader.decrypt(password) == 1:
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                
                decryptedPdf = open(folderName+'\\'+file[:-14]+'_decrypted.pdf', 'wb')
                pdfWriter.write(decryptedPdf)
                decryptedPdf.close()
                pdfFile.close()
                
            else:
                print('Warning! /n Unable to decrypt the '+file+' file!')
            
            
            
            
            



   
   

    
    
    
    
