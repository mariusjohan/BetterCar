import numpy as np
from cell import Cell
import random
import copy


class Maze:
    def __init__(self, rows, cols, start_pos=(0, 0)) -> None:
        self.rows = rows
        self.cols = cols
        if start_pos:
            self.start_pos = start_pos
        self.maze = []

    def generate_maze(self) -> None:
        for i in range(self.rows):
            col = []
            for j in range(self.cols):
                cell_obj = Cell(row_id=i, col_id=j)
                if self.start_pos == (i, j): 
                    cell_obj.start = True
                col.append(cell_obj)
            self.maze.append(col)
    
    def print_maze(self) -> np.ndarray:
        img_array = np.zeros((len(self.maze), len(self.maze[0])))

        for counter, i in enumerate(self.maze):
            for j_counter, j in enumerate(i):
                #if j.has_openings():
                    #img_array[counter][j_counter] = 1
                #if j.start:
                    #img_array[counter][j_counter] = 2
                if j.index:
                    img_array[counter][j_counter] = j.index
            print(img_array[counter].tolist())

        return img_array

    def get_neighbours(self, cell: Cell, visited=False) -> list:  
        neighbours = []
        test_cell = None
        for i in range(4):
            if i == 0: test_cell = [cell.row_id, cell.col_id+1] # op
            elif i == 1: test_cell = [cell.row_id+1, cell.col_id] # høre
            elif i == 2:
                if cell.row_id > 0:
                    test_cell = [cell.row_id-1, cell.col_id] # venstre
            elif i == 3:
                if cell.col_id > 0:
                    test_cell = [cell.row_id, cell.col_id-1] # ned

            try:
                if visited:
                    if not self.maze[test_cell[0]][test_cell[1]].visited:
                        neighbours.append(self.maze[test_cell[0]][test_cell[1]]) 
                else:
                    neighbours.append(self.maze[test_cell[0]][test_cell[1]])
            except: 
                pass

        return neighbours

def generate_track(arr: Maze, min_len=30) -> None:
    "The track is generated with the first visited cell being one above the start cell!!!"
    maze = copy.deepcopy(arr)
    start_cell = maze.maze[maze.start_pos[0]][maze.start_pos[1]]
    visited_cells = []
    track_length = 0
    goal_cells = maze.get_neighbours(start_cell)
    start_cell.knock_down_wall(maze.maze[start_cell.row_id][start_cell.col_id-1])
    start_cell.index = 1
    current_cell = maze.maze[start_cell.row_id][start_cell.col_id-1]
    visited_cells.append(start_cell)
    visited_cells.append(current_cell)
    while True:
        if current_cell == start_cell:
            if track_length < min_len: return generate_track(arr)
            [print("VVVVV", cell.walls) for cell in visited_cells]
            return maze
        possible_neighbours = maze.get_neighbours(current_cell, visited=True)
        if not possible_neighbours:
            return generate_track(arr)
        #Chose cell to go to.
        neighbour_cell = random.choice(possible_neighbours)
        current_cell.knock_down_wall(neighbour_cell)
        current_cell.index = track_length+2
        visited_cells.append(current_cell)
        track_length += 1
        current_cell = neighbour_cell
    

if __name__ == '__main__':
    maze = Maze(16, 9, start_pos=(0, 2))
    maze.generate_maze()
    test = generate_track(arr=maze)
    pm = test.print_maze()


# cell = maze.maze[3][4]
# cell.knock_down_wall(maze.maze[4][4])
# print(cell.row_id, cell.col_id, cell.walls)


#Vælg en start celle
#Find naboer, og vælg en tilfældig, fortsæt med dette indtil ingen naboer kan findes.
#Findes ingen naboer, tjekkes for positionen af slut gridet, er dette ved siden af start, er banen godkendt.
#Ellers gå et træk tilbage, og se om det kan ændres, kan det ikke det, gå et til tilbage osv, indtil en løsning er fundet
#Den er slet ikke optimeret....