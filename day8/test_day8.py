from day8 import part_1, part_2
import pytest

TEST_CASES_PART_1 = [
    (["LLR", "AAA = (BBB, BBB)", "BBB = (AAA, ZZZ)", "ZZZ = (ZZZ, ZZZ)"], 6),
    (
        [
            "RL",
            "",
            "AAA = (BBB, CCC)",
            "BBB = (DDD, EEE)",
            "CCC = (ZZZ, GGG)",
            "DDD = (DDD, DDD)",
            "EEE = (EEE, EEE)",
            "GGG = (GGG, GGG)",
            "ZZZ = (ZZZ, ZZZ)",
        ],
        2,
    ),
]


@pytest.mark.parametrize("lines,expected", TEST_CASES_PART_1)
def test_part_1(lines, expected):
    assert part_1(lines) == expected


TEST_CASES_PART_2 = [
    (
        [
            "LR",
            "",
            "11A = (11B, XXX)",
            "11B = (XXX, 11Z)",
            "11Z = (11B, XXX)",
            "22A = (22B, XXX)",
            "22B = (22C, 22C)",
            "22C = (22Z, 22Z)",
            "22Z = (22B, 22B)",
            "XXX = (XXX, XXX)",
        ],
        6,
    )
]


@pytest.mark.parametrize("lines,expected", TEST_CASES_PART_2)
def test_part_2(lines, expected):
    assert part_2(lines) == expected
