from day7 import (
    part_1,
    calculate_hand_value,
    Hand,
    calculate_hand_value_with_jokers,
    part_2,
)
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


TEST_CASES_HAND_VALUE_JOKERS = [
    ("J2222", Hand.FIVE_OF_A_KIND),
    ("31J25", Hand.ONE_PAIR),
    ("31JJJ", Hand.FOUR_OF_A_KIND),
    ("33JJ5", Hand.FOUR_OF_A_KIND),
    ("T55J5", Hand.FOUR_OF_A_KIND),
    ("3JJ25", Hand.THREE_OF_A_KIND),
    ("3JJJJ", Hand.FIVE_OF_A_KIND),
    ("JJJJJ", Hand.FIVE_OF_A_KIND),
]


@pytest.mark.parametrize("input,expected", TEST_CASES_HAND_VALUE_JOKERS)
def test_calculate_hand_value_jokers(input, expected):
    assert calculate_hand_value_with_jokers(input) == expected


TEST_CASES_PART_2 = [
    (
        [
            "32T3K 765",
            "T55J5 684",
            "KK677 28",
            "KTJJT 220",
            "QQQJA 483",
        ],
        5905,
    )
]


@pytest.mark.parametrize("input,expected", TEST_CASES_PART_2)
def test_part_2(input, expected):
    assert part_2(input) == expected
