# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:25:59 2021

@author: martsc1
"""
# Regex Version of the strip() Method

import re

def regexStrip(string,remove = ' '):
    stripBegin = re.compile(r'^([%s]*)' % (remove))
    start = stripBegin.search(string)
    stripEnd = re.compile(r'([%s]*)$' % (remove))
    end = stripEnd.search(string)
    print(string[len(start.group()):len(string)-len(end.group())])
    

# test                           
regexStrip('    Hello!  ')  
regexStrip('    Hello!  World =)  ')                          
regexStrip('lll Hello! ll', 'l')                         

