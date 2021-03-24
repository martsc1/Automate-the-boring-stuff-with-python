# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:39:38 2021

@author: martsc1
"""
# PDF paranoia encrypt

import os, PyPDF2

print('Enter folder tree directory in which you want to encrypt PDFs:')
folderTree = input()
print('Enter the password you want to encrypt PDFs with:')
password = input()


for folderName, subfolders, filenames in os.walk(folderTree):
    for file in filenames:        
        if '.pdf' in file:
            # create encrypted copy
            pdfFile = open(folderName+'\\'+file, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            
            pdfWriter.encrypt(password)
            encryptedPdf = open(folderName+'\\'+file[:-4]+'_encrypted.pdf', 'wb')
            pdfWriter.write(encryptedPdf)
            encryptedPdf.close()
            pdfFile.close()
            
            # check whether decryption
            pdfCheck = PyPDF2.PdfFileReader(open(folderName+'\\'+file[:-4]+'_encrypted.pdf', 'rb'))
            if pdfCheck.decrypt(password) == 1:
                # delete original file
                os.unlink(folderName+'\\'+file)
            
            



   
   

    
    
    
    