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
            Square(index=1, row=0, column=1, border=Border.TOP | Border.BOTTOM),
            Square(index=2, row=0, column=2, border=Border.TOP | Border.BOTTOM),
            Square(index=3, row=0, column=3, border=Border.TOP),
            Square(index=4, row=0, column=4, border=Border.TOP | Border.BOTTOM),
            Square(index=5, row=0, column=5, border=Border.TOP | Border.BOTTOM),
            Square(index=6, row=0, column=6, border=Border.TOP | Border.BOTTOM),
            Square(index=7, row=0, column=7, border=Border.TOP | Border.RIGHT),
            Square(index=8, row=0, column=8, border=Border.LEFT | Border.RIGHT, role=Role.EXTERIOR),
            Square(index=9, row=0, column=9, border=Border.TOP | Border.LEFT),
            Square(index=10, row=0, column=10, border=Border.TOP | Border.BOTTOM),
            Square(index=11, row=0, column=11, border=Border.TOP | Border.BOTTOM),
            Square(index=12, row=0, column=12, border=Border.TOP | Border.BOTTOM),
            Square(index=13, row=0, column=13, border=Border.TOP),
            Square(index=14, row=0, column=14, border=Border.TOP | Border.BOTTOM),
            Square(index=15, row=0, column=15, border=Border.TOP | Border.BOTTOM),
            Square(index=16, row=0, column=16, border=Border.TOP | Border.RIGHT),
            Square(index=17, row=1, column=0, border=Border.LEFT | Border.RIGHT),
            Square(index=18, row=1, column=1, border=Border.TOP | Border.BOTTOM | Border.LEFT, role=Role.WALL),
            Square(index=19, row=1, column=2, border=Border.TOP | Border.BOTTOM | Border.RIGHT, role=Role.WALL),
            Square(index=20, row=1, column=3, border=Border.LEFT | Border.RIGHT),
            Square(index=21, row=1, column=4, border=Border.TOP | Border.BOTTOM | Border.LEFT, role=Role.WALL),
            Square(index=22, row=1, column=5, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=23, row=1, column=6, border=Border.TOP | Border.BOTTOM | Border.RIGHT, role=Role.WALL),
            Square(index=24, row=1, column=7, border=Border.LEFT | Border.RIGHT),
            Square(index=25, row=1, column=8, border=Border.BOTTOM | Border.LEFT | Border.RIGHT, role=Role.EXTERIOR),
            Square(index=26, row=1, column=9, border=Border.LEFT | Border.RIGHT),
            Square(index=27, row=1, column=10, border=Border.TOP | Border.BOTTOM | Border.LEFT, role=Role.WALL),
            Square(index=28, row=1, column=11, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=29, row=1, column=12, border=Border.TOP | Border.BOTTOM | Border.RIGHT, role=Role.WALL),
            Square(index=30, row=1, column=13, border=Border.LEFT | Border.RIGHT),
            Square(index=31, row=1, column=14, border=Border.TOP | Border.BOTTOM | Border.LEFT, role=Role.WALL),
            Square(index=32, row=1, column=15, border=Border.TOP | Border.BOTTOM | Border.RIGHT, role=Role.WALL),
            Square(index=33, row=1, column=16, border=Border.LEFT | Border.RIGHT),
            Square(index=34, row=2, column=0, border=Border.LEFT),
            Square(index=35, row=2, column=1, border=Border.TOP | Border.BOTTOM),
            Square(index=36, row=2, column=2, border=Border.TOP | Border.BOTTOM),
            Square(index=37, row=2, column=3, border=Border.EMPTY),
            Square(index=38, row=2, column=4, border=Border.TOP | Border.BOTTOM),
            Square(index=39, row=2, column=5, border=Border.TOP),
            Square(index=40, row=2, column=6, border=Border.TOP | Border.BOTTOM),
            Square(index=41, row=2, column=7, border=Border.BOTTOM),
            Square(index=42, row=2, column=8, border=Border.TOP | Border.BOTTOM),
            Square(index=43, row=2, column=9, border=Border.BOTTOM),
            Square(index=44, row=2, column=10, border=Border.TOP | Border.BOTTOM),
            Square(index=45, row=2, column=11, border=Border.TOP),
            Square(index=46, row=2, column=12, border=Border.TOP | Border.BOTTOM),
            Square(index=47, row=2, column=13, border=Border.EMPTY),
            Square(index=48, row=2, column=14, border=Border.TOP | Border.BOTTOM),
            Square(index=49, row=2, column=15, border=Border.TOP | Border.BOTTOM),
            Square(index=50, row=2, column=16, border=Border.RIGHT),
            Square(index=51, row=3, column=0, border=Border.LEFT | Border.RIGHT),
            Square(index=52, row=3, column=1, border=Border.TOP | Border.BOTTOM | Border.LEFT, role=Role.WALL),
            Square(index=53, row=3, column=2, border=Border.TOP | Border.BOTTOM | Border.RIGHT, role=Role.WALL),
            Square(index=54, row=3, column=3, border=Border.LEFT | Border.RIGHT),
            Square(index=55, row=3, column=4, border=Border.TOP | Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=56, row=3, column=5, border=Border.LEFT | Border.RIGHT),
            Square(index=57, row=3, column=6, border=Border.TOP | Border.BOTTOM | Border.LEFT, role=Role.WALL),
            Square(index=58, row=3, column=7, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=59, row=3, column=8, border=Border.TOP, role=Role.WALL),
            Square(index=60, row=3, column=9, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=61, row=3, column=10, border=Border.TOP | Border.BOTTOM | Border.RIGHT, role=Role.WALL),
            Square(index=62, row=3, column=11, border=Border.LEFT | Border.RIGHT),
            Square(index=63, row=3, column=12, border=Border.TOP | Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=64, row=3, column=13, border=Border.LEFT | Border.RIGHT),
            Square(index=65, row=3, column=14, border=Border.TOP | Border.BOTTOM | Border.LEFT, role=Role.WALL),
            Square(index=66, row=3, column=15, border=Border.TOP | Border.BOTTOM | Border.RIGHT, role=Role.WALL),
            Square(index=67, row=3, column=16, border=Border.LEFT | Border.RIGHT),
            Square(index=68, row=4, column=0, border=Border.BOTTOM | Border.LEFT),
            Square(index=69, row=4, column=1, border=Border.TOP | Border.BOTTOM),
            Square(index=70, row=4, column=2, border=Border.TOP | Border.BOTTOM),
            Square(index=71, row=4, column=3, border=Border.RIGHT),
            Square(index=72, row=4, column=4, border=Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=73, row=4, column=5, border=Border.BOTTOM | Border.LEFT),
            Square(index=74, row=4, column=6, border=Border.TOP | Border.BOTTOM),
            Square(index=75, row=4, column=7, border=Border.TOP | Border.RIGHT),
            Square(index=76, row=4, column=8, border=Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=77, row=4, column=9, border=Border.TOP | Border.LEFT),
            Square(index=78, row=4, column=10, border=Border.TOP | Border.BOTTOM),
            Square(index=79, row=4, column=11, border=Border.BOTTOM | Border.RIGHT),
            Square(index=80, row=4, column=12, border=Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=81, row=4, column=13, border=Border.LEFT),
            Square(index=82, row=4, column=14, border=Border.TOP | Border.BOTTOM),
            Square(index=83, row=4, column=15, border=Border.TOP | Border.BOTTOM),
            Square(index=84, row=4, column=16, border=Border.BOTTOM | Border.RIGHT),
            Square(index=85, row=5, column=0, border=Border.TOP, role=Role.EXTERIOR),
            Square(index=86, row=5, column=1, border=Border.TOP, role=Role.EXTERIOR),
            Square(index=87, row=5, column=2, border=Border.TOP | Border.RIGHT, role=Role.EXTERIOR),
            Square(index=88, row=5, column=3, border=Border.LEFT | Border.RIGHT),
            Square(index=89, row=5, column=4, border=Border.LEFT, role=Role.WALL),
            Square(index=90, row=5, column=5, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=91, row=5, column=6, border=Border.TOP | Border.BOTTOM | Border.RIGHT, role=Role.WALL),
            Square(index=92, row=5, column=7, border=Border.LEFT | Border.RIGHT),
            Square(index=93, row=5, column=8, border=Border.BOTTOM | Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=94, row=5, column=9, border=Border.LEFT | Border.RIGHT),
            Square(index=95, row=5, column=10, border=Border.TOP | Border.BOTTOM | Border.LEFT, role=Role.WALL),
            Square(index=96, row=5, column=11, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=97, row=5, column=12, border=Border.RIGHT, role=Role.WALL),
            Square(index=98, row=5, column=13, border=Border.LEFT | Border.RIGHT),
            Square(index=99, row=5, column=14, border=Border.TOP | Border.LEFT, role=Role.EXTERIOR),
            Square(index=100, row=5, column=15, border=Border.TOP, role=Role.EXTERIOR),
            Square(index=101, row=5, column=16, border=Border.TOP, role=Role.EXTERIOR),
            Square(index=102, row=6, column=0, border=Border.EMPTY, role=Role.EXTERIOR),
            Square(index=103, row=6, column=1, border=Border.EMPTY, role=Role.EXTERIOR),
            Square(index=104, row=6, column=2, border=Border.RIGHT, role=Role.EXTERIOR),
            Square(index=105, row=6, column=3, border=Border.LEFT | Border.RIGHT),
            Square(index=106, row=6, column=4, border=Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=107, row=6, column=5, border=Border.TOP | Border.LEFT),
            Square(index=108, row=6, column=6, border=Border.TOP | Border.BOTTOM, role=Role.ENEMY),
            Square(index=109, row=6, column=7, border=Border.BOTTOM),
            Square(index=110, row=6, column=8, border=Border.TOP),
            Square(index=111, row=6, column=9, border=Border.BOTTOM),
            Square(index=112, row=6, column=10, border=Border.TOP | Border.BOTTOM),
            Square(index=113, row=6, column=11, border=Border.TOP | Border.RIGHT),
            Square(index=114, row=6, column=12, border=Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=115, row=6, column=13, border=Border.LEFT | Border.RIGHT),
            Square(index=116, row=6, column=14, border=Border.LEFT, role=Role.EXTERIOR),
            Square(index=117, row=6, column=15, border=Border.EMPTY, role=Role.EXTERIOR),
            Square(index=118, row=6, column=16, border=Border.EMPTY, role=Role.EXTERIOR),
            Square(index=119, row=7, column=0, border=Border.BOTTOM, role=Role.EXTERIOR),
            Square(index=120, row=7, column=1, border=Border.BOTTOM, role=Role.EXTERIOR),
            Square(index=121, row=7, column=2, border=Border.BOTTOM | Border.RIGHT, role=Role.EXTERIOR),
            Square(index=122, row=7, column=3, border=Border.LEFT | Border.RIGHT),
            Square(index=123, row=7, column=4, border=Border.BOTTOM | Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=124, row=7, column=5, border=Border.LEFT | Border.RIGHT),
            Square(index=125, row=7, column=6, border=Border.TOP | Border.LEFT, role=Role.WALL),
            Square(index=126, row=7, column=7, border=Border.TOP | Border.BOTTOM | Border.RIGHT, role=Role.WALL),
            Square(index=127, row=7, column=8, border=Border.LEFT | Border.RIGHT),
            Square(index=128, row=7, column=9, border=Border.TOP | Border.BOTTOM | Border.LEFT, role=Role.WALL),
            Square(index=129, row=7, column=10, border=Border.TOP | Border.RIGHT, role=Role.WALL),
            Square(index=130, row=7, column=11, border=Border.LEFT | Border.RIGHT),
            Square(index=131, row=7, column=12, border=Border.BOTTOM | Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=132, row=7, column=13, border=Border.LEFT | Border.RIGHT),
            Square(index=133, row=7, column=14, border=Border.BOTTOM | Border.LEFT, role=Role.EXTERIOR),
            Square(index=134, row=7, column=15, border=Border.BOTTOM, role=Role.EXTERIOR),
            Square(index=135, row=7, column=16, border=Border.BOTTOM, role=Role.EXTERIOR),
            Square(index=136, row=8, column=0, border=Border.TOP | Border.BOTTOM, role=Role.EXIT),
            Square(index=137, row=8, column=1, border=Border.TOP | Border.BOTTOM),
            Square(index=138, row=8, column=2, border=Border.TOP | Border.BOTTOM),
            Square(index=139, row=8, column=3, border=Border.EMPTY),
            Square(index=140, row=8, column=4, border=Border.TOP | Border.BOTTOM),
            Square(index=141, row=8, column=5, border=Border.RIGHT),
            Square(index=142, row=8, column=6, border=Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=143, row=8, column=7, border=Border.TOP | Border.BOTTOM | Border.LEFT),
            Square(index=144, row=8, column=8, border=Border.BOTTOM, role=Role.ENEMY),
            Square(index=145, row=8, column=9, border=Border.TOP | Border.BOTTOM | Border.RIGHT),
            Square(index=146, row=8, column=10, border=Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=147, row=8, column=11, border=Border.LEFT),
            Square(index=148, row=8, column=12, border=Border.TOP | Border.BOTTOM),
            Square(index=149, row=8, column=13, border=Border.EMPTY),
            Square(index=150, row=8, column=14, border=Border.TOP | Border.BOTTOM),
            Square(index=151, row=8, column=15, border=Border.TOP | Border.BOTTOM),
            Square(index=152, row=8, column=16, border=Border.TOP | Border.BOTTOM, role=Role.ENTRANCE),
            Square(index=153, row=9, column=0, border=Border.TOP, role=Role.EXTERIOR),
            Square(index=154, row=9, column=1, border=Border.TOP, role=Role.EXTERIOR),
            Square(index=155, row=9, column=2, border=Border.TOP | Border.RIGHT, role=Role.EXTERIOR),
            Square(index=156, row=9, column=3, border=Border.LEFT | Border.RIGHT, role=Role.REWARD),
            Square(index=157, row=9, column=4, border=Border.TOP | Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=158, row=9, column=5, border=Border.LEFT | Border.RIGHT),
            Square(index=159, row=9, column=6, border=Border.BOTTOM | Border.LEFT, role=Role.WALL),
            Square(index=160, row=9, column=7, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=161, row=9, column=8, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=162, row=9, column=9, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=163, row=9, column=10, border=Border.BOTTOM | Border.RIGHT, role=Role.WALL),
            Square(index=164, row=9, column=11, border=Border.LEFT | Border.RIGHT),
            Square(index=165, row=9, column=12, border=Border.TOP | Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=166, row=9, column=13, border=Border.LEFT | Border.RIGHT),
            Square(index=167, row=9, column=14, border=Border.TOP | Border.LEFT, role=Role.EXTERIOR),
            Square(index=168, row=9, column=15, border=Border.TOP, role=Role.EXTERIOR),
            Square(index=169, row=9, column=16, border=Border.TOP, role=Role.EXTERIOR),
            Square(index=170, row=10, column=0, border=Border.EMPTY, role=Role.EXTERIOR),
            Square(index=171, row=10, column=1, border=Border.EMPTY, role=Role.EXTERIOR),
            Square(index=172, row=10, column=2, border=Border.RIGHT, role=Role.EXTERIOR),
            Square(index=173, row=10, column=3, border=Border.LEFT | Border.RIGHT),
            Square(index=174, row=10, column=4, border=Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=175, row=10, column=5, border=Border.LEFT),
            Square(index=176, row=10, column=6, border=Border.TOP | Border.BOTTOM),
            Square(index=177, row=10, column=7, border=Border.TOP | Border.BOTTOM),
            Square(index=178, row=10, column=8, border=Border.TOP | Border.BOTTOM),
            Square(index=179, row=10, column=9, border=Border.TOP | Border.BOTTOM),
            Square(index=180, row=10, column=10, border=Border.TOP | Border.BOTTOM),
            Square(index=181, row=10, column=11, border=Border.RIGHT),
            Square(index=182, row=10, column=12, border=Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=183, row=10, column=13, border=Border.LEFT | Border.RIGHT),
            Square(index=184, row=10, column=14, border=Border.LEFT, role=Role.EXTERIOR),
            Square(index=185, row=10, column=15, border=Border.EMPTY, role=Role.EXTERIOR),
            Square(index=186, row=10, column=16, border=Border.EMPTY, role=Role.EXTERIOR),
            Square(index=187, row=11, column=0, border=Border.BOTTOM, role=Role.EXTERIOR),
            Square(index=188, row=11, column=1, border=Border.BOTTOM, role=Role.EXTERIOR),
            Square(index=189, row=11, column=2, border=Border.BOTTOM | Border.RIGHT, role=Role.EXTERIOR),
            Square(index=190, row=11, column=3, border=Border.LEFT | Border.RIGHT),
            Square(index=191, row=11, column=4, border=Border.BOTTOM | Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=192, row=11, column=5, border=Border.LEFT | Border.RIGHT),
            Square(index=193, row=11, column=6, border=Border.TOP | Border.BOTTOM | Border.LEFT, role=Role.WALL),
            Square(index=194, row=11, column=7, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=195, row=11, column=8, border=Border.TOP, role=Role.WALL),
            Square(index=196, row=11, column=9, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=197, row=11, column=10, border=Border.TOP | Border.BOTTOM | Border.RIGHT, role=Role.WALL),
            Square(index=198, row=11, column=11, border=Border.LEFT | Border.RIGHT),
            Square(index=199, row=11, column=12, border=Border.BOTTOM | Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=200, row=11, column=13, border=Border.LEFT | Border.RIGHT),
            Square(index=201, row=11, column=14, border=Border.BOTTOM | Border.LEFT, role=Role.EXTERIOR),
            Square(index=202, row=11, column=15, border=Border.BOTTOM, role=Role.EXTERIOR),
            Square(index=203, row=11, column=16, border=Border.BOTTOM, role=Role.EXTERIOR),
            Square(index=204, row=12, column=0, border=Border.TOP | Border.LEFT),
            Square(index=205, row=12, column=1, border=Border.TOP | Border.BOTTOM),
            Square(index=206, row=12, column=2, border=Border.TOP | Border.BOTTOM),
            Square(index=207, row=12, column=3, border=Border.EMPTY),
            Square(index=208, row=12, column=4, border=Border.TOP | Border.BOTTOM, role=Role.REWARD),
            Square(index=209, row=12, column=5, border=Border.BOTTOM),
            Square(index=210, row=12, column=6, border=Border.TOP | Border.BOTTOM),
            Square(index=211, row=12, column=7, border=Border.TOP | Border.RIGHT),
            Square(index=212, row=12, column=8, border=Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=213, row=12, column=9, border=Border.TOP | Border.LEFT),
            Square(index=214, row=12, column=10, border=Border.TOP | Border.BOTTOM),
            Square(index=215, row=12, column=11, border=Border.BOTTOM),
            Square(index=216, row=12, column=12, border=Border.TOP | Border.BOTTOM),
            Square(index=217, row=12, column=13, border=Border.EMPTY),
            Square(index=218, row=12, column=14, border=Border.TOP | Border.BOTTOM),
            Square(index=219, row=12, column=15, border=Border.TOP | Border.BOTTOM),
            Square(index=220, row=12, column=16, border=Border.TOP | Border.RIGHT),
            Square(index=221, row=13, column=0, border=Border.LEFT | Border.RIGHT),
            Square(index=222, row=13, column=1, border=Border.TOP | Border.BOTTOM | Border.LEFT, role=Role.WALL),
            Square(index=223, row=13, column=2, border=Border.TOP | Border.RIGHT, role=Role.WALL),
            Square(index=224, row=13, column=3, border=Border.LEFT | Border.RIGHT),
            Square(index=225, row=13, column=4, border=Border.TOP | Border.BOTTOM | Border.LEFT, role=Role.WALL),
            Square(index=226, row=13, column=5, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=227, row=13, column=6, border=Border.TOP | Border.BOTTOM | Border.RIGHT, role=Role.WALL),
            Square(index=228, row=13, column=7, border=Border.LEFT | Border.RIGHT),
            Square(index=229, row=13, column=8, border=Border.BOTTOM | Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=230, row=13, column=9, border=Border.LEFT | Border.RIGHT),
            Square(index=231, row=13, column=10, border=Border.TOP | Border.BOTTOM | Border.LEFT, role=Role.WALL),
            Square(index=232, row=13, column=11, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=233, row=13, column=12, border=Border.TOP | Border.BOTTOM | Border.RIGHT, role=Role.WALL),
            Square(index=234, row=13, column=13, border=Border.LEFT | Border.RIGHT),
            Square(index=235, row=13, column=14, border=Border.TOP | Border.LEFT, role=Role.WALL),
            Square(index=236, row=13, column=15, border=Border.TOP | Border.BOTTOM | Border.RIGHT, role=Role.WALL),
            Square(index=237, row=13, column=16, border=Border.LEFT | Border.RIGHT),
            Square(index=238, row=14, column=0, border=Border.BOTTOM | Border.LEFT),
            Square(index=239, row=14, column=1, border=Border.TOP | Border.RIGHT),
            Square(index=240, row=14, column=2, border=Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=241, row=14, column=3, border=Border.LEFT),
            Square(index=242, row=14, column=4, border=Border.TOP | Border.BOTTOM),
            Square(index=243, row=14, column=5, border=Border.TOP),
            Square(index=244, row=14, column=6, border=Border.TOP | Border.BOTTOM),
            Square(index=245, row=14, column=7, border=Border.BOTTOM),
            Square(index=246, row=14, column=8, border=Border.TOP | Border.BOTTOM),
            Square(index=247, row=14, column=9, border=Border.BOTTOM),
            Square(index=248, row=14, column=10, border=Border.TOP | Border.BOTTOM),
            Square(index=249, row=14, column=11, border=Border.TOP),
            Square(index=250, row=14, column=12, border=Border.TOP | Border.BOTTOM),
            Square(index=251, row=14, column=13, border=Border.RIGHT),
            Square(index=252, row=14, column=14, border=Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=253, row=14, column=15, border=Border.TOP | Border.LEFT),
            Square(index=254, row=14, column=16, border=Border.BOTTOM | Border.RIGHT),
            Square(index=255, row=15, column=0, border=Border.TOP | Border.BOTTOM | Border.RIGHT, role=Role.EXTERIOR),
            Square(index=256, row=15, column=1, border=Border.LEFT | Border.RIGHT),
            Square(index=257, row=15, column=2, border=Border.BOTTOM | Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=258, row=15, column=3, border=Border.LEFT | Border.RIGHT),
            Square(index=259, row=15, column=4, border=Border.TOP | Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=260, row=15, column=5, border=Border.LEFT | Border.RIGHT),
            Square(index=261, row=15, column=6, border=Border.TOP | Border.BOTTOM | Border.LEFT, role=Role.WALL),
            Square(index=262, row=15, column=7, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=263, row=15, column=8, border=Border.TOP, role=Role.WALL),
            Square(index=264, row=15, column=9, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=265, row=15, column=10, border=Border.TOP | Border.BOTTOM | Border.RIGHT, role=Role.WALL),
            Square(index=266, row=15, column=11, border=Border.LEFT | Border.RIGHT),
            Square(index=267, row=15, column=12, border=Border.TOP | Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=268, row=15, column=13, border=Border.LEFT | Border.RIGHT),
            Square(index=269, row=15, column=14, border=Border.BOTTOM | Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=270, row=15, column=15, border=Border.LEFT | Border.RIGHT),
            Square(index=271, row=15, column=16, border=Border.TOP | Border.BOTTOM | Border.LEFT, role=Role.EXTERIOR),
            Square(index=272, row=16, column=0, border=Border.TOP | Border.LEFT),
            Square(index=273, row=16, column=1, border=Border.BOTTOM),
            Square(index=274, row=16, column=2, border=Border.TOP | Border.BOTTOM),
            Square(index=275, row=16, column=3, border=Border.BOTTOM | Border.RIGHT),
            Square(index=276, row=16, column=4, border=Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=277, row=16, column=5, border=Border.BOTTOM | Border.LEFT),
            Square(index=278, row=16, column=6, border=Border.TOP | Border.BOTTOM),
            Square(index=279, row=16, column=7, border=Border.TOP | Border.RIGHT),
            Square(index=280, row=16, column=8, border=Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=281, row=16, column=9, border=Border.TOP | Border.LEFT),
            Square(index=282, row=16, column=10, border=Border.TOP | Border.BOTTOM),
            Square(index=283, row=16, column=11, border=Border.BOTTOM | Border.RIGHT),
            Square(index=284, row=16, column=12, border=Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=285, row=16, column=13, border=Border.BOTTOM | Border.LEFT),
            Square(index=286, row=16, column=14, border=Border.TOP | Border.BOTTOM),
            Square(index=287, row=16, column=15, border=Border.BOTTOM),
            Square(index=288, row=16, column=16, border=Border.TOP | Border.RIGHT),
            Square(index=289, row=17, column=0, border=Border.LEFT | Border.RIGHT),
            Square(index=290, row=17, column=1, border=Border.TOP | Border.BOTTOM | Border.LEFT, role=Role.WALL),
            Square(index=291, row=17, column=2, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=292, row=17, column=3, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=293, row=17, column=4, border=Border.BOTTOM, role=Role.WALL),
            Square(index=294, row=17, column=5, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=295, row=17, column=6, border=Border.TOP | Border.BOTTOM | Border.RIGHT, role=Role.WALL),
            Square(index=296, row=17, column=7, border=Border.LEFT | Border.RIGHT),
            Square(index=297, row=17, column=8, border=Border.BOTTOM | Border.LEFT | Border.RIGHT, role=Role.WALL),
            Square(index=298, row=17, column=9, border=Border.LEFT | Border.RIGHT),
            Square(index=299, row=17, column=10, border=Border.TOP | Border.BOTTOM | Border.LEFT, role=Role.WALL),
            Square(index=300, row=17, column=11, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=301, row=17, column=12, border=Border.BOTTOM, role=Role.WALL),
            Square(index=302, row=17, column=13, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=303, row=17, column=14, border=Border.TOP | Border.BOTTOM, role=Role.WALL),
            Square(index=304, row=17, column=15, border=Border.TOP | Border.BOTTOM | Border.RIGHT, role=Role.WALL),
            Square(index=305, row=17, column=16, border=Border.LEFT | Border.RIGHT),
            Square(index=306, row=18, column=0, border=Border.BOTTOM | Border.LEFT),
            Square(index=307, row=18, column=1, border=Border.TOP | Border.BOTTOM),
            Square(index=308, row=18, column=2, border=Border.TOP | Border.BOTTOM),
            Square(index=309, row=18, column=3, border=Border.TOP | Border.BOTTOM),
            Square(index=310, row=18, column=4, border=Border.TOP | Border.BOTTOM),
            Square(index=311, row=18, column=5, border=Border.TOP | Border.BOTTOM),
            Square(index=312, row=18, column=6, border=Border.TOP | Border.BOTTOM),
            Square(index=313, row=18, column=7, border=Border.BOTTOM),
            Square(index=314, row=18, column=8, border=Border.TOP | Border.BOTTOM),
            Square(index=315, row=18, column=9, border=Border.BOTTOM),
            Square(index=316, row=18, column=10, border=Border.TOP | Border.BOTTOM),
            Square(index=317, row=18, column=11, border=Border.TOP | Border.BOTTOM),
            Square(index=318, row=18, column=12, border=Border.TOP | Border.BOTTOM),
            Square(index=319, row=18, column=13, border=Border.TOP | Border.BOTTOM),
            Square(index=320, row=18, column=14, border=Border.TOP | Border.BOTTOM),
            Square(index=321, row=18, column=15, border=Border.TOP | Border.BOTTOM),
            Square(index=322, row=18, column=16, border=Border.BOTTOM | Border.RIGHT),
        )
    )


if __name__ == '__main__':
    main()