import argparse
import pathlib
import tkinter as tk
from tkinter import filedialog
from maze_solver.graphs.solver import solve_all
from maze_solver.models.maze import Maze
from maze_solver.view.renderer import SVGRenderer

class MazeSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Solver")

        self.file_path = None

        open_button = tk.Button(root, text="Open Maze File", command=self.open_file)
        open_button.pack(pady=10)

        solve_button = tk.Button(root, text="Solve Maze", command=self.solve_and_display)
        solve_button.pack(pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Maze files", "*.maze *.txt")])
        if file_path:
            self.file_path = pathlib.Path(file_path)
            print(f"Selected maze file: {self.file_path}")

    def solve_and_display(self):
        if self.file_path:
            maze = Maze.load(self.file_path)
            solutions = solve_all(maze)

            if solutions:
                renderer = SVGRenderer()

                renderer.render(maze).preview()

                for solution in solutions:
                    renderer.render(maze, solution).preview()
            else:
                print("No solution found")
        else:
            print("Please select a maze file first.")

def main():
    root = tk.Tk()
    app = MazeSolverGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
