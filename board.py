import sys
from termcolor import colored, cprint

from chessPieces import *



class Board:
    
    def __init__(self):
        self.__board = []
        self.board_positions = []
        self.__horizontals = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.__position_indexes = {
            "horizontal":0,
            "vertical":1,
            "place":2,
            "piece":3
        }
    def __str__(self):
        if len(self.__board) != 64:
                return ""
        output = " "
        for place in self.__horizontals:
            output += " " + place 
        output += "\n"




        count = 1
        print() 
        for place in self.__board:
            output += ""
            if(count < 8):
                if(count == 1):
                    if(isinstance(place[self.__position_indexes.get("piece")], chessPiece)):
                        output += place[self.__position_indexes.get("vertical")] + " " + place[self.__position_indexes.get("piece")].displayOnBoard()
                    else:
                        output += place[self.__position_indexes.get("vertical")] + " " + place[self.__position_indexes.get("place")] + " "
                else:
                    if(isinstance(place[self.__position_indexes.get("piece")], chessPiece)):
                        output += place[self.__position_indexes.get("piece")].displayOnBoard()
                    else: 
                        output += place[self.__position_indexes.get("place")] + " "

                count += 1
            else:
                if(isinstance(place[self.__position_indexes.get("piece")], chessPiece)):
                    output += place[self.__position_indexes.get("piece")].displayOnBoard()  + place[self.__position_indexes.get("vertical")] + "\n"
                else:
                    output += place[self.__position_indexes.get("place")] + " " + place[self.__position_indexes.get("vertical")] + "\n"
                count = 1


        output += " "
        for place in self.__horizontals:
            output += " " + place 
        return output     
    def old__str__(self):
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
                    output += place[self.__position_indexes.get("vertical")] + " "
                if(isinstance(place[self.__position_indexes.get("piece")], chessPiece)):
                    output += place[self.__position_indexes.get("piece")].displayOnBoard()
                else:
                    output += place[self.__position_indexes.get("place")] + " "
                
            else:
                
                output += '\n' + place[self.__position_indexes.get("vertical")] + " "
                
                if(isinstance(place[self.__position_indexes.get("piece")], chessPiece)):
                    output += place[self.__position_indexes.get("piece")].displayOnBoard()
                else:
                    output += place[self.__position_indexes.get("place")] + " "
                count = 0

            count += 1


        output += "\n "
        for place in self.__horizontals:
            output += " " + place 
        return output

    def __initBoardPieces(self):
        #Rooks
        self.addPiece('a1', Rook('green')), self.addPiece('a8', Rook('grey').reverse())
        self.addPiece('h1', Rook('green')), self.addPiece('h8', Rook('grey').reverse())
        # Knights
        self.addPiece('b1', Knight('green')), self.addPiece('b8', Knight('grey').reverse())
        self.addPiece('g1', Knight('green')), self.addPiece('g8', Knight('grey').reverse())

        # Bishops
        self.addPiece('c1', Bishop('green')), self.addPiece('c8', Bishop('grey').reverse())
        self.addPiece('f1', Bishop('green')), self.addPiece('f8', Bishop('grey').reverse())

        # Kings and Queens
        self.addPiece('d1', Queen('green')),  self.addPiece('d8', Queen('grey').reverse())
        self.addPiece('e1', King('green')),   self.addPiece('e8', King('grey').reverse())

        # Pawns
        self.addPiece('a2', Pawn('green')), self.addPiece('b2', Pawn('green')), self.addPiece('c2', Pawn('green')), self.addPiece('d2', Pawn('green'))
        self.addPiece('e2', Pawn('green')), self.addPiece('f2', Pawn('green')), self.addPiece('g2', Pawn('green')), self.addPiece('h2', Pawn('green'))
        
        self.addPiece('a7', Pawn('grey').reverse()), self.addPiece('b7', Pawn('grey').reverse()), self.addPiece('c7', Pawn('grey').reverse()), self.addPiece('d7', Pawn('grey').reverse())
        self.addPiece('e7', Pawn('grey').reverse()), self.addPiece('f7', Pawn('grey').reverse()), self.addPiece('g7', Pawn('grey').reverse()), self.addPiece('h7', Pawn('grey').reverse())

    def initBoard(self):
        self.__horizontals
        color_counter = 0

        for v in range(1,9):
            for h in self.__horizontals:
                if color_counter % 2 == 0:
                    self.__board.append([h, str(v), colored("x", 'red'), None])
                    self.board_positions.append(h + str(v))
                else:
                    self.__board.append([h, str(v), colored('+', 'blue'), None])
                    self.board_positions.append(h + str(v))
                color_counter +=1
            if color_counter % 2 != 1:
                color_counter = 1
            else:
                color_counter = 0
            
        self.__initBoardPieces()

    def addPiece(self, position, piece):
        self.__board[self.positionToIndex(position)][self.__position_indexes.get("piece")] = piece      

    def removePieceByPosition(self, position):
        self.__board[self.positionToIndex(position)][self.__position_indexes.get("piece")] = None

    def removePieceByName(self, piece):
        pass

    def validPosition(self, position, piece_on_position = True):
        if(position not in self.board_positions):
            print("Must select a real position")
            return False  

        if(not isinstance(self.__board[self.positionToIndex(position)][self.__position_indexes.get("piece")], chessPiece) and piece_on_position):
            print("Must select a chess piece")
            return False
        return True

    def movePiecePosition(self, current_position, new_position):

        if(current_position == new_position):
            print("cannot move to same location")
            return False

        current_position_index = self.positionToIndex(current_position)
        new_position_index = self.positionToIndex(new_position)

        if(not self.__board[current_position_index][self.__position_indexes.get("piece")].isValidMove(current_position_index, new_position_index, self.__board)):
            print("Cannot move " + self.__board[current_position_index][self.__position_indexes.get("piece")].name + " to: " + new_position)
            return False

            
        self.__board[new_position_index][self.__position_indexes.get("piece")] = self.__board[current_position_index][self.__position_indexes.get("piece")]
        self.__board[new_position_index][self.__position_indexes.get("piece")].first_move = False
        self.__board[current_position_index][self.__position_indexes.get("piece")] = None
            
        return True

    def toogleSelectPiece(self, position):
        
        if(isinstance(self.__board[self.positionToIndex(position)][self.__position_indexes.get("piece")], chessPiece)):
            self.__board[self.positionToIndex(position)][self.__position_indexes.get("piece")].selected = not self.__board[self.positionToIndex(position)][self.__position_indexes.get("piece")].selected
   # Helpers

    def recursive_find(haystack, needle):
        for hay in haystack:
            if(isinstance(hay, list)):
                return Board.recursive_find(hay, needle)
            if(hay == needle):
                return True
        return False

    def positionToArray(self, position):
        return [position[:1], position[1:]]

    def positionToIndex(self, position):
        position = self.positionToArray(position)
        count = 0
        for place in self.__board:
            if(place[0] == position[0] and place[1] == position[1]):
                return count
            count += 1
        
        return False
