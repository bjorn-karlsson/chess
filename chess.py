
from os import system
from time import sleep 
from board import *

class Chess:

    def __init__(self):
        self.__board = Board()

    def __str__(self):
        return self.__board.__str__()

    def __initGame(self):
        self.__board.initBoard()
        self.player1, self.player2 = [], []

    def __inputHandler(self):
        oldPos = str(input("Input:"))

        if (oldPos == ''):
            self.draw()
            self.__inputHandler()

        if(oldPos == "R"):
            self.__board = Board()
            self.__initGame()

        valid_moves = self.__board.getValidMovesOfPosition(oldPos)
        
        self.__board.toogleSelectedPieces(valid_moves)


        if(not self.__board.validPosition(oldPos)):
            self.draw(2)
            return self.__inputHandler()

        self.__board.toogleSelectedPieces(oldPos)
        self.draw()

        newPos = input("Move To:")
        if(not self.__board.validPosition(newPos, False)):
            self.__board.toogleSelectedPieces(oldPos)
            self.__board.toogleSelectedPieces(valid_moves)
            self.draw(2)
            return self.__inputHandler()
            
        self.draw()
        self.__board.toogleSelectedPieces(oldPos)
        if(len(valid_moves) > 0):
            self.__board.toogleSelectedPieces(valid_moves)
    
        if(not self.__board.movePiecePosition(oldPos, newPos)):
            self.draw(2)
            return self.__inputHandler()
        print("Moving to: " + newPos)

    def start(self):
        self.__initGame()
        self.update()
    
    def update(self):
        self.draw()
        while(True):
            self.__inputHandler()
            self.draw()

    def draw(self, wait = 0):
        sleep(wait)
        system('cls')
        print(self)
        
