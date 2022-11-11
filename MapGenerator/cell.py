class Cell:
    """
    A maze is built upon a lots of cells. A cell is basically just four walls. One can think of the maze as an excel sheet
    When we generate the track, we remove some of these walls, which can be used to create the actual race track, by inserting images
    """

    def __init__(self, row_id, col_id, total_row=16, total_col=9) -> None:
        self.row_id = row_id
        self.col_id = col_id
        self.walls = {"top": True, 'right': True, 'down': True, 'left': True}
        self.start = False
        self.visited = False  # Has the cell been "visited" by the map generating algorithm?
        self.total_row = total_row
        self.total_col = total_col
        self.index = None

    def knock_down_wall(self, neighbour: "Cell") -> None:
        wall_between = self.get_wall_between(neighbour)
        # print(f"Cell pos: {self.row_id, self.col_id} Neighbour pos: {neighbour.row_id, neighbour.col_id}")
        # print(wall_between)
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
        if self.row_id == neighbour.row_id:  # The wall must be above or below
            if self.col_id - neighbour.col_id == 1:  # the wall is above
                return ['top', 'down']
            elif self.col_id - neighbour.col_id == -1:  # The wall is below
                return ['down', 'top']
        if self.col_id == neighbour.col_id:  # The is to the side of the cell
            if self.row_id - neighbour.row_id == -1:  # RIGHT
                return ['right', 'left']
            elif self.row_id - neighbour.row_id == 1:  # LEFT
                return ['left', 'right']
            print('3')

        print('1')

    def has_openings(self) -> bool:
        return not (self.walls['top'] and self.walls['right'] and self.walls['down'] and self.walls['left'])
