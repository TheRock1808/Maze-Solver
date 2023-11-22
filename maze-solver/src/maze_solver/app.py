# app.py
from flask import Flask, render_template, jsonify
from maze_solver.view.renderer import SVGRenderer
from maze_solver.maze_solver_utils import solve_maze_and_get_html, parse_path
import pathlib

app = Flask(__name__)

@app.route('/')
def index():
    # Call the function from maze_solver_utils to get the HTML content
    maze_path = pathlib.Path("C:/Users/HP/OneDrive/Documents/CODE/GT_Project/mazes/miniature.maze")
    html_content = solve_maze_and_get_html(maze_path)
    return render_template('index.html', maze_html=html_content)

@app.route('/solve_maze', methods=['POST'])
def solve_maze():
    # Here you would implement your maze-solving logic
    # For simplicity, let's just return a dummy solution for now
    solution = [[0, 1, 0], [0, 1, 0], [0, 0, 0]]
    return jsonify({'solution': solution})

if __name__ == '__main__':
    app.run(debug=True)
