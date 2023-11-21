from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve_maze', methods=['POST'])
def solve_maze():
    # Here you would implement your maze-solving logic
    # For simplicity, let's just return a dummy solution for now
    solution = [[0, 1, 0], [0, 1, 0], [0, 0, 0]]

    return jsonify({'solution': solution})

if __name__ == '__main__':
    app.run(debug=True)
