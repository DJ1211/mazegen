from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None
            ):
        
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed

        if self._seed != None:
            random.seed(self._seed)
            
        

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(self._num_cols - 1, self._num_rows -1)
        self._reset_cells_visited()
        
    
    def _create_cells(self):
        self._cells = []
        for col in range(self._num_cols):
            col_list = []
            for row in range(self._num_rows):
                col_list.append(Cell(self._win))
            self._cells.append(col_list)
        
        for i, column in enumerate(self._cells):
            for j, cell in enumerate(column):
                self._draw_cell(i, j)
                
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        
        left_x = i * self._cell_size_x + self._x1
        right_x = (i + 1) * self._cell_size_x + self._x1
        top_y = j * self._cell_size_y + self._y1
        bottom_y = (j + 1) * self._cell_size_y + self._y1

        self._cells[i][j].draw(left_x, top_y, right_x, bottom_y)

        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[-1][-1]
        entrance.has_top_wall = False
        exit.has_bottom_wall = False

        entrance.draw(entrance._left_x, entrance._top_y, entrance._right_x, entrance._bottom_y)
        exit.draw(exit._left_x, exit._top_y, exit._right_x, exit._bottom_y)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True    

        while True:
            to_visit = []
        
            if i > 0:
                if self._cells[i - 1][j]._visited == False:
                    to_visit.append([i - 1, j])
        
            if i < len(self._cells) - 1:
                if self._cells[i + 1][j]._visited == False:
                    to_visit.append([i + 1, j])

            if j > 0:
                if self._cells[i][j - 1]._visited == False:
                    to_visit.append([i, j - 1])

            if j < len(self._cells[0]) - 1:
                if self._cells[i][j + 1]._visited == False:
                    to_visit.append([i, j + 1])

            if not to_visit:
                self._draw_cell(i, j)
                return
            
            rand_cell = random.randrange(len(to_visit))
            neighbour_i = to_visit[rand_cell][0]
            neighbour_j = to_visit[rand_cell][1]

            if neighbour_i != i:
                if neighbour_i > i:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i + 1][j].has_left_wall = False
                else:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i - 1][j].has_right_wall = False
            else:
                if neighbour_j > j:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j + 1].has_top_wall = False
                else:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j - 1].has_bottom_wall = False
            
            self._break_walls_r(neighbour_i, neighbour_j)
        
   
    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell._visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j]._visited = True
        
        if self._cells[i][j] == self._cells[-1][-1]:
            return True

        to_visit = []

        if i > 0:
            if self._cells[i - 1][j]._visited == False and self._cells[i][j].has_left_wall == False:
                to_visit.append([i - 1, j])
        
        if i < len(self._cells) - 1:
            if self._cells[i + 1][j]._visited == False and self._cells[i][j].has_right_wall == False:
                to_visit.append([i + 1, j])

        if j > 0:
            if self._cells[i][j - 1]._visited == False and self._cells[i][j].has_top_wall == False:
                to_visit.append([i, j - 1])

        if j < len(self._cells[0]) - 1:
            if self._cells[i][j + 1]._visited == False and self._cells[i][j].has_bottom_wall == False:
                to_visit.append([i, j + 1]) 
        
        for neighbour in to_visit:
            neighbour_i = neighbour[0]
            neighbour_j = neighbour[1]
            next_cell = self._cells[neighbour_i][neighbour_j]
            self._cells[i][j].draw_move(next_cell)

            if self._solve_r(neighbour_i, neighbour_j):
                return True

            else:
                self._cells[i][j].draw_move(next_cell, undo = True)
        
        return False

