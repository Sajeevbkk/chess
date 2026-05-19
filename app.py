import pygame
import sys

class App:
    moving = False
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 800
        App.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Chess")

        self.clock = pygame.time.Clock()
        self.clock.tick(3)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pass
                    # App.moving = True

            App.screen.fill(pygame.Color("white"))

            if App.moving: fps = 60
            else: fps = 3

            self.draw_board()

            pygame.display.flip()
            self.clock.tick(fps)

    def draw_board(self):
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
                                 pygame.Color("black"),
                                 (100*col, 100*row, 100, 100),
                                 line_width)

