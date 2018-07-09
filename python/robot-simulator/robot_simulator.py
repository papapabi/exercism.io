from collections import namedtuple

Point = namedtuple('Point', 'x y')

EAST = Point(1, 0)
NORTH = Point(0, 1)
WEST = Point(-1, 0)
SOUTH = Point(0, -1)


class Robot(object):

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.x = x
        self.y = y
        self.bearing = bearing

    @property
    def coordinates(self):
        return (self.x, self.y)

    @property
    def actions(self):
        return self._actions

    def turn_left(self):
        x, y = self.bearing
        self.bearing = -y, x

    def turn_right(self):
        x, y = self.bearing
        self.bearing = y, -x

    def advance(self):
        x, y = self.bearing
        self.x += x
        self.y += y

    def simulate(self, instructions):
        for instruction in instructions:
            self._actions[instruction](self)

    _actions = {'R': turn_right,
               'L': turn_left,
               'A': advance}
