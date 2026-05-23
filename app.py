import pygame
from render import render
import characters
import setup

class App:
    moving = False
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 800
        App.screen = pygame.display.set_mode((self.width, self.height))
        App.font = pygame.font.SysFont("comicsans", 16)
        pygame.display.set_caption("Chess")
        App.pieces_on_board = {
        characters.King(
            1, setup.black_pieces_files[0]
        ): [4, 0],
        characters.King(
            0, setup.white_pieces_files[0]
        ): [4, 7],
        characters.Queen(
            1, setup.black_pieces_files[1]
        ): [3, 0],
        characters.Queen(
            0, setup.white_pieces_files[1]
        ): [3, 7],
    }
        setup.add_pieces(App.pieces_on_board)
        self.pieces = pygame.sprite.Group()
        self.pieces.add(setup.create_pieces(App.pieces_on_board))

        self.clock = pygame.time.Clock()
        self.clock.tick(3)

        # function to run the program
        self.run = render(self, App)

    @staticmethod
    def draw_board():
        for row in range(8):
            for col in range(8):
                line_width = 2
                if row % 2 == 0:
                    if col % 2 != 0:
                        line_width = 0
                else:
                    if col % 2 == 0:
                        line_width = 0
                pygame.draw.rect(App.screen,
                                 pygame.Color("gray"),
                                 (100*col, 100*row, 100, 100),
                                 line_width)
                text = App.font.render(f"({col}, {row})", True, "blue")
                App.screen.blit(text, (100*col, 100*row))

