from nose.tools import assert_true, assert_false, assert_equal
from conway import GameOfLife


class TestConwayTestCase(object):

    def test_grid_dimensions_load(self):
        game = GameOfLife(100, 100)

        assert_equal(game.x, 100)
        assert_equal(game.y, 100)

    def test_creates_grid(self):
        game = GameOfLife(100, 100)

        assert_equal(
            game.grid,
            {i: {j: False for j in xrange(100)} for i in xrange(100)}
        )

    def test_initial_grid_is_empty(self):
        game = GameOfLife(5, 5)

        assert_true(game.is_dead())

    def test_is_cell_alive_or_dead(self):
        game = GameOfLife(5, 5)
        game.set_cell(1, 1)

        assert_true(game.is_cell_alive(x=1, y=1))
        assert_false(game.is_cell_alive(x=2, y=1))

    def test_set_cell_status(self):
        game = GameOfLife(10, 10)

        game.set_cell(5, 4)
        game.set_cell(1, 2)

        assert_true(game.is_cell_alive(x=5, y=4))
        assert_true(game.is_cell_alive(x=1, y=2))

    def test_set_cell_status_to_dead(self):
        game = GameOfLife(10, 10)

        game.set_cell(5, 4, False)
        game.set_cell(1, 2, True)

        assert_false(game.is_cell_alive(x=5, y=4))
        assert_true(game.is_cell_alive(x=1, y=2))

    def test_detached_cell_dies(self):
        game = GameOfLife(10, 10)
        game.set_cell(5, 5)

        game.step()

        assert_false(game.is_cell_alive(x=5, y=5))

    def test_underpopulated_area_cell_dies(self):
        game = GameOfLife(10, 10)
        game.set_cell(5, 5)
        game.set_cell(5, 6)

        game.step()

        assert_false(game.is_cell_alive(x=5, y=5))
        assert_false(game.is_cell_alive(x=5, y=6))

    def test_overpopulated_area_cell_dies(self):
        game = GameOfLife(10, 10)
        game.set_cell(0, 0)
        game.set_cell(1, 1)
        game.set_cell(0, 1)
        game.set_cell(1, 0)
        game.set_cell(2, 1)

        game.step()

        assert_false(game.is_cell_alive(x=1, y=1))

    def test_well_populated_area_cell_dies(self):
        game = GameOfLife(10, 10)
        game.set_cell(5, 5)
        game.set_cell(4, 5)
        game.set_cell(5, 4)
        game.set_cell(4, 4)

        game.step()

        assert_true(game.is_cell_alive(x=5, y=4))
        assert_true(game.is_cell_alive(x=4, y=4))
        assert_true(game.is_cell_alive(x=5, y=5))
        assert_true(game.is_cell_alive(x=4, y=5))
