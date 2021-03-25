# -*- coding: utf-8 -*-
"""

@author: martsc1
"""
# Brute-Force PDF Password Breaker
import PyPDF2,sys

# Read dictionary
dictionary = open('C:\\Users\\martsc1\\Documents\\Online courses\\automate the boring stuff\\automate_online-materials\\dictionary.txt')
dictionaryLines = dictionary.readlines()
#remove line seperators
dictionaryWords = [x[:-1] for x in dictionaryLines]
    
print('Enter the direct path to the pdf you want to decrypt:')
file2decrypt = input()


pdfFile = open(file2decrypt, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)


# loop through dictionary words
for iWords in range(len(dictionaryWords)):
    # check whether decryption worked
    if pdfReader.decrypt(dictionaryWords[iWords]) == 1:
        print('PDF decrypted! The password is: \n'+dictionaryWords[iWords])
        sys.exit()
    elif pdfReader.decrypt(dictionaryWords[iWords].lower()) == 1:
        print('PDF decrypted! The password is: \n'+dictionaryWords[iWords].lower())
        sys.exit()

    
print('Password not in dictionary')