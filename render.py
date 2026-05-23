import pygame
import sys

def render(app_inst, App):
    while True:
        event_handler(pygame.event.get(), app_inst, App)

        App.screen.fill(pygame.Color("white"))

        if App.moving:
            fps = 60
        else:
            fps = 10

        App.draw_board()
        # app_inst.pieces.update()
        app_inst.pieces.draw(App.screen)

        pygame.display.flip()
        app_inst.clock.tick(fps)

def event_handler(events, app, App):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            collided_piece = check_collision(app.pieces)
            if collided_piece:
                App.moving = True
                App.locked = collided_piece
        if event.type == pygame.MOUSEBUTTONUP and App.moving:
            App.moving = False
            x = App.locked.rect.centerx // App.locked.horizontal_multiplier
            y = App.locked.rect.centery//App.locked.vertical_multiplier
            if App.locked.check_valid_move(x, y, app.pieces) and 0 <= x < 8 and 0 <= y < 8:
                App.locked.x = App.locked.rect.centerx//App.locked.horizontal_multiplier
                App.locked.y = App.locked.rect.centery//App.locked.vertical_multiplier
            App.locked.rect.left = App.locked.x * App.locked.horizontal_multiplier
            App.locked.rect.top = App.locked.y * App.locked.vertical_multiplier
            App.locked = None
        if event.type == pygame.MOUSEMOTION and App.moving:
            App.locked.rect.move_ip(event.rel)

def check_collision(pieces):
    for piece in pieces:
        if piece.rect.collidepoint(pygame.mouse.get_pos()):
            return piece
    return False
