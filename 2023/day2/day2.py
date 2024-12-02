from collections import defaultdict
import os
import re

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, "input.txt")

MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14


def process_set(game_set: str) -> dict[str, int]:
    """Returns a mapping of number of colored cubes in a set"""
    mapping = defaultdict(int)
    match_blue = re.search(r"(\d+)blue", game_set)
    if match_blue:
        mapping["blue"] = int(match_blue.group(1))
    match_red = re.search(r"(\d+)red", game_set)
    if match_red:
        mapping["red"] = int(match_red.group(1))
    match_green = re.search(r"(\d+)green", game_set)
    if match_green:
        mapping["green"] = int(match_green.group(1))
    return mapping


def process_game(game: str) -> bool:
    """
    Determines whether a game is valid.
    The game is valid if the number of each color of cube is less than the max specified
    """
    game_sets = game.split(";")
    for set in game_sets:
        results = process_set(set)
        if results["red"] > MAX_RED_CUBES:
            return False
        if results["green"] > MAX_GREEN_CUBES:
            return False
        if results["blue"] > MAX_BLUE_CUBES:
            return False
    return True


def process_game_min_values(game: str) -> dict[str, int]:
    """
    Takes a game consisting of sets of colored cubes and returns
    the minimum number of cubes of each color required to play the game
    """
    map = defaultdict(int)
    game_sets = game.split(";")
    for set in game_sets:
        results = process_set(set)
        map["red"] = max(map["red"], results["red"])
        map["green"] = max(map["green"], results["green"])
        map["blue"] = max(map["blue"], results["blue"])

    return map


def calculate_power(map: dict[str, int]) -> int:
    """Returns the product of the minimum number of cubes of each color"""
    return map["red"] * map["green"] * map["blue"]


def get_sum(lines: list[str]):
    """Returns the sum of the game ids of all valid games"""
    sum = 0
    for line in lines:
        line.strip()
        game_number = re.search(r"Game (\d+)", line).group(1)
        game = line.split(":")[1].replace(" ", "")
        if process_game(game):
            sum += int(game_number)
    return sum


def get_sum_of_powers(lines: list[str]):
    """Takes the input and returns the product of the minimum number of cubes of each color"""
    sum = 0
    for line in lines:
        line.strip()
        game = line.split(":")[1].replace(" ", "")
        map = process_game_min_values(game)
        sum += calculate_power(map)
    return sum


# Save file as input.txt in same directory as this file
def main():
    with open(INPUT_FILE_PATH) as f:
        lines = f.read().splitlines()
        print(get_sum(lines))

    with open(INPUT_FILE_PATH) as f:
        lines = f.read().splitlines()
        print(get_sum_of_powers(lines))


if __name__ == "__main__":
    main()
