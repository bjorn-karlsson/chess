import sys
from termcolor import colored, cprint

class chessPiece:

    def __init__(self, symbol = 'X', color = 'red', name = "null"):
        self.symbol = symbol
        self.color = color
        self.name = name
        self.moveCount = 0
        self.selected = False

    def displayOnBoard(self):
        if(self.selected):
           
            return colored(self.symbol + " ", self.color, attrs=['bold'])
        else: 
            return colored(self.symbol + " ", self.color)

    def isValidMove(self):
        return True

class King(chessPiece):
    def __init__(self, color):
       super().__init__('K', color, "King")

class Queen(chessPiece):
    def __init__(self, color):
        super().__init__('Q', color, "Queen")

class Rook(chessPiece):
    def __init__(self, color):
        super().__init__('r', color, "Rook")

class Bishop(chessPiece):
    def __init__(self, color):
        super().__init__('b', color, "Bishop")

class Knight(chessPiece):
    def __init__(self, color):
        super().__init__('k', color, "Knight")

class Pawn(chessPiece):
    def __init__(self, color):
        super().__init__('p', color, "Pawn")