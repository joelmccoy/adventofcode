import pytest
import day12

TEST_CASES_GET_NUM_COMBINATIONS = [
    (".??..??...?##.", [3, 1, 1], 4),
    ("???.###", [3, 1, 1], 1),
    ("?#?#?#?#?#?#?#?", [6, 1, 3, 1], 1),
    ("????.######..#####.", [5, 6, 1], 4)
]


@pytest.mark.parametrize("records,contiguous,expected", TEST_CASES_GET_NUM_COMBINATIONS)
def test_get_combinations(records, contiguous, expected):
    assert len(day12.get_combinations(records, contiguous)) == expected

TEST_CASES_PART_1 = [
    ([
        "???.### 1,1,3",
        ".??..??...?##. 1,1,3",
        "?#?#?#?#?#?#?#? 1,3,1,6",
        "????.#...#... 4,1,1",
        "????.######..#####. 1,6,5",
        "?###???????? 3,2,1"
    ], 21)
]

@pytest.mark.parametrize("lines,expected", TEST_CASES_PART_1)
def test_part_1(lines, expected):
    assert day12.part_1(lines) == expected