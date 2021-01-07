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

    def isValidMove(self, cur_index, new_index, movements, board, max_steps = False):
        dif_index = new_index - cur_index
        reversed_check = 1
        if(dif_index < 0):
            reversed_check = -1
        dif_index = dif_index * reversed_check
        #Check if valid Movement
        
        result_value = 0
        for moves in movements:
            if(dif_index % moves == 0):
                result_value = moves
                break

        if(max_steps and int(dif_index / result_value) > max_steps):
            return False
        
        results = self.collision2(int(dif_index / result_value), new_index, cur_index, result_value, reversed_check, board)
        if(not results):
            return True

        if(isinstance(results[3], chessPiece) 
        and results[3].is_reversed != self.is_reversed
        and results[3] == board[new_index][3]):
            return True

        return False


    def collision2(self, times, new_index, current_index, directional_index, reverse_constant, board, storeCollisions = False):
        for v in range(times):     
            current_index = current_index + (directional_index * reverse_constant) 
            #print("cur:", current_index)
            #print("new:", new_index)
            #print("dir:", directional_index)
            #print("board:", board[current_index][3])
            #input()        
            if(isinstance(board[current_index][3], chessPiece)):
                return board[current_index]

        return False
    
    def collision(self, times, new_index, current_index, directional_index, reverse_constant, board, storeCollisions = False):
        stored_collisions = []
        for v in range(times):
            #print(current_index)
            #print(new_index)
            #print(directional_index)
            #print(board[new_index][3])
            #input()     
            if(new_index == current_index):
                if(storeCollisions):
                    return stored_collisions
                else: 
                    return False

            if(isinstance(board[new_index][3], chessPiece)):
                if(storeCollisions):
                    stored_collisions.append(board[new_index])
                else:
                    return board[new_index][3]

            new_index = new_index + (directional_index * reverse_constant)    
            
        if(storeCollisions):
            return stored_collisions
        else: 
            return False

    def reverse(self):
        self.is_reversed = True
        return self



class King(chessPiece):
    def __init__(self, color):
       super().__init__('K', color, "King")
    def isValidMove(self, cur_index, new_index, board):
        return super().isValidMove(cur_index, new_index, [7, 9, 8, 1], board, 1)

class Queen(chessPiece):
    def __init__(self, color):
        super().__init__('Q', color, "Queen")
    def isValidMove(self, cur_index, new_index, board):
        return super().isValidMove(cur_index, new_index, [7, 9, 8, 1], board)

class Rook(chessPiece):
    def __init__(self, color):
        super().__init__('r', color, "Rook")
    def isValidMove(self, cur_index, new_index, board):
        return super().isValidMove(cur_index, new_index, [8, 1], board)

class Bishop(chessPiece):
    def __init__(self, color):
        super().__init__('b', color, "Bishop")
    def isValidMove(self, cur_index, new_index, board):
        return super().isValidMove(cur_index, new_index, [9, 7], board)

class Knight(chessPiece):
    def __init__(self, color):
        super().__init__('k', color, "Knight")

    def isValidMove(self, cur_index, new_index, board):
        dif_index = cur_index - new_index
        print(dif_index)
        if(dif_index != 10 and dif_index != -10  
            and dif_index != 15 and dif_index != -15
            and dif_index != 17 and dif_index != -17
            and dif_index != 6 and dif_index != -6):
            return False
        if(not isinstance(board[new_index][3], chessPiece)):
            return True
        if(self.is_reversed == board[new_index][3].is_reversed):
            return False
        return False

class Pawn(chessPiece):
    def __init__(self, color):
        super().__init__('p', color, "Pawn")

    def isValidMove(self, cur_index, new_index, board):
        dif_index = cur_index - new_index
        reversed_check = 1

        if(not self.is_reversed):
            reversed_check = -1
        dif_index = dif_index * reversed_check

        if(dif_index == 7 or dif_index == 9):
            result = self.collision(int(dif_index / dif_index), new_index, cur_index, dif_index, reversed_check, board)
            print(result)
            if(isinstance(result, chessPiece) and result.is_reversed != self.is_reversed):
                return True

        elif((dif_index == 16 and self.first_move) or dif_index == 8):
            if(not self.collision(int(dif_index / 8), new_index, cur_index, 8, reversed_check, board)):
                return True

        return False
        
