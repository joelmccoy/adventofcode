import pytest
from day6 import get_number_of_winning_combinations, get_number_of_winning_combos_part_2

TEST_CASES_PART_1 = [(["Time:      7  15   30", "Distance:  9  40  200"], 288)]


@pytest.mark.parametrize("lines, expected", TEST_CASES_PART_1)
def test_get_number_of_winning_combinations(lines, expected):
    assert get_number_of_winning_combinations(lines) == expected


TEST_CASES_PART_2 = [(["Time:      7  15   30", "Distance:  9  40  200"], 71503)]


@pytest.mark.parametrize("lines, expected", TEST_CASES_PART_2)
def test_get_number_of_winning_combos_part_2(lines, expected):
    assert get_number_of_winning_combos_part_2(lines) == expected
