import os
import re
from collections import defaultdict

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, "input.txt")


def process_card(card: str):
    matches = defaultdict(bool)
    split = card.split(":")
    numbers = split[1].split("|")
    winning_numbers_raw = numbers[0]
    actual_numbers_raw = numbers[1]

    regex = re.compile(r"(\d+)")
    winning_numbers = regex.findall(winning_numbers_raw)
    for num in winning_numbers:
        matches[num] = True

    actual_numbers = regex.findall(actual_numbers_raw)
    num_matches = 0
    for num in actual_numbers:
        if matches[num]:
            num_matches += 1

    if num_matches == 0:
        return 0
    else:
        return 2 ** (num_matches - 1)


def process_game(lines: list[str]):
    total = 0
    for card in lines:
        total += process_card(card)
    return total


def process_game_part_2(lines: str):
    card_map = defaultdict(lambda: 1)
    total_cards = 0
    for card in lines:
        split = card.split(":")
        card_number = int(re.findall(r"(\d+)", split[0])[0])
        numbers = split[1].split("|")
        winning_numbers_raw = numbers[0]
        actual_numbers_raw = numbers[1]

        matches = defaultdict(bool)
        regex = re.compile(r"(\d+)")
        winning_numbers = regex.findall(winning_numbers_raw)
        for num in winning_numbers:
            matches[num] = True

        actual_numbers = regex.findall(actual_numbers_raw)
        num_matches = 0
        for num in actual_numbers:
            if matches[num]:
                num_matches += 1

        for x in range(num_matches):
            card_map[card_number + x + 1] += 1 * card_map[card_number]

        total_cards += card_map[card_number]

    return total_cards


# Save file as input.txt in same directory as this file
def main():
    with open(INPUT_FILE_PATH) as f:
        lines = f.read().splitlines()
        print(process_game(lines))

    with open(INPUT_FILE_PATH) as f:
        lines = f.read().splitlines()
        print(process_game_part_2(lines))


if __name__ == "__main__":
    main()
