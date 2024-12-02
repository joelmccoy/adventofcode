from day10 import part_1, part_2
import pytest

TEST_CASES_PART_1 = [
    ([".....", ".S-7.", ".|.|.", ".L-J.", "....."], 4),
    (["..F7.", ".FJ|.", "SJ.L7", "|F--J", "LJ..."], 8),
]


@pytest.mark.parametrize("lines,expected", TEST_CASES_PART_1)
def test_part_1(lines, expected):
    assert part_1(lines) == expected


TEST_CASES_PART_2 = [
    ([".....", ".S-7.", ".|.|.", ".L-J.", "....."], 1),
    (["..F7.", ".FJ|.", "SJ.L7", "|F--J", "LJ..."], 1),
    (
        [
            ".F----7F7F7F7F-7....",
            ".|F--7||||||||FJ....",
            ".||.FJ||||||||L7....",
            "FJL7L7LJLJ||LJ.L-7..",
            "L--J.L7...LJS7F-7L7.",
            "....F-J..F7FJ|L7L7L7",
            "....L7.F7||L7|.L7L7|",
            ".....|FJLJ|FJ|F7|.LJ",
            "....FJL-7.||.||||...",
            "....L---J.LJ.LJLJ...",
        ],
        8,
    ),
    (
        [
            "...........",
            ".S-------7.",
            ".|F-----7|.",
            ".||.....||.",
            ".||.....||.",
            ".|L-7.F-J|.",
            ".|..|.|..|.",
            ".L--J.L--J.",
            "...........",
        ],
        4,
    ),
]


@pytest.mark.parametrize("lines,expected", TEST_CASES_PART_2)
def test_part_2(lines, expected):
    assert part_2(lines) == expected
