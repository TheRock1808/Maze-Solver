from pathlib import Path

from maze_solver.models.border import Border
from maze_solver.models.maze import Maze
from maze_solver.models.role import Role
from maze_solver.models.square import Square


def main() -> None:
    build_maze().dump(Path(__file__).with_suffix(".maze"))


def build_maze() -> Maze:
    return Maze(
        squares=(
            Square(index=0, row=0, column=0, border=Border.TOP | Border.LEFT),
            Square(index=1, row=0, column=1, border=Border.TOP),
            Square(index=2, row=0, column=2, border=Border.TOP | Border.RIGHT),
            Square(index=3, row=0, column=3, border=Border.LEFT | Border.BOTTOM, role=Role.EXIT),
            Square(index=4, row=0, column=4, border=Border.TOP | Border.RIGHT),
            Square(index=5, row=0, column=5, border=Border.TOP),
            Square(index=6, row=0, column=6, border=Border.TOP),
            Square(index=7, row=0, column=7, border=Border.TOP | Border.RIGHT),
            Square(index=8, row=1, column=0, border=Border.RIGHT | Border.LEFT),
            Square(index=9, row=1, column=1, border=Border.RIGHT | Border.BOTTOM | Border.LEFT),
            Square(index=10, row=1, column=2, border=Border.TOP | Border.LEFT),
            Square(index=11, row=1, column=3, border=Border.TOP),
            Square(index=12, row=1, column=4, border=Border.RIGHT | Border.LEFT),
            Square(index=13, row=1, column=5, border=Border.TOP),  #
            Square(index=14, row=1, column=6, border=Border.TOP),
            Square(index=15, row=1, column=7, border=Border.BOTTOM | Border.RIGHT),
            Square(index=16, row=2, column=0, border=Border.LEFT),
            Square(index=17, row=2, column=1, border=Border.TOP),
            Square(index=18, row=2, column=2, border=Border.RIGHT | Border.BOTTOM),
            Square(index=19, row=2, column=3, border=Border.BOTTOM | Border.LEFT | Border.RIGHT),
            Square(index=20, row=2, column=4, border=Border.RIGHT | Border.LEFT),
            Square(index=21, row=2, column=5, border=Border.RIGHT | Border.BOTTOM | Border.LEFT),
            Square(index=22, row=2, column=6, border=Border.LEFT | Border.BOTTOM),
            Square(index=23, row=2, column=7, border=Border.TOP | Border.RIGHT),
            Square(index=24, row=3, column=0, border=Border.LEFT | Border.RIGHT),
            Square(index=25, row=3, column=1, border=Border.BOTTOM | Border.LEFT),
            Square(index=26, row=3, column=2, border=Border.TOP | Border.BOTTOM),
            Square(index=27, row=3, column=3, border=Border.TOP | Border.BOTTOM),
            Square(index=28, row=3, column=4, border=Border.RIGHT | Border.BOTTOM),
            Square(index=29, row=3, column=5, border=Border.TOP | Border.LEFT),
            Square(index=30, row=3, column=6, border=Border.TOP | Border.BOTTOM),
            Square(index=31, row=3, column=7, border=Border.BOTTOM | Border.RIGHT),
            Square(index=32, row=4, column=0, border=Border.LEFT | Border.RIGHT),
            Square(index=33, row=4, column=1, border=Border.TOP | Border.LEFT),
            Square(index=34, row=4, column=2, border=Border.TOP | Border.BOTTOM),
            Square(index=35, row=4, column=3, border=Border.TOP),  #
            Square(index=36, row=4, column=4, border=Border.TOP | Border.BOTTOM | Border.RIGHT),
            Square(index=37, row=4, column=5, border=Border.BOTTOM | Border.LEFT),
            Square(index=38, row=4, column=6, border=Border.TOP | Border.RIGHT),
            Square(index=39, row=4, column=7, border=Border.TOP | Border.RIGHT | Border.LEFT),
            Square(index=40, row=5, column=0, border=Border.LEFT | Border.BOTTOM),
            Square(index=41, row=5, column=1, border=Border.BOTTOM | Border.RIGHT),
            Square(index=42, row=5, column=2, border=Border.TOP | Border.LEFT | Border.BOTTOM),
            Square(index=43, row=5, column=3, border=Border.BOTTOM),
            Square(index=44, row=5, column=4, border=Border.TOP, role=Role.ENTRANCE),
            Square(index=45, row=5, column=5, border=Border.TOP | Border.BOTTOM),
            Square(index=46, row=5, column=6, border=Border.BOTTOM),
            Square(index=47, row=5, column=7, border=Border.BOTTOM | Border.RIGHT),
        )
    )
    
if __name__ == '__main__':
    main()