import pygame

class Piece(pygame.sprite.Sprite):
    # color=> 0: white, 1: black
    def __init__(self, color, file):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.image = pygame.transform.scale(
            pygame.image.load(file).convert_alpha(),
            (100, 100)
        )
        self.rect = self.image.get_rect()
        self.horizontal_multiplier = 100
        self.vertical_multiplier = 100
        self.x = None
        self.y = None

    def check_valid_move(self, x, y, group):
        return True

    def check_collision(self, x, y, group):
        for member in group:
            if self != member and member.x == x and member.y == y:
                return False
        return True

class King(Piece):
    def __init__(self, color, file):
        Piece.__init__(self, color, file)

    def check_valid_move(self, x, y, group):
        if abs(self.x - x) <= 1 and abs(self.y - y) <= 1:
            return self.check_collision(x, y, group)
        return False

class Queen(Piece):
    def __init__(self, color, file):
        Piece.__init__(self, color, file)

    def check_valid_move(self, x, y, group):
        if abs(self.x - x) == abs(self.y - y) or \
                (self.x == x and 0 <= y < 8) or (self.y == y and 0 <= x < 8):
            return self.check_collision(x, y, group)
        return False

class Bishop(Piece):
    def __init__(self, color, file):
        Piece.__init__(self, color, file)

    def check_valid_move(self, x, y, group):
        if abs(self.x - x) == abs(self.y - y):
            return self.check_collision(x, y, group)
        return False

class Knight(Piece):
    def __init__(self, color, file):
        Piece.__init__(self, color, file)

class Rook(Piece):
    def __init__(self, color, file):
        Piece.__init__(self, color, file)

    def check_valid_move(self, x, y, group):
        if self.y == y:
            a, b = (self.x, x) if self.x > x else (x, self.x)
            axis = 0 # 0 denotes x
        elif self.x == x:
            a, b = (self.y, y) if self.y > y else (y, self.y)
            axis = 1 # 1 denotes y
        else: return False
        between = False
        for member in group:
            if self != member:
                if axis == 0 and member.y == self.y:
                    c = a-member.x
                elif axis == 1 and member.x == self.x:
                    c = a-member.y
                else: continue
                if a-b > c:
                    between = True
        if not between: return self.check_collision(x, y, group)
        return False

class Pawn(Piece):
    def __init__(self, color, file):
        Piece.__init__(self, color, file)
        self.horizontal_multiplier = 100
        self.vertical_multiplier = 100