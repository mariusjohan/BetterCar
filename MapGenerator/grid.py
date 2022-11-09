class Grid:
    """TESTESTEST"""
    def __init__(self, row_id, col_id, total_row=16, total_col=9) -> None:
        self.row_id = row_id
        self.col_id = col_id
        self.walls = {"top": True, 'right': True, 'down': True, 'left': True}
        self.start = False
        self.visited = False #Has the cell been "visited" by the map generating algorithm?
        self.total_row = total_row
        self.total_col = total_col

    def knock_down_wall(self, neighbour) -> None:
        wall_between = self.get_wall_between(neighbour)
        self.walls[wall_between[0]] = False
        neighbour.walls[wall_between[1]] = False
    
    def get_opening(self) -> list:
        "Returns list of directions of the openins of the cell-walls"
        openings = []
        for key, value in self.walls.items():
            if value is False:
                openings.append(key)
        return openings

    def get_wall_between(self, neighbour) -> list:
        if self.row_id == neighbour.row_id: #The wall must be above or below current cell
            if self.col_id - neighbour.col_id == -1: #The wall is above the current cell
                return ['top', 'down']
            elif self.col_id - neighbour.col_id == 1: #The wall is below the current cell
                return ['down', 'top']
        if self.col_id == neighbour.col_id:
            if self.row_id - neighbour.row_id == -1: #The wall is to the right of current cell
                return ['right', 'left']
            elif self.row_id - neighbour.row_id == 1: #The wall is to the left of current cell
                return ['left', 'right']

    def get_neighbours(self) -> list:
        if self.row_id == 0:
            if self.col_id == 0:
                return [[self.row_id+1, self.col_id], [self.row_id, self.col_id+1]]
            if self.col_id == self.total_col:
                pass
    
