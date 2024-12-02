from day11 import part_1, part_2
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


TEST_CASES_PART_2 = [
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
        10,
        1030,
    )
]


@pytest.mark.parametrize("lines,expansion_factor,expected", TEST_CASES_PART_2)
def test_part_2(lines, expansion_factor, expected):
    assert part_2(lines, expansion_factor) == expected
