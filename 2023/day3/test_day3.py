import pytest
from day3 import is_symbol, process_schematic

TEST_CASES_IS_SYMBOL = [("#", True), (".", False), ("4", False)]


@pytest.mark.parametrize("symbol, expected", TEST_CASES_IS_SYMBOL)
def test_is_symbol(symbol, expected):
    assert is_symbol(symbol) == expected


TEST_CASES = [
    (
        [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ],
        (4361, 467 * 35 + 755 * 598),
    ),
    (
        [
            "1.........",
            ".#.*......",
            "..........",
            "......#...",
            "...*4.....",
            "..........",
            "..........",
            "..........",
            ".....45...",
            "..........",
        ],
        (5, 0),
    ),
    (
        [
            "1",
            "*",
            ".",
            ".",
            "4",
            ".",
        ],
        (1, 0),
    ),
    (
        [
            "1*...43..32&",
        ],
        (33, 0),
    ),
    (
        [
            "123",
            "000",
            "423",
        ],
        (0, 0),
    ),
    (
        [
            "1#3",
            "111",
            ".2.",
        ],
        (115, 0),
    ),
    (
        [
            ".........232.633..........",
            ".............*............",
            "670-..@.......181......814",
            ".......563........741....*.",
        ],
        (2861, 633 * 181),
    ),
]


@pytest.mark.parametrize("test_case", TEST_CASES)
def test_process_schematic(test_case):
    lines = test_case[0]
    expected = test_case[1]
    assert process_schematic(lines) == expected
