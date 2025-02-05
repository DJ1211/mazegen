from graphics import Line, Point

class Cell:
    def __init__(self, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._left_x = None
        self._right_x = None
        self._top_y = None
        self._bottom_y = None
        self._win = win
        self._visited = False

    def draw(self, left_x, top_y, right_x, bottom_y):
        if self._win is None:
            return
        self._left_x = left_x
        self._right_x = right_x
        self._top_y = top_y
        self._bottom_y = bottom_y

        left_wall = Line(Point(left_x, top_y), Point(left_x, bottom_y))
        right_wall = Line(Point(right_x, top_y), Point(right_x, bottom_y))
        top_wall = Line(Point(left_x, top_y), Point(right_x, top_y))
        bottom_wall = Line(Point(left_x, bottom_y), Point(right_x, bottom_y))

        if self.has_left_wall:
            self._win.draw_line(left_wall)
        else:
            self._win.draw_line(left_wall, "white")

        if self.has_right_wall:
            self._win.draw_line(right_wall)
        else:
            self._win.draw_line(right_wall, "white")

        if self.has_top_wall:
            self._win.draw_line(top_wall)
        else:
            self._win.draw_line(top_wall, "white")

        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall)
        else:
            self._win.draw_line(bottom_wall, "white")
    
    def draw_move(self, to_cell, undo=False):
        center_x, center_y = self._calculate_center()
        to_cell_center_x, to_cell_center_y = to_cell._calculate_center()
        
        line = Line(Point(center_x, center_y), Point(to_cell_center_x, to_cell_center_y))
        if undo:
            self._win.draw_line(line, "gray")
        else:
            self._win.draw_line(line, "red")
    
    def _calculate_center(self):
        center_x = (self._left_x + self._right_x) / 2
        center_y = (self._top_y + self._bottom_y) / 2

        return center_x, center_y