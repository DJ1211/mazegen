from graphics import Window
from maze import Maze
import sys

def main():
    num_rows = 20
    num_cols = 24
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    win.set_maze_params(margin, num_rows, num_cols, cell_size_x, cell_size_y, Maze)
    print("maze created")

    win.enable_buttons()
    win.set_maze(maze)
    win.wait_for_close()

main()

