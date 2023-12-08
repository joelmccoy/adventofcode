from day7 import part_1, calculate_hand_value, Hand
import pytest

TEST_CASES = [
    (
        [
            "32T3K 765",
            "T55J5 684",
            "KK677 28",
            "KTJJT 220",
            "QQQJA 483",
        ],
        6440,
    )
]


@pytest.mark.parametrize("input,expected", TEST_CASES)
def test_part_1(input, expected):
    assert part_1(input) == expected

TEST_CASES_HAND_VALUE = [
    ("32222", Hand.FOUR_OF_A_KIND),
    ("33225", Hand.TWO_PAIR),
]

@pytest.mark.parametrize("input,expected", TEST_CASES_HAND_VALUE)
def test_calculate_hand_value(input, expected):
    assert calculate_hand_value(input) == expected