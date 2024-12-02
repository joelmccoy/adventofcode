import pytest
import day13

TEST_CASES_PART_ONE = [
    (
        [
            "#.##..##.",
            "..#.##.#.",
            "##......#",
            "##......#",
            "..#.##.#.",
            "..##..##.",
            "#.#.##.#.",
            "\n",
            "#...##..#",
            "#....#..#",
            "..##..###",
            "#####.##.",
            "#####.##.",
            "..##..###",
            "#....#..#",
        ],
        405,
    ),
]


@pytest.mark.parametrize("input, output", TEST_CASES_PART_ONE)
def test_part_one(input, output):
    assert day13.part_1(input) == output


TEST_CASES_PART_TWO = [
    (
        [
            "######...###.",
            "##########.##",
            "..##....#####",
            "..##..###.#..",
            "..##..#.#.#..",
            "......#......",
            ".#..#..#.#..#",
            "..##..#...##.",
            "#....#.#..##.",
            "######.#####.",
            ".......##..#.",
            ".......##..#.",
            "######.######",
        ],
        1100,
    )
]


@pytest.mark.parametrize("input, output", TEST_CASES_PART_TWO)
def test_part_two(input, output):
    assert day13.part_2(input) == output
