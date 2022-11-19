from typing import List

class Cell:

    """ A maze is built upon lots of cells. A cell is basically just four walls. One can think of the maze as an excel sheet
        When we generate the track, some of these walls are removed, and later these removed walls create a path from start to finish. """

    def __init__(self, row_idx, col_idx):
        self.row_idx = row_idx
        self.col_idx = col_idx

        self.walls = {
            'top': True,
            'bottom': True,
            'left': True,
            'right': True,
        }

        self.start = False
        self.visited = False
        self.index = None

    def __str__(self):
        return str(1 - int(sum(self.walls.values()) == 4))

    def __repr__(self):
        return str(1 - int(sum(self.walls.values()) == 4))

    def knock_down_wall(self, neighbour: 'Cell') -> None:
        """ Removes walls that connect with the neighbouring cell """

        wall_between = self.get_wall_between(neighbour)

        self.walls[wall_between[0]] = False
        neighbour.walls[wall_between[1]] = False

        neighbour.visited = True

    def get_wall_between(self, neighbour: 'Cell') -> List[str]:
        """ Returns a list telling which walls to knock down. 
            The first item is the current cell's wall to be knocked down
            And the second item is the neighbouring wall to be knocked down """

        vertical = self.row_idx == neighbour.row_idx

        if vertical:
            step_size = self.col_idx - neighbour.col_idx
            return ['top', 'bottom'][::step_size]
        elif not vertical:
            step_size = self.row_idx - neighbour.row_idx
            return ['left', 'right'][::step_size]

    def get_opening(self, neighbour: 'Cell') -> List[str]:
        """ Returns a list of places where the this cell's walls has been removed """

        return [key for key,val in self.walls.items() if val == False]
        
    def has_openings(self) -> bool:
        """ Return a boolean if all the cell's walls are still intact """

        return not (self.walls['top'] and self.walls['right'] and self.walls['down'] and self.walls['left'])