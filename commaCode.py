# Comma Code
import sys
def commaCode(spam):
    if len(spam) > 0:
        
        for i in range(len(spam)):
            if not isinstance(spam[i], str):
                spam[i] = str(spam[i])
                
        spam.insert(-1,'and')
        result = ', '.join(spam)
        print(result)
    else:
        print('Input is empty')
        
    
commaCode(['apples', 'bananas', 'tofu', 'cats'])
commaCode([])
commaCode([1, 2, 'apples', 'pears'])
