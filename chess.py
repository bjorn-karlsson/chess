
from os import system
from time import sleep 
import random

from board import *

class Player:

    def __init__(self, name, number, color):
        self.name = name
        self.side = number
        self.color = color
        self.check_mate = False
        self.turn = False


class Chess:

    ERROR_MESSAGE_TIME = 1.5
    ERROR_MESSAGE_POSITION = "is an invalid location"
    ERROR_MESSAGE_MOVING = "unable to move to :"

    

    def __init__(self):
        self.__first_player = Player("Bob", 1, "green")
        self.__second_player = Player("Bot", 2, "yellow")
        self.__board = Board(self.__first_player.color, self.__second_player.color)

    def __str__(self):
        return self.__board.__str__()

    def restart(self):
        self.__board = Board(self.__first_player.color, self.__second_player.color)
        self.__initGame()    

    def __initGame(self):
        self.__board.initBoard()
        self.player1, self.player2 = [], []

    def __getInput(self, input_text = ":", print_before = False):
        if(print_before):
            print(print_before)
        result = str(input(input_text))
        return result

    def __validInput(self, input):
        if(input == ''):
            return False
        else:
            return True

    def __checkInput(self, input):
        if(not self.__validInput(input)):
            return False
        if(input == "R"):
            self.restart()
        return True

    def __toggleSelectedPositions(self, positions, draw_before = False, draw_after = False):

        if(not isinstance(positions, list)):
            positions = [positions]

        if(draw_before):
            self.draw()
        for position in positions:
            self.__board.toogleSelectedPieces(position)
        if(draw_after):
            self.draw()

    def __displayErrorMessage(self, message, seconds = ERROR_MESSAGE_TIME):
        print(message)
        self.draw(seconds)

    def __gameInputHandler(self):
        move_from = self.__getInput("Move from: ")
        if(not self.__checkInput(move_from)):
            return False

        if(not self.__board.validPosition(move_from)):
            self.__displayErrorMessage(f"[{move_from}] " + Chess.ERROR_MESSAGE_POSITION)
            return self.__gameInputHandler()

        valid_moves = self.__board.getValidMovesOfPosition(move_from)
        self.__toggleSelectedPositions([valid_moves, move_from], False, True)


        move_to = input("Move to:")
        if(not self.__board.validPosition(move_to, False)):
            self.__toggleSelectedPositions([valid_moves, move_from], False, True)
            self.__displayErrorMessage(f"[{move_to}] " + Chess.ERROR_MESSAGE_POSITION)
            return self.__gameInputHandler()
            

        if(len(valid_moves) > 0):
            self.__toggleSelectedPositions([valid_moves, move_from],  False, True)
    
        if(not self.__board.movePiecePosition(move_from, move_to)):
            self.__displayErrorMessage(Chess.ERROR_MESSAGE_MOVING + f" [{move_to}] ")
            return self.__gameInputHandler()

        #print("Moving to: " + move_to)

    def start(self):
        self.__initGame()
        self.update()

    def beginTurn(self):
        return self.____first_player

    def switchTurn(self, player):
        if(self.__first_player == player):
            player = self.__second_player
        else:
            player = self.__first_player

        return player


    def update(self):
        player = self.beginTurn()
        self.draw()
        while(not self.__first_player.check_mate and not self.__second_player.check_mate):
            input = self.__gameInputHandler()
            if(self.__board.isMate()):
                if(self.__board.isCheckMate()):
                    pass

            player = self.switchTurn(player)
            self.draw()

    def draw(self, wait = 0):
        sleep(wait)
        system('cls')
        print(self)
        
