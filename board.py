from copy import deepcopy
from chessPieces import *

class Place:

    def __init__(self, symbol, color):
        self.symbol = symbol
        self.color = color
        self.selected = False

    def displayOnBoard(self):
        if(self.selected):
            return colored(self.symbol + " ", self.color, attrs=['bold'])
        else: 
            return colored(self.symbol + " ", self.color)


class Board:

    def __init__(self, player_color1, player_color2, color1 = 'red' , color2 = 'blue'):
        self.__board = []
        self.board_positions = []
        self.player_color1 = player_color1
        self.player_color2 = player_color2
        self.color1 = color1 
        self.color2 = color2

    def __str__(self):
        if len(self.__board) != 64:
                return ""
        output = "\n "
        for place in CONST.HORIZONTAL_VALUES:
            output += " " + place 
        output += "\n"
        count = 1 
        for place in self.__board:
            output += ""
            if(count < 8):
                if(count == 1):
                    if(isinstance(place[CONST.PIECE_INDEX], chessPiece)):
                        output += place[CONST.VERTICAL_INDEX] + " " + place[CONST.PIECE_INDEX].displayOnBoard()
                    else:
                        output += place[CONST.VERTICAL_INDEX] + " " + place[CONST.PLACE_INDEX].displayOnBoard()
                else:
                    if(isinstance(place[CONST.PIECE_INDEX], chessPiece)):
                        output += place[CONST.PIECE_INDEX].displayOnBoard()
                    else: 
                        output += place[CONST.PLACE_INDEX].displayOnBoard()

                count += 1
            else:
                if(isinstance(place[CONST.PIECE_INDEX], chessPiece)):
                    output += place[CONST.PIECE_INDEX].displayOnBoard()  + place[CONST.VERTICAL_INDEX] + "\n"
                else:
                    output += place[CONST.PLACE_INDEX].displayOnBoard() + place[CONST.VERTICAL_INDEX] + "\n"
                count = 1


        output += " "
        for place in CONST.HORIZONTAL_VALUES:
            output += " " + place 
        
        return output

    # Adds pieces to the board
    def __initBoardPieces(self):

        #PROMOTION 
        #self.addPiece('e8', King(self.player_color2).reverse())
        #self.addPiece('e1', King(self.player_color1))

        #self.addPiece('b5', Pawn(self.player_color1))
        #self.addPiece('c4', Pawn(self.player_color2).reverse())
        #return

        ## CASTLING 
        self.addPiece('a8', Rook(self.player_color1))
        self.addPiece('h8', Rook(self.player_color1))
        self.addPiece('e8', King(self.player_color1))

        self.addPiece('c1', Bishop(self.player_color2).reverse())

        self.addPiece('a1', Rook(self.player_color2).reverse())
        self.addPiece('h1', Rook(self.player_color2).reverse())
        self.addPiece('e1', King(self.player_color2).reverse())
        return 
        #Rooks
        self.addPiece('a1', Rook(self.player_color1)), self.addPiece('a8', Rook(self.player_color2).reverse())
        self.addPiece('h1', Rook(self.player_color1)), self.addPiece('h8', Rook(self.player_color2).reverse())
        # Knights
        self.addPiece('b1', Knight(self.player_color1)), self.addPiece('b8', Knight(self.player_color2).reverse())
        self.addPiece('g1', Knight(self.player_color1)), self.addPiece('g8', Knight(self.player_color2).reverse())

        # Bishops
        self.addPiece('c1', Bishop(self.player_color1)), self.addPiece('c8', Bishop(self.player_color2).reverse())
        self.addPiece('f1', Bishop(self.player_color1)), self.addPiece('f8', Bishop(self.player_color2).reverse())

        # Kings and Queens
        self.addPiece('d1', Queen(self.player_color1)),  self.addPiece('d8', Queen(self.player_color2).reverse())
        self.addPiece('e1', King(self.player_color1)),   self.addPiece('e8', King(self.player_color2).reverse())

        # Pawns
        self.addPiece('a2', Pawn(self.player_color1)), self.addPiece('b2', Pawn(self.player_color1)), self.addPiece('c2', Pawn(self.player_color1)), self.addPiece('d2', Pawn(self.player_color1))
        self.addPiece('e2', Pawn(self.player_color1)), self.addPiece('f2', Pawn(self.player_color1)), self.addPiece('g2', Pawn(self.player_color1)), self.addPiece('h2', Pawn(self.player_color1))
        
        self.addPiece('a7', Pawn(self.player_color2).reverse()), self.addPiece('b7', Pawn(self.player_color2).reverse()), self.addPiece('c7', Pawn(self.player_color2).reverse()), self.addPiece('d7', Pawn(self.player_color2).reverse())
        self.addPiece('e7', Pawn(self.player_color2).reverse()), self.addPiece('f7', Pawn(self.player_color2).reverse()), self.addPiece('g7', Pawn(self.player_color2).reverse()), self.addPiece('h7', Pawn(self.player_color2).reverse())

    # Creates the 8x8 chess board
    # real examples: board = [["a", "1", "x", Rook], ["b", "1", "+", Knight] ... ["h", "6", "x", None], ["a", "7", "x", Pawn]]
    def initBoard(self):
        CONST.HORIZONTAL_VALUES
        color_counter = 0

        for v in range(1,9):
            for h in CONST.HORIZONTAL_VALUES:
                if color_counter % 2 == 0:
                    self.__board.append([h, str(v), Place("x", self.color1), None])
                    self.board_positions.append(h + str(v))
                else:
                    self.__board.append([h, str(v), Place('+', self.color2), None])
                    self.board_positions.append(h + str(v))
                color_counter +=1
            if color_counter % 2 != 1:
                color_counter = 1
            else:
                color_counter = 0
            
        self.__initBoardPieces()

    # Adds a single piece to a specific board position, ex: pos: "a1", piece: Rook()
    def addPiece(self, position, piece):
        if(isinstance(piece, chessPiece)):
            self.__board[self.positionToIndex(position)][CONST.PIECE_INDEX] = piece      

    # Removes a single piece by board position, ex: "a1"  or "h8"
    def removePieceByPosition(self, position):
        self.__board[self.positionToIndex(position)][CONST.PIECE_INDEX] = None

    # chech if position is a real (and a piece), ex: "a1" is inside the board and "a1" is Chess Piece
    def validPosition(self, position, check_for_piece = True):
        if(position not in self.board_positions):
            #print("Must select a real position")
            return False  

        if(not isinstance(self.__board[self.positionToIndex(position)][CONST.PIECE_INDEX], chessPiece) and check_for_piece):
            #print("Must select a chess piece")
            return False
    
        return True
        
    def getValidMovesOfPosition(self, position):
        if(position in self.board_positions):
            if(isinstance(self.__board[self.positionToIndex(position)][CONST.PIECE_INDEX], chessPiece)):
                return self.__board[self.positionToIndex(position)][CONST.PIECE_INDEX].getValidMoves(self.positionToIndex(position), self.__board)
        return []
    # Try to move a selected piece from current position to a new position

    def getPositionByPiece(self, piece):
        for place in self.__board:
            if(place[CONST.PIECE_INDEX] == piece):
                return place[CONST.HORIZONTAL_INDEX] + place[CONST.VERTICAL_INDEX]

    def getPositionsByPieces(self, pieces):
        positions = []
        for piece in pieces:
            positions.append(self.getPositionByPiece(piece))
        return positions

    def getPieces(self, player_delimiter):
        is_reversed = bool
        if(player_delimiter == 1):
            is_reversed = False
        elif(player_delimiter == 2):
            is_reversed = True
        else:
            return []
        pieces = []

        for place in self.__board:
            if(isinstance(place[CONST.PIECE_INDEX], chessPiece)
            and is_reversed == place[CONST.PIECE_INDEX].is_reversed):
                pieces.append(place[CONST.PIECE_INDEX])
        return pieces

    def getKingPosition(self, player_delimiter):
        is_reversed = bool
        if(player_delimiter == 1):
            is_reversed = False
        elif(player_delimiter == 2):
            is_reversed = True
        else:
            return None
        for place in self.__board:
            if(isinstance(place[CONST.PIECE_INDEX], King)
            and is_reversed == place[CONST.PIECE_INDEX].is_reversed):
                return place[CONST.HORIZONTAL_INDEX] + place[CONST.VERTICAL_INDEX]
            
        
        raise Exception('NoKingFound', f'No king found for player({player_delimiter})')
        
    def promotionAvailable(self, player_delimiter):
        
        pawn_positions = self.getPositionsByPieces(list(filter(lambda piece: isinstance(piece, Pawn), self.getPieces(player_delimiter))))
        pawn_promotions = []
        for pawn_position in pawn_positions:
            if(self.getValidMovesOfPosition(pawn_position) == [] 
            and ((self.positionToIndex(pawn_position) + 8) > 63 
            or (self.positionToIndex(pawn_position) - 8) < 0)):
                pawn_promotions.append(pawn_position)
        if(pawn_promotions != []):
            return pawn_promotions

        return False

    def castling(self, cur_position_index, new_position_index):

        
        current_position = self.indexToPosition(cur_position_index) 

        if(current_position == "h8" or current_position == "h1"):
            if(isinstance(self.__board[cur_position_index - 1][CONST.PIECE_INDEX ], chessPiece)
            or isinstance(self.__board[cur_position_index - 2][CONST.PIECE_INDEX ], chessPiece)):
                return False
            self.__board[cur_position_index][CONST.PIECE_INDEX].first_move = False
            self.__board[new_position_index][CONST.PIECE_INDEX].first_move = False         

            self.__board[cur_position_index - 2][CONST.PIECE_INDEX] = self.__board[cur_position_index][CONST.PIECE_INDEX]
            self.__board[new_position_index + 2][CONST.PIECE_INDEX] = self.__board[new_position_index][CONST.PIECE_INDEX]

            self.__board[cur_position_index][CONST.PIECE_INDEX] = None
            self.__board[new_position_index][CONST.PIECE_INDEX] = None
            return True
        elif(current_position == "a8" or current_position == "a1"):
            if(isinstance(self.__board[cur_position_index + 1][CONST.PIECE_INDEX ], chessPiece)
            or isinstance(self.__board[cur_position_index + 2][CONST.PIECE_INDEX ], chessPiece)
            or isinstance(self.__board[cur_position_index + 3][CONST.PIECE_INDEX ], chessPiece)):
                return False

            self.__board[cur_position_index][CONST.PIECE_INDEX].first_move = False
            self.__board[new_position_index][CONST.PIECE_INDEX].first_move = False

            self.__board[cur_position_index + 3][CONST.PIECE_INDEX] = self.__board[cur_position_index][CONST.PIECE_INDEX]
            self.__board[new_position_index - 2][CONST.PIECE_INDEX] = self.__board[new_position_index][CONST.PIECE_INDEX]

            self.__board[cur_position_index][CONST.PIECE_INDEX] = None
            self.__board[new_position_index][CONST.PIECE_INDEX] = None
            return True

        return False
        ##SHORT
        #if(cur_position_index == 63 or cur_position_index == )

        #    return False

        ##LONG


        #print(real_dif)

    

    def movePiecePosition(self, current_position, new_position, get_replaced = False):

        if(current_position == new_position):
            return False

        current_position_index = self.positionToIndex(current_position)
        new_position_index = self.positionToIndex(new_position)

        if(new_position_index > 63 or new_position_index < 0):
            return False
        
        if(not isinstance(self.__board[current_position_index][CONST.PIECE_INDEX], chessPiece)):
            return False

        result = self.__board[current_position_index][CONST.PIECE_INDEX].isValidMove(current_position_index, new_position_index, self.__board)
        if(not result):
            return False

        if(result == CONST.CASTLING_VALUE):  
            return self.castling(current_position_index, new_position_index)
                
        

        replaced_positions = None
        if(get_replaced):
            replaced_positions = self.__board[new_position_index][CONST.PIECE_INDEX]

        self.__board[current_position_index][CONST.PIECE_INDEX].first_move = False
        self.__board[new_position_index][CONST.PIECE_INDEX] = self.__board[current_position_index][CONST.PIECE_INDEX]
        self.__board[current_position_index][CONST.PIECE_INDEX] = None
        
        if(get_replaced):
            return replaced_positions
        
        return True

    def isCheckMate(self, attacking_player_positions, defending_player_piece_positions, king_position):
        copy_of_board = deepcopy(self.__board)
        #input()
        copy_of_king_position = king_position
        #copy_of_board = self.__board[:]
        #print(len(copy_of_board))
        #print(len(self.__board))
        
        #print("isCheckMate?")
        #print("attacking:" , attacking_player_positions)
        #print("defending:" , defending_player_piece_positions)
        #print("king:" , king_position)
        #input()
        #print ("\n")

        for defending_player_piece_position in defending_player_piece_positions:
            defending_player_piece_position_index = self.positionToIndex(defending_player_piece_position)
            defending_player_piece = self.__board[defending_player_piece_position_index][CONST.PIECE_INDEX]
            defending_player_piece_moves = self.getValidMovesOfPosition(defending_player_piece_position)
            #print("Check position moves:", defending_player_piece_position)
            #print("Position Index:", defending_player_piece_position_index)
            #print("Piece:", defending_player_piece.name)
            #print("Avalible moves:", defending_player_piece_moves)
            #input()
            #print("\n")

            for defending_player_move in defending_player_piece_moves:
                #print(self.positionToIndex("a7"))
                king_position = copy_of_king_position
                #print(self.__board[48])
                #print(copy_of_board[48])
                #input()
                self.movePiecePosition(defending_player_piece_position, defending_player_move)
 

                if(king_position == defending_player_piece_position):
                    king_position = defending_player_move

                #input()
                if(not self.isMate(attacking_player_positions, king_position)):
                    #self.movePiecePosition(defending_player_move, defending_player_piece_position)
                    #print(self.__str__())
                    #input()
                    self.__board = deepcopy(copy_of_board)
                    
                    return False
                
                
                #self.movePiecePosition(defending_player_move, defending_player_piece_position)
                #self.addPiece(defending_player_move, result)
                #self.__board = copy_of_board
                
                self.__board = deepcopy(copy_of_board)
        
        self.__board = deepcopy(copy_of_board)
        return True
    def isMate(self, player_piece_positions, king_position, board = False):
        #print("isMate?")
        #print("attacking:" , player_piece_positions)
        ##print("king:" , king_position)
        #print("king:" , king_position)
        #print("e7", self.__board[self.positionToIndex("e7")])
        #input()
        if(not board):
            board = self.__board
        king_index = self.positionToIndex(king_position)
        for player_piece_position in player_piece_positions:

            player_piece_index = self.positionToIndex(player_piece_position)
            #print(self.board_positions)
            #print(player_piece_position)
            #print(player_piece_index)
            #print(self.__board[player_piece_index])
            #input()
            if(not isinstance(board[player_piece_index][CONST.PIECE_INDEX], chessPiece)):
                continue

            if(board[player_piece_index][CONST.PIECE_INDEX].isValidMove(player_piece_index, king_index, board)):
                #print("True")
                #input()
                return True
        #print("False")
        #input()
        return False
    # Toogles the highlight of given positions chess piece
    def toogleSelectedPieces(self, positions): 

        if(not isinstance(positions, list)):
            positions = [positions]
        for position in positions:
            if(isinstance(self.__board[self.positionToIndex(position)][CONST.PIECE_INDEX], chessPiece)):
                self.__board[self.positionToIndex(position)][CONST.PIECE_INDEX].selected = not self.__board[self.positionToIndex(position)][CONST.PIECE_INDEX].selected
            else:
                self.__board[self.positionToIndex(position)][CONST.PLACE_INDEX].selected = not self.__board[self.positionToIndex(position)][CONST.PLACE_INDEX].selected
    
    def getBoardByIndexOfPosition(self, index):
        return self.__board[index][CONST.PIECE_INDEX]


   # Returns the vertical and horizontal values as an array
    def positionToArray(position):
        return [position[0], position[1]]

    # Simply returns index of given position, ex: "a1" => 0 or "h8" => 63
    def positionToIndex(self, position):
        return self.board_positions.index(position)

    # Simply returns position of given index, ex: 0 => "a1" or 63 => "h8"
    def indexToPosition(self, index):
        return self.board_positions[index]
