import pygame as pyg
from cell import Cell
from maze import Maze, generate_track

SCALE = 1
WIDTH = 16
HEIGHT = 9
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
BLOCKSIZE = SCREEN_WIDTH/WIDTH # 120

pyg.init()
SCREEN = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
vertical      = pyg.image.load("track_imgs/vertical.png")
horizontal    = pyg.image.load("track_imgs/horizontal.png")
right_to_down = pyg.image.load("track_imgs/r2d.png")
down_to_left  = pyg.image.load("track_imgs/d2l.png")
left_to_top   = pyg.image.load("track_imgs/l2t.png")
top_to_right  = pyg.image.load("track_imgs/t2r.png")

def generate_image(maze: Maze):
    for cell_row in maze:
        for cell in cell_row: 
            cell_img = get_img(cell)
            if cell_img == 'skip':
                continue
            cell_coordinates = get_coordinates(cell)
            cell_img_rect = cell_img.get_rect()
            SCREEN.blit(cell_img, cell_img_rect.move(*cell_coordinates))

def get_img(cell: Cell):
    openings = cell.get_opening()
    print(f"WALLS: {cell.walls}")
    print(f"openings: {openings}")
    if ('down' and 'up') in openings:
        return vertical
    elif ('left' and 'right') in openings: 
        return horizontal
    elif ('right' and 'down') in openings:
        return right_to_down
    elif ('down' and 'left') in openings:
        return down_to_left
    elif ('left' and 'top') in openings:
        return left_to_top
    elif ('top' and 'right') in openings:
        return top_to_right
    else:
        return 'skip'

def get_coordinates(cell: Cell) -> tuple: 
    row_id, col_id = cell.row_id, cell.col_id
    return (row_id*BLOCKSIZE, col_id*BLOCKSIZE)


if __name__ == "__main__":
    grids = Maze(rows=16, cols=9, start_pos=(0, 2))
    grids.generate_maze()
    track = generate_track(arr = grids)
    generate_image(track.maze)
    #SCREEN.blit(right_to_down, (0, 0))
    pyg.image.save(SCREEN, "tracks/test.png")
    track.print_maze()