class Cell:
    """TESTESTEST"""
    def __init__(self, row_id, col_id, total_row=16, total_col=9) -> None:
        self.row_id = row_id
        self.col_id = col_id
        self.walls = {"top": True, 'right': True, 'down': True, 'left': True}
        self.start = False
        self.visited = False #Has the cell been "visited" by the map generating algorithm?
        self.total_row = total_row
        self.total_col = total_col
        self.index = None

    def knock_down_wall(self, neighbour: "Cell") -> None:
        wall_between = self.get_wall_between(neighbour)
        print(f"Cell pos: {self.row_id, self.col_id} Neighbour pos: {neighbour.row_id, neighbour.col_id}")
        print(wall_between)
        wall_between_0 = wall_between[0]
        self.walls[wall_between_0] = False
        neighbour.walls[wall_between[1]] = False
        neighbour.visited = True
    
    def get_opening(self) -> list:
        "Returns list of directions of the openins of the cell-walls"
        openings = []
        for key, value in self.walls.items():
            if value is False:
                openings.append(key)
        return openings

    def get_wall_between(self, neighbour: "Cell") -> list:
        "Returns the direction of the wall, first for the current cell, and afterwards for the neighbour"
        if self.row_id == neighbour.row_id: #The wall must be above or below current cell
            if self.col_id - neighbour.col_id == -1: #The wall is above the current cell
                return ['top', 'down']
            elif self.col_id - neighbour.col_id == 1: #The wall is below the current cell
                return ['down', 'top']
            print('2')
        if self.col_id == neighbour.col_id:
            if self.row_id - neighbour.row_id == -1: #The wall is to the right of current cell
                return ['right', 'left']
            elif self.row_id - neighbour.row_id == 1: #The wall is to the left of current cell
                return ['left', 'right']
            print('3')

        print('1')

    def has_openings(self) -> bool:
        return not (self.walls['top'] and self.walls['right'] and self.walls['down'] and self.walls['left'])
    