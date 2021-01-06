import sys
from termcolor import colored, cprint

class chessPiece:

    def __init__(self, symbol = 'X', color = 'red', name = "null"):
        self.symbol = symbol
        self.color = color
        self.name = name
        self.move_count = 0
        self.selected = False
        self.first_move = True
        self.is_reversed = False # inverts all calculations

    def setCurrentPosition(self, position):
        self.current_board_position = position

    def displayOnBoard(self):
        if(self.selected):
            return colored(self.symbol + " ", self.color, attrs=['bold'])
        else: 
            return colored(self.symbol + " ", self.color)

    def isValidMove(self):
        return True

    def reverse(self):
        self.is_reversed = True
        return self



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

    def isValidMove(self, cur_index, new_index, board):
        contains_piece = isinstance(board[new_index][3], chessPiece)
        steps = 0
        if(self.is_reversed):
            while(cur_index > new_index and cur_index != new_index):
                cur_index -= 8
                steps += 1  
        else:
            while(cur_index < new_index and cur_index != new_index):
                cur_index += 8
                steps += 1
        print(new_index - cur_index, steps)
        result = new_index - cur_index

        if ((steps == 2 or steps == 1) and self.first_move and result == 0 and not contains_piece):
            return True
        elif(steps == 1 and result == 0 and not contains_piece):
            return True
        elif((result == -1 or result == 1) and steps == 1 and contains_piece):
            return True
        elif(result == 7 and steps == 2 and contains_piece):
            return True
        else: 
            return False

