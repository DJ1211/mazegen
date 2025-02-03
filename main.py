from graphics import Window
from cell import Cell

def main():

    win = Window(800, 600)

    cell1 = Cell(win)
    cell1.draw(50, 50, 150, 150,)

    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.draw(200, 50, 300, 150)

    cell3 = Cell(win)
    cell3.has_right_wall = False
    cell3.draw(350, 50, 450, 150)

    cell4 = Cell(win)
    cell4.has_top_wall = False
    cell4.draw(500, 50, 600, 150)

    cell5 = Cell(win)
    cell5.has_bottom_wall = False
    cell5.draw(650, 50, 750, 150)

    cell6 = Cell(win)
    cell6.has_left_wall = False
    cell6.has_right_wall = False
    cell6.draw(50, 250, 150, 350)

    cell7 = Cell(win)
    cell7.has_left_wall = False
    cell7.has_top_wall = False
    cell7.draw(200, 250, 300, 350)

    cell8 = Cell(win)
    cell8.has_left_wall = False
    cell8.has_bottom_wall = False
    cell8.draw(350, 250, 450, 350)

    cell9 = Cell(win)
    cell9.has_right_wall = False
    cell9.has_top_wall = False
    cell9.draw(500, 250, 600, 350)

    cell9 = Cell(win)
    cell9.has_right_wall = False
    cell9.has_bottom_wall = False
    cell9.draw(650, 250, 750, 350)

    cell10 = Cell(win)
    cell10.has_top_wall = False
    cell10.has_bottom_wall = False
    cell10.draw(50, 450, 150, 550)

    win.wait_for_close()

main()

