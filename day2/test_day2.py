import pytest

from day2 import get_sum, process_game, get_sum_of_powers

# (input, expected)
TEST_CASES_GET_SUM = [
    (
        [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ],
        8,
    ),
    (
        [
            "Game 1: 1 red, 5 blue, 1 green; 16 blue, 3 red; 6 blue, 5 red; 4 red, 7 blue, 1 green",  # invalid
            "Game 2: 4 blue; 4 red, 3 blue, 1 green; 4 red, 9 blue, 2 green; 5 blue, 7 green, 4 red",  # valid
            "Game 3: 10 blue; 7 blue, 1 green; 19 blue, 1 green, 9 red",  # invalid
            "Game 4: 2 green; 14 blue, 14 red, 4 green; 12 red, 11 green, 13 blue; 5 green, 9 red, 4 blue; 9 red, 7 green, 12 blue; 2 green, 3 blue, 8 red",  # invalid
            "Game 5: 3 blue, 4 red; 12 red, 2 green, 15 blue; 1 red, 10 blue, 1 green",  # invalid
            "Game 6: 1 blue, 7 red; 3 green, 5 red, 1 blue; 1 green, 7 red; 6 red, 1 blue, 4 green; 1 green, 8 red, 1 blue; 2 green, 4 red, 1 blue",  # valid
            "Game 7: 11 green, 10 blue, 2 red; 1 green, 12 blue, 2 red; 9 green, 14 blue; 1 red, 19 blue, 15 green",  # invalid
            "Game 8: 4 green, 2 red, 14 blue; 9 green, 1 red, 15 blue; 2 green, 9 red, 8 blue; 11 green, 7 red, 8 blue; 9 red, 7 green, 6 blue",  # invalid
            "Game 9: 4 blue, 1 green, 2 red; 1 blue, 3 red; 1 red, 3 blue, 3 green",  # valid
            "Game 10: 4 red, 3 green, 6 blue; 2 green, 15 blue, 6 red; 3 green, 2 blue; 2 red, 1 green; 11 blue, 7 red, 4 green; 2 blue, 2 red, 4 green",  # invalid
        ],
        17,
    ),
]


@pytest.mark.parametrize("test_case", TEST_CASES_GET_SUM)
def test_get_sum(test_case):
    input = test_case[0]
    expected = test_case[1]
    assert get_sum(input) == expected


# (input, expected)
TEST_CASES_PROCESS_GAME = [
    (
        "3green,4blue,7red;7red,8green;7green,16red,1blue;8green,2blue,4red;5green,3blue,18red",
        False,
    ),
    ("3green,4blue,7red;", True),
    ("13green,12red,14blue;", True),
    ("", True),
    ("14green;", False),
    ("13red;", False),
    ("15blue;", False),
]


@pytest.mark.parametrize("test_case", TEST_CASES_PROCESS_GAME)
def test_process_game(test_case):
    input = test_case[0]
    expected = test_case[1]
    assert process_game(input) == expected


TEST_CASES_GET_SUM_OF_POWERS = [
    (
        [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ],
        2286
    ),
    (
        [
            "Game 1: 0 red, 0 green, 0 blue"
        ],
        0  
    )
]

@pytest.mark.parametrize("test_case", TEST_CASES_GET_SUM_OF_POWERS)
def test_get_sum_of_powers(test_case):
    input = test_case[0]
    expected = test_case[1]
    assert get_sum_of_powers(input) == expected