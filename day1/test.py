import pytest

from main import (
    get_digits,
    get_sum,
)

TEST_CASES_GET_DIGITS = [
    ("1abc2", 12),
    ("pqr3stu8vwx", 38),
    ("a1b2c3d4e5f", 15),
    ("treb7uchet", 77),
    ("1", 11),
    ("0abcdefg", 0),
    ("0abcdef5", 5),
    ("tgppgp9", 99),
]


@pytest.mark.parametrize("test_case", TEST_CASES_GET_DIGITS)
def test_get_digits(test_case):
    input_str = test_case[0]
    expected = test_case[1]
    assert get_digits(input_str) == expected


# (input, expected, replace_words)
TEST_CASES_GET_SUM = [
    (["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"], 142, False),
    (["1", "0abcdefg", "0abcdef5"], 16, False),
    ([], 0, False),
    (
        [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
        ],
        281,
        True,
    ),
    (
        [
            "one",
            "11",
        ],
        22,
        True,
    ),
    (["oneight", "eighthree", "sevenine", "1ei4ght", "zero1", ""], 205, True),
]


@pytest.mark.parametrize("test_case", TEST_CASES_GET_SUM)
def test_get_sum(test_case):
    input_strs = test_case[0]
    expected = test_case[1]
    replace_words = test_case[2]
    assert get_sum(input_strs, replace_words) == expected


TEST_CASES_GET_DIGITS_WITH_WORD_REPLACEMENT = [
    ("one", 11),
    ("nineight", 98),
    ("", 0),
    ("ooonneeeone", 11),
    ("twone", 21),
    ("eighthree", 83),
    ("sevenine", 79),
    ("on2e", 22),
    ("8nrbjbpjpnineseven", 87),
    ("7eightqmfmsn", 78),
    ("473sevensqpvvhfdrfiventgvmvrhtqx", 45),
    ("4eightfivenxftjch", 45),
]


@pytest.mark.parametrize("test_case", TEST_CASES_GET_DIGITS_WITH_WORD_REPLACEMENT)
def test_get_digits_with_word_replacement(test_case):
    input_str = test_case[0]
    expected = test_case[1]
    assert get_digits(input_str, replace_words=True) == expected
