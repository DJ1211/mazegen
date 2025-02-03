from graphics import Line, Point

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._left_x = None
        self._right_x = None
        self._top_y = None
        self._bottom_y = None
        self._win = win

    def draw(self, left_x, top_y, right_x, bottom_y):
        self._left_x = left_x
        self._right_x = right_x
        self._top_y = top_y
        self._bottom_y = bottom_y

        if self.has_left_wall:
            line = Line(Point(left_x, top_y), Point(left_x, bottom_y))
            self._win.draw_line(line)

        if self.has_right_wall:
            line = Line(Point(right_x, top_y), Point(right_x, bottom_y))
            self._win.draw_line(line)

        if self.has_top_wall:
            line = Line(Point(left_x, top_y), Point(right_x, top_y))
            self._win.draw_line(line)

        if self.has_bottom_wall:
            line = Line(Point(left_x, bottom_y), Point(right_x, bottom_y))
            self._win.draw_line(line)