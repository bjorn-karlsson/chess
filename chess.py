from os import system
from time import sleep 
import random

from board import *

class Player:

    def __init__(self, name, team, color):
        self.name = name
        self.team = team
        self.color = color
        self.check_mate = False
        self.mate = False
        self.turn = False
        self.piece_positions = []
        


class Chess:

    ERROR_MESSAGE_TIME = 1.5
    ERROR_MESSAGE_POSITION = "is an invalid location"
    ERROR_MESSAGE_MOVING = "unable to move to :"

    CONTINUTE_MESSAGE = "Press enter to continue..."

    EXIT_CODE_NORMAL = 1

    

    def __init__(self):
        self.__first_player = Player("Bob", 1, "green")
        self.__second_player = Player("Bot", 2, "yellow")
        self.current_player = None
        self.waiting_player = None
        self.__board = Board(self.__first_player.color, self.__second_player.color)
        self.board_history = []

    def __str__(self):
        return self.__board.__str__()

    def restart(self):
        self.__init__()
        self.start() 

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
        input = input.lower()
        if(input in ["r", "restart", "reload"]):
            self.restart()
        if(input in ["q", "quit", "exit"]):
            exit()
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

        self.updatePlayerPiecePositions(self.current_player)

        self.__toggleSelectedPositions(self.current_player.piece_positions, False, True)

        move_from = self.__getInput("Move from: ")
        
        self.__toggleSelectedPositions(self.current_player.piece_positions, False, True)

        if(not self.__checkInput(move_from)):
            return self.__gameInputHandler()

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
        self.draw()
        self.updatePlayerPiecePositions(self.current_player)
        self.updatePlayerPiecePositions(self.waiting_player)
        #print("Moving to: " + move_to)

    def start(self):
        self.__initGame()
        self.update()

    def updatePlayerPiecePositions(self, players):
        if(not isinstance(players, list)):
            players = [players]

        for player in players:
            player.piece_positions = self.__board.getPositionsByPieces(self.__board.getPieces(player.team))

        return True

    def beginTurn(self):
        self.updatePlayerPiecePositions([self.__first_player, self.__second_player])
        self.current_player = self.__first_player
        self.waiting_player = self.__second_player
        return self.__first_player

    def switchTurn(self):

        if(self.__first_player == self.current_player):
            self.current_player = self.__second_player
            self.waiting_player = self.__first_player
        else:
            self.current_player = self.__first_player
            self.waiting_player = self.__second_player
    
        return self.current_player

    def checkForMateAndCheckMate(self, player1, player2):
        if(self.__board.isMate(player1.piece_positions, self.__board.getKingPosition(player2.team))):
            if(player2.mate):
                self.draw()
                print(colored("Check Mate... ", "red") + colored(f"Player{player2.team}", player2.color) + colored(" lost the game...", "red"))
                input(Chess.CONTINUTE_MESSAGE)
                player2.check_mate = True
                return player2
            if(self.__board.isCheckMate(player1.piece_positions, player2.piece_positions, self.__board.getKingPosition(player2.team))):
                self.draw()
                print(colored("Check Mate... ", "red") + colored(f"Player{player2.team}", player2.color) + colored(" lost the game...", "red"))
                input(Chess.CONTINUTE_MESSAGE)
                player2.check_mate = True
                return player2
            else:
                player2.mate = True
                self.draw()
                print(colored("Mate!", player2.color))
                input(Chess.CONTINUTE_MESSAGE)
        else:
            player2.mate = False

    def checkForPromotion(self, player):
        result = self.__board.promotionAvailable(player.team)

        if(result):
            print(f"player{player.team}'s Pawn on {result[0]} got promoted")
            self.draw(2.5)
            if(player.team == 1):
                self.__board.addPiece(result[0], Queen(self.__board.player_color1))
            elif(player.team == 2):
                self.__board.addPiece(result[0], Queen(self.__board.player_color2).reverse())
            return result
        return False
    
    def update(self):
        self.beginTurn()
        self.board_history.append(deepcopy(self.__board))
        self.draw()
        while(not self.__first_player.check_mate and not self.__second_player.check_mate):
            
            self.__gameInputHandler()

            ## CHECK FOR PAWN PROMOTIONS
            self.checkForPromotion(self.current_player)
            #self.checkForPromotion(self.waiting_player)

            ## CHECK IF GAME IS OVER or JUST MATE
            self.checkForMateAndCheckMate(self.current_player, self.waiting_player)
            self.checkForMateAndCheckMate(self.waiting_player, self.current_player)
            
            self.board_history.append(deepcopy(self.__board))
            self.switchTurn()
            self.draw()

        for board in self.board_history:
            input()
            self.clear()
            print(board)
        self.restart()

    def draw(self, wait = 0):
        self.clear(wait)
        print(self)
    
    def clear(self, wait = 0):
        sleep(wait)
        system('cls')
