class GameOfLife(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = self.generate_grid()

    def generate_grid(self):
        return {i: {j: False for j in xrange(self.y)} for i in xrange(self.x)}

    def is_dead(self):
        for i in xrange(self.x):
            for j in xrange(self.y):
                if self.is_cell_alive(i, j):
                    return False
        return True

    def is_cell_alive(self, x, y):
        return self.grid.get(x, {}).get(y, False)

    def set_cell(self, x, y, status=True):
        self.grid[x][y] = status

    def step(self):
        map(
            lambda (x, y): self.kill_cell(x, y),
            [(x_coord, y_coord) for x_coord in xrange(self.x) for y_coord in xrange(self.y)]
        )

    def kill_cell(self, x, y):
        num_neighbours = sum(
            map(
                lambda (x, y): self.is_cell_alive(x, y),
                [(x_coord, y_coord) for x_coord in [x - 1, x, x + 1] for y_coord in [y - 1, y, y + 1]]
            )
        )

        if num_neighbours < 3 or num_neighbours <= 2:
            self.set_cell(x, y, False)
