from maze import Maze, generate_track
from cell import Cell
from PIL import Image, ImageEnhance

img = Image.new("RGBA", (2000,2000))

maze = generate_track(Maze(16, 9, start_pos=(0, 2)))

def get_img(cell: Cell):
    openings = cell.get_opening()
    if ('down' and 'up') in openings:
        return Image.open('track_imgs/vertical.png')
    elif ('left' and 'right') in openings: 
        return Image.open('track_imgs/horizontal.png')
    elif ('right' and 'down') in openings:
        return Image.open('track_imgs/r2d.png')
    elif ('down' and 'left') in openings:
        return Image.open('track_imgs/d2l.png')
    elif ('left' and 'top') in openings:
        return Image.open('track_imgs/l2t.png')
    elif ('top' and 'right') in openings:
        return Image.open('track_imgs/t2r.png')
    else: 
        print('SJIPPPPPPIIIINNGGG')
        return 'skip'

def get_coordinates(cell: Cell) -> tuple: 
    row_id, col_id = cell.row_id, cell.col_id
    return (row_id*BLOCKSIZE, col_id*BLOCKSIZE)

print('.'*100)
for cell_row in maze.maze:
    for cell in cell_row:
        cell_img = get_img(cell)
        cell_coordinates = get_coordinates(cell)
        if cell_img == 'skip':
            continue
        print('---', cell_img)
        img.paste(cell_img, cell_coordinates)

img.show()