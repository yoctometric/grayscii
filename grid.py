import random

class Grid:
    """
    A class used to handle 2d grids of characters
    """
    def __init__(self, w: int, h: int, fill: str='.') -> None:
        self.width = w
        self.height = h

        self.board = [[fill for y in range(h)] for x in range(w)]


    def set_pixel(self, x: int, y: int, c: str) -> str:
        """
        Sets the pixel to a new char and returns the old char
        """
        old = self.board[x][y]
        self.board[x][y] = c
        return old


    def __str__(self):
        """
        Returns a prettily formatted version of the grid for rendering
        """
        pretty = ""
        for y in range(self.height):
            for x in range(self.width):
                pretty += self.board[x][y]
            pretty += "\n"

        return pretty



class BrightnessGrid(Grid):
    """
    An extension of Grid that is better suited for drawing with greyscale levels
    """
    def __init__(self, w: int, h: int, fill: str = '.', palette: list = ['.', 'o', 'O', '0']) -> None:
        self.set_palette(palette)
        super().__init__(w, h, fill)


    def set_palette(self, palette: list):
        """
        Sets the palette that the grid will use to draw points.
        Takes a list of characters, where the lowest index corresponds to the lowest brightness values and the highest index corresponds to the highest brightness value
        """
        self.palette = palette


    def draw_point(self, x: int, y: int, level: float):
        """
        Places a point onto the grid based on how bright (level) the point should be
        """
        # clamp level
        if level > 1:
            level = 1
        elif level < 0:
            level = 0
        
        for i in range(len(self.palette)-1, -1, -1):
            thresh = i / len(self.palette)
            if level >= thresh:
                self.set_pixel(x, y, c=self.palette[i])
                return



if __name__ == "__main__":
    grid = BrightnessGrid(200, 60, ' ')
    
    for x in range(grid.width):
        for y in range(grid.height):
            val = (x+y) / (grid.width + grid.height) + random.random() / 4
            grid.draw_point(x, y, val)

    print(grid)