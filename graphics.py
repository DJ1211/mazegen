from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg = "white", height = height, width = width)
        self.__canvas.pack(fill = BOTH, expand = 1)
        self.__is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__is_running = True  
        while self.__is_running:
            self.redraw()
        print("Window Closed")

    def draw_line(self, line, fill_colour = "black"):
        line.draw(self.__canvas, fill_colour)

    def close(self):
        self.__is_running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def draw(self, canvas, fill_colour = "black"):
        canvas.create_line(
            self.first.x, self.first.y, self.second.x, self.second.y, fill = fill_colour, width = 2
        )

