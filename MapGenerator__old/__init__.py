import sys
sys.path.append('./MapGenerator')
sys.setrecursionlimit(10**6)

import pygame as pyg

from cell import Cell
from maze import Maze, generate_track


BLOCKSIZE = 146
vertical = pyg.image.load("./track_imgs/vertical.png")
horizontal = pyg.image.load("./track_imgs/horizontal.png")
right_to_down = pyg.image.load("./track_imgs/r2d.png")
down_to_left = pyg.image.load("./track_imgs/d2l.png")
left_to_top = pyg.image.load("./track_imgs/l2t.png")
top_to_right = pyg.image.load("./track_imgs/t2r.png")

movex = 10  # 70
movey = 15  # 85


def generate_image(maze: Maze, screen):
    for cell_row in maze:
        for cell in cell_row:
            cell_img = get_img(cell)
            if cell_img == 'skip':
                continue
            cell_coordinates = get_coordinates(cell)
            cell_img_rect = cell_img.get_rect()
            screen.blit(cell_img, cell_img_rect.move(
                cell_coordinates[0]+movex, cell_coordinates[1]+movey))


def get_img(cell: Cell):
    openings = cell.get_opening()
    if 'down' in openings and 'top' in openings:
        return vertical
    elif 'left' in openings and 'right' in openings:
        return horizontal
    elif 'right' in openings and 'down' in openings:
        return right_to_down
    elif 'down' in openings and 'left' in openings:
        return down_to_left
    elif 'left' in openings and 'top' in openings:
        return left_to_top
    elif 'top' in openings and 'right' in openings:
        return top_to_right
    elif openings.__len__() == 0:
        return "skip"



def get_coordinates(cell: Cell) -> tuple:
    row_id, col_id = cell.row_id, cell.col_id
    return (row_id*BLOCKSIZE, col_id*BLOCKSIZE)


def main(fileName=None, rows=13, cols=7, start_pos=(0, 2), track_length=40, SCREEN_WIDTH=1920, SCREEN_HEIGHT=1080, BLOCKSIZE=146):
    if track_length > 70:
        raise ValueError("Track Length is too long!")
    pyg.init()

    SCREEN = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    grids = Maze(rows=rows, cols=cols, start_pos=start_pos)
    grids.generate_maze()
    track = generate_track(arr=grids, min_len=track_length)
    print(track.seed)
    generate_image(track.maze, SCREEN)
    if fileName:
        pyg.image.save(SCREEN, fileName)
    track.print_maze()

    return SCREEN

main('new_image2.png')