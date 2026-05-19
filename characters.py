import pygame

class Piece(pygame.sprite.Sprite):
    # color: 0: white, 1: black
    def __init__(self, color, file):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.image = pygame.transform.scale2x(
            pygame.image.load(file).convert_alpha()
        )
        self.rect = self.image.get_rect()
        self.horizontal_multiplier = 100
        self.vertical_multiplier = 100

class King(Piece):
    def __init__(self, color, file):
        Piece.__init__(self, color, file)
        self.horizontal_multiplier = 101

class Queen(Piece):
    def __init__(self, color, file):
        Piece.__init__(self, color, file)
        self.horizontal_multiplier = 102

class Bishop(Piece):
    def __init__(self, color, file):
        Piece.__init__(self, color, file)

class Knight(Piece):
    def __init__(self, color, file):
        Piece.__init__(self, color, file)

class Rook(Piece):
    def __init__(self, color, file):
        Piece.__init__(self, color, file)

class Pawn(Piece):
    def __init__(self, color, file):
        Piece.__init__(self, color, file)
        self.horizontal_multiplier = 100
        self.vertical_multiplier = 100