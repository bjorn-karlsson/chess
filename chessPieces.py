class chessPiece:

    def __init__(self, symbol = 'X', color = 'C'):
        self.symbol = symbol
        self.color = color
        self.moveCount = 0

    def __str__(self):
        return self.symbol

    def isValidMove(self):
        return True

class King(chessPiece):
    def __init__(self, color):
       super().__init__('K', color)

class Queen(chessPiece):
    def __init__(self, color):
        super().__init__('Q', color)

class Rook(chessPiece):
    def __init__(self, color):
        super().__init__('r', color)

class Bishop(chessPiece):
    def __init__(self, color):
        super().__init__('b', color)

class Knight(chessPiece):
    def __init__(self, color):
        super().__init__('k', color)

class Pawn(chessPiece):
    def __init__(self, color):
        super().__init__('p', color)