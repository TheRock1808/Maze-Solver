import array
import pathlib
# from typing import Iterator

# from maze_solver.models.border import Border
from maze_solver.models.maze import Maze
# from maze_solver.models.role import Role
from maze_solver.models.square import Square
from maze_solver.persistence.file_format import FileBody, FileHeader

FORMAT_VERSION: int = 1


def dump(maze: Maze, path: pathlib.Path) -> None:
    header, body = serialize(maze)
    with path.open(mode="wb") as file:
        header.write(file)
        body.write(file)

def serialize(maze: Maze) -> tuple[FileHeader, FileBody]:
    header = FileHeader(FORMAT_VERSION, maze.width, maze.height)
    body = FileBody(array.array("B", map(compress, maze)))
    return header, body

# def deserialize(header: FileHeader, body: FileBody) -> Iterator[Square]:
#     for index, square_value in enumerate(body.square_values):
#         row, column = divmod(index, header.width)
#         border, role = decompress(square_value)
#         yield Square(index, row, column, border, role)


def compress(square: Square) -> int:
    return (square.role << 4) | square.border.value


# def decompress(square_value: int) -> tuple[Border, Role]:
#     return Border(square_value & 0xF), Role(square_value >> 4)