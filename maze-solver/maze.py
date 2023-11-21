import random

def generate_maze(width, height):
    # Initialize the maze with walls
    maze = [[1] * width for _ in range(height)]

    def is_valid(x, y):
        return 0 <= x < width and 0 <= y < height and maze[y][x] == 1

    def carve(x, y):
        maze[y][x] = 0  # Mark the current cell as part of the maze

        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]  # Possible moves
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                maze[(y + ny) // 2][(x + nx) // 2] = 0  # Carve a path
                carve(nx, ny)

    entrance_x, entrance_y = random.randrange(1, width, 2), 0  # Entrance at the top
    exit_x, exit_y = random.randrange(1, width, 2), height - 1  # Exit at the bottom

    carve(entrance_x, entrance_y)
    carve(exit_x, exit_y)

    # Add more loops and dead-ends to make the maze more complex
    for _ in range(width * height // 8):
        x, y = random.randrange(1, width, 2), random.randrange(1, height, 2)
        carve(x, y)

    # Close unnecessary openings
    for i in range(width):
        if i != entrance_x:
            maze[0][i] = 1  # Close the top wall
        if i != exit_x:
            maze[height - 1][i] = 1  # Close the bottom wall

    return maze

def print_maze(maze):
    for row in maze:
        print(" ".join(["#" if cell == 1 else " " for cell in row]))

width = 21  # Adjust the width and height as needed
height = 21
maze = generate_maze(width, height)
print_maze(maze)
