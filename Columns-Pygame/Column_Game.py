import pygame
from Settings import Settings
import Game_Logic as GL
from Column_Group import ColumnGroup

def run_game():
    clock = pygame.time.Clock()
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Columns by Cam")

    global column
    column = ColumnGroup(settings, screen)
    counter = 0
    global new_column
    new_column = False
    while True:
        print(counter)
        clock.tick(30)
        GL.check_events(column)
        if counter == 30:
            counter = 0
            new_column = GL.drop(column)
        GL.update_board(column)
        GL.update_screen(settings, screen)
        pygame.display.update()
        counter += 1
        if new_column:
            new_column = False
            column = ColumnGroup(settings, screen)
        GL.continue_play(settings, screen)
run_game()












