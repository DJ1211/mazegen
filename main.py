from graphics import Window
from cell import Cell

def main():

    win = Window(800, 600)

    cell1 = Cell(win)
    cell1.draw(55, 50, 155, 150)
   

    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.draw(201, 57, 303, 159)

    cell3 = Cell(win)
    cell3.has_right_wall = False
    cell3.draw(350, 50, 450, 150)

    cell1.draw_move(cell2)
    cell2.draw_move(cell3, undo=True)

    win.wait_for_close()

main()

