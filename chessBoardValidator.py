# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:38:22 2021

@author: martsc1
"""
# Chess Dictionary Validator
#A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, 
#at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. 
#The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', 
#or 'king'. This function should detect when a bug has resulted in an improper chess board.

def isValidChessBoard(chessBoard):
    goodBoard = True
    validSpaces = []
    for letter in [chr(i) for i in range(ord('a'),ord('i'))]:
        for num in range(1,9):
            validSpaces.append(str(num)+letter)
        
    
    if sum(value == 'bking' for value in chessBoard.values()) != 1:
        print('Invalid number of black kings.')
        goodBoard = False
    elif sum(value == 'wking' for value in chessBoard.values()) != 1:
        print('Invalid number of white kings.')
        goodBoard = False
    elif len(chessBoard) > 32:
        print('Too many pieces on the board.')
        goodBoard = False
    elif sum(value == 'bpawn' for value in chessBoard.values()) > 8:
        print('Too many black pawns on the board.')
        goodBoard = False
    elif sum(value == 'wpawn' for value in chessBoard.values()) > 8:
        print('Too many white pawns on the board.')
        goodBoard = False
    for elem in chessBoard.items():
        if elem[0] not in validSpaces:
            print('Not all chess pieces are on valid spaces.')
            goodBoard = False
        elif elem[1][0] not in ['b','w']:
            print('Not all chess pieces have a valid color.')
            goodBoard = False
        elif elem[1][1:] not in ['pawn', 'knight', 'bishop', 'rook', 'queen','king']:
            print('Not all chess pieces have a valid name.')
            goodBoard = False
            
    if goodBoard:
        print('The chess board seems correct!')
        

            
        
    