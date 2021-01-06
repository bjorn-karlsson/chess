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

    def isValidMove(self, piece):
        if(not isinstance(piece, chessPiece)):
            return True
        if(self.is_reversed == piece.is_reversed):
            return False
        return True


        

    def reverse(self):
        self.is_reversed = True
        return self



class King(chessPiece):
    def __init__(self, color):
       super().__init__('K', color, "King")
    def isValidMove(self, cur_index, new_index, piece):
        pass

class Queen(chessPiece):
    def __init__(self, color):
        super().__init__('Q', color, "Queen")
    def isValidMove(self, cur_index, new_index, piece):
        pass
class Rook(chessPiece):
    def __init__(self, color):
        super().__init__('r', color, "Rook")
    def isValidMove(self, cur_index, new_index, piece):
        pass

class Bishop(chessPiece):
    def __init__(self, color):
        super().__init__('b', color, "Bishop")
    def isValidMove(self, cur_index, new_index, piece):
        pass


class Knight(chessPiece):
    def __init__(self, color):
        super().__init__('k', color, "Knight")
    def isValidMove(self, cur_index, new_index, piece):
        dif_index = cur_index - new_index
        print(dif_index)
        if(dif_index != 10 and dif_index != -10  
            and dif_index != 15 and dif_index != -15
            and dif_index != 17 and dif_index != -17
            and dif_index != 6 and dif_index != -6):
            return False
        return super().isValidMove(piece)
class Pawn(chessPiece):
    def __init__(self, color):
        super().__init__('p', color, "Pawn")

    def isValidMove(self, cur_index, new_index, piece):
        dif_index = cur_index - new_index
        if(not self.is_reversed):
            dif_index = dif_index * -1

        if(dif_index == 7 or dif_index == 9):
            if(isinstance(piece, chessPiece)):
                if(self.is_reversed != piece.is_reversed):
                    return True

        elif((dif_index == 16 and self.first_move) or dif_index == 8):
            if(not isinstance(piece, chessPiece)):
                return True

        return False
        
