# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:11:44 2021

@author: martsc1
"""
# Character Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for elem in range(len(grid[0])):
    for part in range(len(grid)):
        print(grid[part][elem],end='')
    print('')
        
        