from day11 import part_1
import pytest

TEST_CASES_PART_1 = [
    (
        [
            "...#......",
            ".......#..",
            "#.........",
            "..........",
            "......#...",
            ".#........",
            ".........#",
            "..........",
            ".......#..",
            "#...#.....",
        ],
        374,
    )
]


@pytest.mark.parametrize("lines,expected", TEST_CASES_PART_1)
def test_part_1(lines, expected):
    assert part_1(lines) == expected
