
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

    def __inputHandler(self):
        oldPos = input("Move From:")
        if(not self.__board.validatePosition(oldPos)):
            self.draw(2)
            self.__inputHandler()

        self.__board.toogleSelectPiece(oldPos)
        self.draw()

        newPos = input("Move To:")
        if(not self.__board.validatePosition(newPos, False)):
            self.__board.toogleSelectPiece(oldPos)
            self.draw(2)
            self.__inputHandler()
            
        self.draw()
        self.__board.toogleSelectPiece(oldPos)
        if(not self.__movePiece(oldPos, newPos)):
            self.draw(2)
            self.__inputHandler()
        print("Moving to: " + newPos)

    def __movePiece(self, oldPos, newPos):
        return self.__board.movePiecePos(oldPos, newPos)

    def start(self):
        self.__initGame()
        self.update()
       # self.__board.movePiecePos('a2', 'a4')
    
    def update(self):
        self.draw()
        while(True):
            self.__inputHandler()
            self.draw(1)

    def draw(self, wait = 0):
        sleep(wait)
        system('cls')
        print(self)
        