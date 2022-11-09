import grid

class Maze:
    def __init__(self, rows, cols, start_pos=(0, 0)) -> None:
        self.rows = rows
        self.cols = cols
        if start_pos:
            self.start_pos = start_pos
        self.arr = []

    def generate_maze(self) -> None:
        for i in range(self.rows):
            col = []
            for j in range(self.cols):
                cell = grid.Grid(row_id=i, col_id=j)
                if self.start_pos == (i, j): cell.start = True
                col.append(cell)
            self.arr.append(col)

# maze = Maze(10, 5)
# maze.generate_maze()
# cell = maze.arr[3][4]
# cell.knock_down_wall(maze.arr[4][4])
# print(cell.row_id, cell.col_id, cell.walls)


#Vælg en start celle
#Find naboer, og vælg en tilfældig, fortsæt med dette indtil ingen naboer kan findes.
#Findes ingen naboer, tjekkes for positionen af slut gridet, er dette ved siden af start, er banen godkendt.
#Ellers gå et træk tilbage, og se om det kan ændres, kan det ikke det, gå et til tilbage osv, indtil en løsning er fundet
#Den er slet ikke optimeret....