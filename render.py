import pygame
import sys

def render(app_inst, App):
    while True:
        event_handler(pygame.event.get())

        App.screen.fill(pygame.Color("white"))

        if App.moving:
            fps = 60
        else:
            fps = 3

        app_inst.draw_board()
        app_inst.pieces.update()
        app_inst.pieces.draw(App.screen)

        pygame.display.flip()
        app_inst.clock.tick(fps)

def event_handler(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pass
