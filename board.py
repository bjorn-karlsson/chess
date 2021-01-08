import sys
from termcolor import colored, cprint

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
    
    def __init__(self):
        self.__board = []
        self.board_positions = []
        self.horizontals = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.position_indexes = { "horizontal":0, "vertical":1, "place":2, "piece":3 }
    def __str__(self):
        if len(self.__board) != 64:
                return ""
        output = " "
        for place in self.horizontals:
            output += " " + place 
        output += "\n"
        count = 1
        print() 
        for place in self.__board:
            output += ""
            if(count < 8):
                if(count == 1):
                    if(isinstance(place[self.position_indexes.get("piece")], chessPiece)):
                        output += place[self.position_indexes.get("vertical")] + " " + place[self.position_indexes.get("piece")].displayOnBoard()
                    else:
                        output += place[self.position_indexes.get("vertical")] + " " + place[self.position_indexes.get("place")].displayOnBoard()
                else:
                    if(isinstance(place[self.position_indexes.get("piece")], chessPiece)):
                        output += place[self.position_indexes.get("piece")].displayOnBoard()
                    else: 
                        output += place[self.position_indexes.get("place")].displayOnBoard()

                count += 1
            else:
                if(isinstance(place[self.position_indexes.get("piece")], chessPiece)):
                    output += place[self.position_indexes.get("piece")].displayOnBoard()  + place[self.position_indexes.get("vertical")] + "\n"
                else:
                    output += place[self.position_indexes.get("place")].displayOnBoard() + place[self.position_indexes.get("vertical")] + "\n"
                count = 1


        output += " "
        for place in self.horizontals:
            output += " " + place 
        return output     
    def old__str__(self):
        if len(self.__board) != 64:
            return ""
        output = "\n "
        for place in self.horizontals:
            output += " " + place 
        output += "\n"
        count = 0
        for place in self.__board:

            if(count < 8):
                if (count == 0):
                    output += place[self.position_indexes.get("vertical")] + " "
                if(isinstance(place[self.position_indexes.get("piece")], chessPiece)):
                    output += place[self.position_indexes.get("piece")].displayOnBoard()
                else:
                    output += place[self.position_indexes.get("place")] + " "
                
            else:
                
                output += '\n' + place[self.position_indexes.get("vertical")] + " "
                
                if(isinstance(place[self.position_indexes.get("piece")], chessPiece)):
                    output += place[self.position_indexes.get("piece")].displayOnBoard()
                else:
                    output += place[self.position_indexes.get("place")] + " "
                count = 0

            count += 1


        output += "\n "
        for place in self.horizontals:
            output += " " + place 
        return output

    # Adds pieces to the board
    def __initBoardPieces(self):
        self.addPiece('a1', Queen('green'))
        #self.addPiece('h8', Rook('green'))
        return 
        #Rooks
        self.addPiece('a1', Rook('green')), self.addPiece('a8', Rook('yellow').reverse())
        self.addPiece('h1', Rook('green')), self.addPiece('h8', Rook('yellow').reverse())
        # Knights
        self.addPiece('b1', Knight('green')), self.addPiece('b8', Knight('yellow').reverse())
        self.addPiece('g1', Knight('green')), self.addPiece('g8', Knight('yellow').reverse())

        # Bishops
        self.addPiece('c1', Bishop('green')), self.addPiece('c8', Bishop('yellow').reverse())
        self.addPiece('f1', Bishop('green')), self.addPiece('f8', Bishop('yellow').reverse())

        # Kings and Queens
        self.addPiece('d1', Queen('green')),  self.addPiece('d8', Queen('yellow').reverse())
        self.addPiece('e1', King('green')),   self.addPiece('e8', King('yellow').reverse())

        # Pawns
        self.addPiece('a2', Pawn('green')), self.addPiece('b2', Pawn('green')), self.addPiece('c2', Pawn('green')), self.addPiece('d2', Pawn('green'))
        self.addPiece('e2', Pawn('green')), self.addPiece('f2', Pawn('green')), self.addPiece('g2', Pawn('green')), self.addPiece('h2', Pawn('green'))
        
        self.addPiece('a7', Pawn('yellow').reverse()), self.addPiece('b7', Pawn('yellow').reverse()), self.addPiece('c7', Pawn('yellow').reverse()), self.addPiece('d7', Pawn('yellow').reverse())
        self.addPiece('e7', Pawn('yellow').reverse()), self.addPiece('f7', Pawn('yellow').reverse()), self.addPiece('g7', Pawn('yellow').reverse()), self.addPiece('h7', Pawn('yellow').reverse())

    # Creates the 8x8 chess board
    # real examples: board = [["a", "1", "x", Rook], ["b", "1", "+", Knight] ... ["h", "6", "x", None], ["a", "7", "x", Pawn]]
    def initBoard(self):
        self.horizontals
        color_counter = 0

        for v in range(1,9):
            for h in self.horizontals:
                if color_counter % 2 == 0:
                    self.__board.append([h, str(v), Place("x", 'red'), None])
                    self.board_positions.append(h + str(v))
                else:
                    self.__board.append([h, str(v), Place('+', 'blue'), None])
                    self.board_positions.append(h + str(v))
                color_counter +=1
            if color_counter % 2 != 1:
                color_counter = 1
            else:
                color_counter = 0
            
        self.__initBoardPieces()

    # Adds a single piece to a specific board position, ex: pos: "a1", piece: Rook()
    def addPiece(self, position, piece):
        self.__board[self.positionToIndex(position)][self.position_indexes.get("piece")] = piece      

    # Removes a single piece by board position, ex: "a1"  or "h8"
    def removePieceByPosition(self, position):
        self.__board[self.positionToIndex(position)][self.position_indexes.get("piece")] = None

    # chech if position is a real (and a piece), ex: "a1" is inside the board and "a1" is Chess Piece
    def validPosition(self, position, check_for_piece = True):
        if(position not in self.board_positions):
            print("Must select a real position")
            return False  

        if(not isinstance(self.__board[self.positionToIndex(position)][self.position_indexes.get("piece")], chessPiece) and check_for_piece):
            print("Must select a chess piece")
            return False
    
        return True
        
    def getValidMovesOfPosition(self, position):
        if(position in self.board_positions):
            if(isinstance(self.__board[self.positionToIndex(position)][self.position_indexes.get("piece")], chessPiece)):
                return self.__board[self.positionToIndex(position)][self.position_indexes.get("piece")].getValidMoves(self.positionToIndex(position), self.__board)
        return []
    # Try to move a selected piece from current position to a new position
    def movePiecePosition(self, current_position, new_position):

        if(current_position == new_position):
            print("cannot move to same location")
            return False

        current_position_index = self.positionToIndex(current_position)
        new_position_index = self.positionToIndex(new_position)

        if(not self.__board[current_position_index][self.position_indexes.get("piece")].isValidMove(current_position_index, new_position_index, self.__board)):
            print("Cannot move " + self.__board[current_position_index][self.position_indexes.get("piece")].name + " to: " + new_position)
            return False

        self.__board[current_position_index][self.position_indexes.get("piece")].first_move = False
        self.__board[new_position_index][self.position_indexes.get("piece")] = self.__board[current_position_index][self.position_indexes.get("piece")]
        self.__board[current_position_index][self.position_indexes.get("piece")] = None
            
        return True

    # Toogles the highlight of given positions chess piece
    def toogleSelectedPieces(self, positions): 
        if(not isinstance(positions, list)):
            positions = [positions]
        for position in positions:
            if(isinstance(self.__board[self.positionToIndex(position)][self.position_indexes.get("piece")], chessPiece)):
                self.__board[self.positionToIndex(position)][self.position_indexes.get("piece")].selected = not self.__board[self.positionToIndex(position)][self.position_indexes.get("piece")].selected
            else:
                self.__board[self.positionToIndex(position)][self.position_indexes.get("place")].selected = not self.__board[self.positionToIndex(position)][self.position_indexes.get("place")].selected
    
    def getBoardByIndexOfPosition(self, index):
        return self.__board[index][self.position_indexes.get("piece")]


   # Returns the vertical and horizontal values as an array
    def positionToArray(position):
        return [position[0], position[1]]

    # Simply returns index of given position, ex: "a1" => 0 or "h8" => 63
    def positionToIndex(self, position):
        return self.board_positions.index(position)

    # Simply returns position of given index, ex: 0 => "a1" or 63 => "h8"
    def indexToPosition(self, index):
        return self.board_positions[index]

    def indexToPosition(index):
        return Board.board_positions[index]