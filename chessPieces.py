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
        self.moves = []
        self.horizontals = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def setCurrentPosition(self, position):
        self.current_board_position = position

    def displayOnBoard(self):
        if(self.selected):
            return colored(self.symbol + " ", self.color, attrs=['reverse', 'bold'])
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
                if(moves == 1 and board[new_index][1] != board[cur_index][1]):
                    return False
                result_value = moves
                break
        
        if(result_value == 0):
            return False

        if(max_steps and int(dif_index / result_value) > max_steps):
            return False
        
        results = self.collision2(int(dif_index / result_value), new_index, cur_index, result_value, reversed_check, board)
        #print(new_index)

        ##FIX QUEEN BUG##

        if(new_index == 56):
            print(board[new_index])
            print(results)
            input()

        if(not results):
            return True
        try:
            if(isinstance(results[3], chessPiece) 
            and results[3].is_reversed != self.is_reversed
            and results[3] == board[new_index][3]):
                return True
        except IndexError:
            print("INVALID INDEX:", new_index)
            input()
            return False
        return False

    def getValidMoves(self, cur_index, board):
        all_moves = self.getAllMoves()
        valid_moves = []
        #valid_indexes = []
        for move in all_moves:
            new_index = cur_index + move
            if(new_index < 0 or new_index > 63):
                continue
            while (self.isValidMove(cur_index, new_index, board)):
                if(new_index < 0 or new_index > 63):
                    break
                #valid_indexes.append(new_index)
                valid_moves.append(board[new_index][0] + board[new_index][1])
                #print("\nMove:", move)
                #print("CurI:", cur_index)
                #print("newI:", new_index)
                
                #print("Valid:", self.isValidMove(cur_index, new_index, board))
                #input()
                new_index = new_index + move
        
        #print(valid_moves)
        #input()
        return valid_moves
        
         

    def getAllMoves(self):
        all_moves = []
        for move in self.moves:
            all_moves.append(move)
            all_moves.append(move * -1)
        return all_moves

    def collision2(self, times, new_index, current_index, directional_index, reverse_constant, board):
        prev_index = 0
        for v in range(times):     
            
            current_index = current_index + (directional_index * reverse_constant) 

            if(current_index > 63 or current_index < 0):
                return False

            prev_index = current_index - (directional_index * reverse_constant)
            prev_horizontal = self.horizontals.index(board[prev_index][0])
            cur_horizontal = self.horizontals.index(board[current_index][0])
            prev_vertical = int(board[prev_index][1])
            cur_vertical = int(board[current_index][1])

            vertical_dif = prev_vertical - cur_vertical
            horizontal_dif = prev_horizontal - cur_horizontal
            if(vertical_dif < 0): vertical_dif = vertical_dif * -1
            if(horizontal_dif < 0): horizontal_dif = horizontal_dif * -1



            if(horizontal_dif > 1 or vertical_dif > 1):
                return board[prev_index]

            if(board[current_index][0] == "a" and board[current_index][1] == "8"):
                print(board[current_index])           
                print("prev_pos:", board[prev_index][0],  board[prev_index][1])
                print("ph:", prev_horizontal)
                print("pv:", prev_vertical, "\n")
                print("cur_pos:", board[current_index][0],  board[current_index][1])
                print("ch:", cur_horizontal)
                print("cv:", cur_vertical, "\n")
                print("diffh:", horizontal_dif)
                print("diffv:", vertical_dif)
                print(directional_index * reverse_constant)
                input()
            #print("cur:", current_index)
            #print("new:", new_index)
            #print("prev", prev_index)
            #print("dir:", directional_index)
            #print("prev_pos:", board[prev_index][0],  board[prev_index][1])
            #print("cur_pos:", board[current_index][0],  board[current_index][1])
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


# Related pieces

class King(chessPiece):
    def __init__(self, color):
       super().__init__('K', color, "King")
       self.moves = [9, 7, 8, 1]
    def isValidMove(self, cur_index, new_index, board):
        return super().isValidMove(cur_index, new_index, self.moves, board, 1)
class Queen(chessPiece):
    def __init__(self, color):
        super().__init__('Q', color, "Queen")
        self.moves = [9, 7, 8, 1]
    def isValidMove(self, cur_index, new_index, board):
        return super().isValidMove(cur_index, new_index, self.moves, board)
            

class Rook(chessPiece):
    def __init__(self, color):
        super().__init__('r', color, "Rook")
        self.moves = [8, 1]
    def isValidMove(self, cur_index, new_index, board):
        return super().isValidMove(cur_index, new_index, self.moves, board)
class Bishop(chessPiece):
    def __init__(self, color):
        super().__init__('b', color, "Bishop")
        self.moves = [9, 7]
    def isValidMove(self, cur_index, new_index, board):
        return super().isValidMove(cur_index, new_index, self.moves, board)

# Unique pieces

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
        if(self.is_reversed != board[new_index][3].is_reversed):
            return True
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
        
