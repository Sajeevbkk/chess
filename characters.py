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
            stepx = 1 if x - self.x > 0 else -1
            stepy = 1 if y - self.y > 0 else -1
            position_btwn = [(self.x + i * stepx, self.y + i * stepy) for i in range(abs(self.x - x))]
            for member in group:
                if member != self and (member.x, member.y) in position_btwn:
                    return False
            return self.check_collision(x, y, group)
        return False

class Knight(Piece):
    def __init__(self, color, file):
        Piece.__init__(self, color, file)

class Rook(Piece):
    def __init__(self, color, file):
        Piece.__init__(self, color, file)

    def check_valid_move(self, x, y, group):
        if self.x == x:
            old = self.y
            new = y
            check = 'y'
        elif self.y == y:
            old = self.x
            new = x
            check = 'x'
        else: return False
        for member in group:
            if self != member and getattr(member,
                                          'x' if check == 'y' else 'y'
                                          ) == getattr(
                self, 'x' if check == 'y' else 'y'
            ):
                if old > new:
                    if old > getattr(member, check) > new:
                        return False
                if old < new:
                    if old < getattr(member, check) < new:
                        return False
        return self.check_collision(x, y, group)

class Pawn(Piece):
    def __init__(self, color, file):
        Piece.__init__(self, color, file)
        self.horizontal_multiplier = 100
        self.vertical_multiplier = 100