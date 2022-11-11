import copy
import random

import numpy as np
from cell import Cell


class Maze:
    def __init__(self, rows, cols, start_pos=(0, 0)) -> None:
        self.rows = rows
        self.cols = cols
        if start_pos:
            self.start_pos = start_pos
        self.maze = []

        self.seed = ""

    def generate_maze(self) -> None:
        """ Generates a matrix with cells, but there's no "path" for the car """
        for i in range(self.rows):
            col = []
            for j in range(self.cols):
                cell_obj = Cell(row_id=i, col_id=j)
                if self.start_pos == (i, j):
                    cell_obj.start = True
                col.append(cell_obj)
            self.maze.append(col)

    def print_maze(self) -> np.ndarray:
        """
        Prints the maze, with the each line consisting of a row (y axis), with the first index being on the top of the screen going downwards.
        Mainly used for debugging
        """
        img_array = np.zeros((len(self.maze), len(self.maze[0])))

        for x_counter, x_axis in enumerate(self.maze):
            for y_counter, cell in enumerate(x_axis):
                if cell.index:
                    img_array[x_counter][y_counter] = cell.index

        return img_array

    def get_neighbours(self, cell: Cell, visited=False) -> list:
        "Return a list of neighbouring cells to a given cell from the matrix"
        neighbours = []
        test_cell = None
        for i in range(4):
            if i == 0:
                test_cell = [cell.row_id, cell.col_id+1]  # op
            elif i == 1:
                test_cell = [cell.row_id+1, cell.col_id]  # høre
            elif i == 2:
                if cell.row_id > 0:
                    test_cell = [cell.row_id-1, cell.col_id]  # venstre
            elif i == 3:
                if cell.col_id > 0:
                    test_cell = [cell.row_id, cell.col_id-1]  # ned

            try:
                if visited:
                    if not self.maze[test_cell[0]][test_cell[1]].visited:
                        neighbours.append(
                            self.maze[test_cell[0]][test_cell[1]])
                else:
                    neighbours.append(self.maze[test_cell[0]][test_cell[1]])
            except:
                pass

        return neighbours


def generate_track(arr: Maze, min_len=30) -> None:
    "The track is generated with the first visited cell being one above the start cell!!!"
    maze = copy.deepcopy(arr)
    visited_cells = []
    track_length = 0
    test_dict = {"right": '1', "left": '3', 'top': '4', 'down': '2'}
    # Get the start cell
    start_cell = maze.maze[maze.start_pos[0]][maze.start_pos[1]]
    start_cell.index = 1
    start_cell.knock_down_wall(
        maze.maze[start_cell.row_id][start_cell.col_id-1])
    maze.seed += f"{start_cell.row_id}-{start_cell.col_id}-"
    maze.seed += f"{test_dict['top']}"

    current_cell = maze.maze[start_cell.row_id][start_cell.col_id-1]
    visited_cells.append(start_cell)
    visited_cells.append(current_cell)

    while True:
        
        if current_cell == start_cell:  # Are we back at the start?
            if track_length < min_len:
                return generate_track(arr, min_len)
            return maze

        possible_neighbours = maze.get_neighbours(current_cell, visited=True)
        if not possible_neighbours:  # No possible neighbours, retry
            return generate_track(arr, min_len)

        # Chose cell to go to.
        neighbour_cell = random.choice(possible_neighbours)
        track_length += 1
        # Knock down neighbour wall
        current_cell.knock_down_wall(neighbour_cell)
        wall_to_add = current_cell.get_wall_between(neighbour_cell)
        maze.seed += f"{test_dict[wall_to_add[0]]}"
        current_cell.index = track_length+1
        visited_cells.append(current_cell)

        # Continue as next cell
        current_cell = neighbour_cell


if __name__ == '__main__':
    maze = Maze(16, 9, start_pos=(0, 2))
    maze.generate_maze()
    test = generate_track(arr=maze, min_len=50)
    pm = test.print_maze()
