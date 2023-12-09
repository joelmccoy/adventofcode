from day9 import part_1, part_2
import pytest

TEST_CASES_PART_1 = [
    (
        [
            "0 3 6 9 12 15",
            "1 3 6 10 15 21",
            "10 13 16 21 30 45",
        ],
        114,
    ),
]


@pytest.mark.parametrize("lines,expected", TEST_CASES_PART_1)
def test_part_1(lines, expected):
    assert part_1(lines) == expected


TEST_CASES_PART_2 = [
    (
        [
            "0 3 6 9 12 15",
            "1 3 6 10 15 21",
            "10 13 16 21 30 45",
        ],
        2,
    ),
]


@pytest.mark.parametrize("lines,expected", TEST_CASES_PART_2)
def test_part_2(lines, expected):
    assert part_2(lines) == expected
