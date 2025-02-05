from tkinter import Tk, BOTH, Canvas, Button, Frame, LEFT

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg = "white", height = height, width = width)
        self.__canvas.pack(fill = BOTH, expand = 1)
        self.__is_running = False
        self.__solve_button = None 
        self.__maze_params = None

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
    
    def set_maze_params(self, margin, num_rows, num_cols, cell_size_x, cell_size_y, maze_class):
        self.__maze_params = {
            "margin": margin,
            "num_rows": num_rows,
            "num_cols": num_cols,
            "cell_size_x": cell_size_x,
            "cell_size_y": cell_size_y,
            "maze_class": maze_class
        }

    def set_maze(self, maze):
        self.__maze = maze

    def create_button(self):
        self.__root.configure(bg="white")

        button_frame = Frame(self.__root,
                             bg="white")
        button_frame.pack(pady=20)

        self.__solve_button = Button(button_frame, 
                   text="Solve", 
                   command=self.solve_button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

        self.__new_maze_button = Button(button_frame, 
                   text="New Maze", 
                   command=self.new_maze,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

        self.__solve_button.pack(side=LEFT, padx=10)
        self.__new_maze_button.pack(side=LEFT, padx=10)

    def solve_button_clicked(self):
        if hasattr(self, '_Window__maze'):
            self.__solve_button.config(text = "Solving...", state="disabled")
            self.__new_maze_button.config(text="Please Wait", state="disabled")
            is_solvable = self.__maze.solve()
            if not is_solvable:
                print("maze can not be solved!")
                self.__solve_button.config(text = "Impossible", state="disabled")
                self.__new_maze_button.config(text="New Maze", state="normal")
            else:
                print("maze solved!")
                self.__solve_button.config(text = "Solved!", state="disabled")
                self.__new_maze_button.config(text="New Maze", state="normal")


    def clear_canvas(self):
        self.__canvas.delete("all")

    def new_maze(self):
        self.__new_maze_button.config(text="Building...", state="disabled")
        self.__solve_button.config(text="Please Wait", state="disabled")
        self.clear_canvas()

        params = self.__maze_params
        MazeClass = params["maze_class"]
        new_maze = MazeClass(
            params["margin"],
            params["margin"],
            params["num_rows"],
            params["num_cols"],
            params["cell_size_x"],
            params["cell_size_y"],
            self
        )

        self.set_maze(new_maze)
        print("maze created")
        self.__solve_button.config(text="Solve", state="normal")
        self.__new_maze_button.config(text="New Maze", state="normal")

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

