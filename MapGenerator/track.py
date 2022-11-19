import os
import pygame as pyg

from cell import Cell

from typing import Optional, Tuple

BASE_PATH = './track_imgs'
BLOCKSIZE = 146
MOVEX = 10  # 70
MOVEY = 15  # 85
SEED_DICT = {
    'top': '4',
    'bottom': '2',
    'left': '3',
    'right': '1',
    '4': 'top',
    '2': 'bottom',
    '3': 'left',
    '1': 'right'
}

class Track:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        
        self.track = []
        self.initialize_track()

    def initialize_track(self):
        """ Creates an empty matrix of cell objects with all their walls intact """

        for c in range(self.cols):
            row = [Cell(row_idx=r, col_idx=c) for r in range(self.rows)]
            self.track.append(row)

    def get_cell_at(self, row_idx: int, col_idx: int) -> Cell:
        """ Returns a cell at the given location """

        return self.track[col_idx][row_idx]

    def print_track(self):
        """ Prints each row of the track, and ending the entire print with an `enter` """

        for c in range(self.cols):
            print(self.track[c])
        print()

    def generate_track_from_seed(self, seed):
        """ Given a seed - or a precomputed path - this function decides which walls should be knocked down.
            The function just changes the cells in the preexisting track matrix """

        start_pos = list(map(int, (seed[0], seed[2])))

        # Place start_pos at `self.track`
        self.track[start_pos[0]][start_pos[1]].start = True

        current_pos = start_pos
        for cell_id in seed.split('-')[-1]:
            current_cell = self.get_cell_at(current_pos[0], current_pos[1])
            match cell_id:
                case '1': # (right)
                    current_pos[0] += 1
                case '2': # (down)
                    current_pos[1] += 1 
                case '3': # (left)
                    current_pos[0] -= 1 
                case '4': # (up)
                    current_pos[1] -= 1 
            neighbour_cell = self.get_cell_at(current_pos[0], current_pos[1])

            current_cell.knock_down_wall(neighbour_cell)            

    def download_image(self):
        raise NotImplementedError('This function has not been implemented yet')

        def get_coordinates(cell: Cell):
            return (cell.row_idx*BLOCKSIZE, cell.col_idx*BLOCKSIZE)            

        def get_image_block(cell: Cell):
            openings = cell.get_opening()
            if len(openings) == 0:
                return 'skip'

            openings = sorted(openings)
            image_name = '_to_'.join(openings)
            filepath = os.path.join(BASE_PATH, image_name)

            return pyg.image.load(filepath)
