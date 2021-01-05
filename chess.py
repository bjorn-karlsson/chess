
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
        self.draw()
        newPos = input("Move To:")
        self.draw()
        self.__movePiece(oldPos, newPos)

    def __movePiece(self, oldPos, newPos):
        self.__board.movePiecePos(oldPos, newPos)

    def start(self):
        self.__initGame()
        self.update()
       # self.__board.movePiecePos('a2', 'a4')
    
    def update(self):
        self.draw()
        while(True):
            self.__inputHandler()
            self.draw(0.5)

    def draw(self, wait = 0):
        sleep(wait)
        system('cls')
        print(self)
        
