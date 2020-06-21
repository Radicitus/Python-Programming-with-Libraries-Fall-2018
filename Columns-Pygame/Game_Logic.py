import pygame, time

from Column_Group import ColumnGroup
global board
board = [[0 for i in range(6)] for i in range(12)]

def game_over(settings, screen):
    global board
    for row in board:
        row.clear()
    board = [[0 for i in range(6)] for i in range(12)]
    screen.fill((255, 255, 255))
    pygame.display.flip()
    time.sleep(2)
    update_screen(settings, screen)

def continue_play(settings, screen):
    counter = 0
    print(board)
    for col in range(6):
        for row in range(4):
            if board[row][col] != 0:
                counter += 1
        if counter == 4:
            game_over(settings, screen)
        else:
            counter = 0

def check_events(ColumnGroup):
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                check_keydown_events(event, ColumnGroup)
            if event.type == pygame.KEYUP:
                check_keyup_events(event, ColumnGroup)


def update_boxes(ColumnGroup):
    for box in ColumnGroup.boxes:
        row = box.get_position()[0]
        col = box.get_position()[1]
        board[row][col] = box

def drop(ColumnGroup):
    if not check_valid_move_down(ColumnGroup):
        update_boxes(ColumnGroup)
        return True
    else:
        ColumnGroup.update(True)
        last_pos = ColumnGroup.get_all_position()[2]
        pos_to_remove_Y = last_pos[0] - 1
        pos_to_remove_X = last_pos[1]
        board[pos_to_remove_Y][pos_to_remove_X] = 0

def update_board(ColumnGroup):
    if ColumnGroup.is_left():
        if check_valid_move_left(ColumnGroup):
            position = ColumnGroup.get_all_position()
            for pos in position:
                board[pos[0]][pos[1]] = 0
            ColumnGroup.update()

    if ColumnGroup.is_right():
        if check_valid_move_right(ColumnGroup):
            position = ColumnGroup.get_all_position()
            for pos in position:
                board[pos[0]][pos[1]] = 0
            ColumnGroup.update()

    for box in ColumnGroup.to_add():
        try:
            board[box.get_position()[0]][box.get_position()[1]] = box
        except:
            pass
    print(board)


def check_keydown_events(event, ColumnGroup):
    if event.key == pygame.K_q:
        pygame.quit()
        quit()
    if event.key == pygame.K_RIGHT:
        ColumnGroup.change_right()
    elif event.key == pygame.K_LEFT:
        ColumnGroup.change_left()
    elif event.key == pygame.K_SPACE:
        ColumnGroup.rotate()


def check_keyup_events(event, ColumnGroup):
    if event.key == pygame.K_RIGHT:
        ColumnGroup.change_right()
    elif event.key == pygame.K_LEFT:
        ColumnGroup.change_left()


def check_valid_move_right(ColumnGroup):
    row = ColumnGroup.get_position()[0]
    col = ColumnGroup.get_position()[1]
    try:
        if board[row][col + 1] == 0 and col < 5:
            return True
    except:
        return False


def check_valid_move_left(ColumnGroup):
    row = ColumnGroup.get_position()[0]
    col = ColumnGroup.get_position()[1]
    try:
        if board[row][col - 1] == 0 and col > 0:
            return True
    except:
        return False


def check_valid_move_down(ColumnGroup):
    row = ColumnGroup.get_position()[0]
    col = ColumnGroup.get_position()[1]
    try:
        if board[row + 1][col] == 0:
            return True
    except:
        return False


def update_screen(settings, screen):
    screen.fill(settings.bg_color)
    for row in board:
        for col in row:
            if col == 0:
                continue
            else:
                col.blitme()





