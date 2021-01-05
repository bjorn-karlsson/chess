import sys

from chessPieces import *



class Board:
    
    def __init__(self):
        self.__board = []
        self.__horizontals = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    def __str__(self):
        if len(self.__board) != 64:
                return ""
        output = "\n "
        for place in self.__horizontals:
            output += " " + place 
        output += "\n"
        count = 0
        for place in self.__board:
        
            if(count < 8):
                if (count == 0):
                    output += place[1] + " "
                if(isinstance(place[3], chessPiece)):
                    output += place[3].symbol + " "
                else:
                    output += place[2] + " "
                
            else:
                output += '\n' + place[1] + " "
                if(isinstance(place[3], chessPiece)):
                    output += place[3].symbol + " "
                else:
                    output += place[2] + " "
                count = 0
            count += 1
    
        return output

    def __initBoardPieces(self):
        #Rooks
        self.addPiece('a1', Rook('w')), self.addPiece('a8', Rook('b'))
        self.addPiece('h1', Rook('w')), self.addPiece('h8', Rook('b'))
        # Knights
        self.addPiece('b1', Knight('w')), self.addPiece('b8', Knight('b'))
        self.addPiece('g1', Knight('w')), self.addPiece('g8', Knight('b'))

        # Bishops
        self.addPiece('c1', Bishop('w')), self.addPiece('c8', Bishop('b'))
        self.addPiece('f1', Bishop('w')), self.addPiece('f8', Bishop('b'))

        # Kings and Queens
        self.addPiece('d1', Queen('w')),  self.addPiece('d8', Queen('b'))
        self.addPiece('e1', King('w')),   self.addPiece('e8', King('b'))

        # Pawns
        self.addPiece('a2', Pawn('w')), self.addPiece('b2', Pawn('w')), self.addPiece('c2', Pawn('w')), self.addPiece('d2', Pawn('w'))
        self.addPiece('e2', Pawn('w')), self.addPiece('f2', Pawn('w')), self.addPiece('g2', Pawn('w')), self.addPiece('h2', Pawn('w'))
        
        self.addPiece('a7', Pawn('b')), self.addPiece('b7', Pawn('b')), self.addPiece('c7', Pawn('b')), self.addPiece('d7', Pawn('b'))
        self.addPiece('e7', Pawn('b')), self.addPiece('f7', Pawn('b')), self.addPiece('g7', Pawn('b')), self.addPiece('h7', Pawn('b'))

    def initBoard(self):
        self.__horizontals
        color_counter = 0
        for v in range(1,9):
            for h in self.__horizontals:
                if color_counter % 2 == 0:
                    self.__board.append([h, str(v), " ", None])
                else:
                    self.__board.append([h, str(v), '+', None])
                color_counter +=1
            if color_counter % 2 != 1:
                color_counter = 1
            else:
                color_counter = 0
        self.__initBoardPieces()

    def addPiece(self, position, piece):
        self.__board[self.positionToIndex(position)][3] = piece      

    def movePiecePos(self, current_position, new_position):
        if(self.__board[self.positionToIndex(current_position)][3].isValidMove()):
            if(isinstance(self.__board[self.positionToIndex(current_position)][3], chessPiece)):
                self.__board[self.positionToIndex(new_position)][3] = self.__board[self.positionToIndex(current_position)][3]
                self.__board[self.positionToIndex(current_position)][3] = None

    def removePieceByPosition(self, position):
        self.__board[self.positionToIndex(position)][3] = None

    def removePieceByName(self, piece):
        pass

   # Helpers

    def reverseArr(self, array):
        reversed_array = []
        for i in reversed(array):
            reversed_array.append(i)
        return reversed_array

    def positionToArray(self, position):
        return [position[:1], position[1:]]

    def positionToIndex(self, position):
        position = self.positionToArray(position)
        count = 0
        for place in self.__board:
            if(place[0] == position[0] and place[1] == position[1]):
                return count
            count += 1
        
        return None
