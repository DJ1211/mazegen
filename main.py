from graphics import Window
from cell import Cell
from maze import Maze

def main():
    num_rows = 10
    num_cols = 15
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    seed = 0
    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

#    cell1 = Cell(win)
#    cell1.draw(55, 50, 155, 150)
   

#    cell2 = Cell(win)
#    cell2.has_left_wall = False
#    cell2.draw(201, 57, 303, 159)

#    cell3 = Cell(win)
#    cell3.has_right_wall = False
#    cell3.draw(350, 50, 450, 150)

#    cell1.draw_move(cell2)
#    cell2.draw_move(cell3, undo=True)

    win.wait_for_close()

main()

