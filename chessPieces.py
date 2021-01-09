import sys
from termcolor import colored, cprint
import defines as CONST
import assets
class chessPiece:

    def __init__(self, symbol = 'X', color = 'red', name = "null"):
        self.symbol = symbol
        self.color = color
        self.name = name
        self.selected = False
        self.first_move = True
        self.is_reversed = False # inverts all calculations
        self.moves = []

    def displayOnBoard(self):
        if(self.selected):
            return colored(self.symbol + " ", self.color, attrs=['reverse', 'bold'])
        else: 
            return colored(self.symbol + " ", self.color)

    # compares current index postion and new or selected index postion with current chess piece index movements
    # also takes current board as List() not Board()
    # max steps is by default False, but when active set it to Int value
    def isValidMove(self, cur_index, new_index, movements, board, max_steps = False): 
        # check if next move / selected move is not outside of the board
        if(new_index > 63 or new_index < 0):
            return False

        # 
        dif_index = new_index - cur_index

        reversed_check = 1
        if(dif_index < 0):
            reversed_check = -1

        dif_index = dif_index * reversed_check  

        #Check if valid Movement
        result_value = 0
        if(isinstance(movements, list)):
            for move in movements:
                if(dif_index % move == 0):
                    if(move == 1 
                    and (board[new_index][CONST.VERTICAL_INDEX] != board[cur_index][CONST.VERTICAL_INDEX]) 
                    and (board[new_index][CONST.HORIZONTAL_INDEX] != board[cur_index][CONST.HORIZONTAL_INDEX])):
                        continue
                    if(chessPiece.isValidMove(self, cur_index, new_index, move, board, max_steps)):
                        return True
        else:
            result_value = movements          
  


        if(result_value == 0):
            return False

        if(max_steps and int(dif_index / result_value) > max_steps):
            return False
        
        collision_result = self.collision(int(dif_index / result_value), cur_index, result_value, reversed_check, board)

        # Return True if no collision was found
        if(not collision_result):
            return True

        # Return True if collision was chess piece, opposite team and result matches selected/new index positions chess piece
        if(isinstance(collision_result[CONST.PIECE_INDEX], chessPiece) 
        and collision_result[CONST.PIECE_INDEX].is_reversed != self.is_reversed
        and collision_result[CONST.PIECE_INDEX] == board[new_index][CONST.PIECE_INDEX]):
            return True

        return False

    def getValidMoves(self, cur_index, board):
        #return []
        all_moves = self.getAllMoves()
        valid_moves = []
        valid_indexes = []
        new_index = cur_index
        for move in all_moves:
            new_index = cur_index + move
            while (self.isValidMove(cur_index, new_index, board)):
                valid_indexes.append(new_index)
                valid_moves.append(board[new_index][CONST.HORIZONTAL_INDEX] + board[new_index][CONST.VERTICAL_INDEX])
                new_index = new_index + move
        return list(dict.fromkeys(valid_moves))        

    def convertIndexesToPositions(self, cur_index, indexes, board):
        converted_indexes = []
        for index in indexes:
            cur_index_sample = cur_index
            cur_index_sample -= index
            converted_indexes.append(self.convertIndexToPosition(cur_index_sample, board))
        return converted_indexes

    def convertIndexToPosition(self, index, board):
        return board[index][CONST.HORIZONTAL_INDEX] + board[index][CONST.VERTICAL_INDEX]

    def getAllMoves(self):
        all_moves = []
        for move in self.moves:
            all_moves.append(move)
            all_moves.append(move * -1)
        return all_moves

    def outsideMargin(self, new_index, cur_index, board, margin = 1):
        try:
            new_horizontal = CONST.HORIZONTAL_VALUES.index(board[new_index][CONST.HORIZONTAL_INDEX])
            cur_horizontal = CONST.HORIZONTAL_VALUES.index(board[cur_index][CONST.HORIZONTAL_INDEX])

            new_vertical = int(board[new_index][CONST.VERTICAL_INDEX])
            cur_vertical = int(board[cur_index][CONST.VERTICAL_INDEX])

            vertical_dif = new_vertical - cur_vertical
            horizontal_dif = new_horizontal - cur_horizontal

            if(vertical_dif < 0): vertical_dif = vertical_dif * -1
            if(horizontal_dif < 0): horizontal_dif = horizontal_dif * -1

            if(horizontal_dif > margin or vertical_dif > margin):
                return True
            
        except IndexError:
            return True

        return False
        

    def collision(self, times, current_index, directional_index, reverse_constant, board):
        prev_index = 0
        check_current_index = current_index
        for v in range(times):     
            check_current_index = check_current_index + (directional_index * reverse_constant) 

            if(check_current_index > 63 or check_current_index < 0):
                return False

            prev_index = check_current_index - (directional_index * reverse_constant)

            if(self.outsideMargin(prev_index, check_current_index, board)):
                return board[prev_index]
   
            
            if(isinstance(board[check_current_index][CONST.PIECE_INDEX], chessPiece)):
                return board[check_current_index]
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
        self.moves = [6, 10, 15, 17]
    def isValidMove(self, cur_index, new_index, board):

        if(self.outsideMargin(cur_index, new_index, board, 2)):
            return False

        dif_index = cur_index - new_index

        if(dif_index not in self.getAllMoves()):
            return False
        
        if(not isinstance(board[new_index][CONST.PIECE_INDEX], chessPiece)):
            return True

        if(self.is_reversed != board[new_index][CONST.PIECE_INDEX].is_reversed):
            return True

        return False

    def getValidMoves(self, cur_index, board):
        #return []
        moves = self.getAllMoves()
        valid_moves = []
        for move in moves:
            if(self.isValidMove(cur_index, cur_index - move, board)):
                valid_moves.append(move)

        return self.convertIndexesToPositions(cur_index, valid_moves, board)

class Pawn(chessPiece):
    def __init__(self, color):
        super().__init__('p', color, "Pawn")
        self.moves = [16, 8, 7, 9]

    def reverse(self):
        self.is_reversed = True
        assets.invertList(self.moves)
        return self

    def isValidMove(self, cur_index, new_index, board):
        dif_index = new_index - cur_index
        if(dif_index not in self.moves):
            return False

        
        if(self.outsideMargin(cur_index, new_index, board, 2) and self.first_move):
            return False
        
        if(self.outsideMargin(cur_index, new_index, board) and not self.first_move):
            return False


        collision = self.collision(int(dif_index / dif_index), new_index, cur_index, dif_index, 1, board)

        if(not collision and assets.isOdd(dif_index)):
            return False
        elif(not collision and assets.isEven(dif_index)):
            return True

        if(collision.is_reversed == self.is_reversed):
            return False

        if(assets.isOdd(dif_index) and collision.is_reversed != self.is_reversed):
            return True
        
        return False
    
    def collision(self, times, new_index, current_index, directional_index, reverse_constant, board):
        for v in range(times):
   
            if(new_index == current_index):
                return False

            if(isinstance(board[new_index][CONST.PIECE_INDEX], chessPiece)):
                return board[new_index][CONST.PIECE_INDEX]

            new_index = new_index + (directional_index * reverse_constant)    
        
        return False
    #def getValidMoves(self, cur_index, board):
    #    return []
        
