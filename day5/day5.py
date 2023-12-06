import os
import re
from collections import defaultdict

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, "input.txt")


def get_mappings(lines: list[str]) -> dict[int, list[tuple[int, int]]]:
    mappings: dict[int, dict[str, list[tuple[int, int]]]] = defaultdict(
        lambda: defaultdict(list)
    )
    mapping_number = 0
    for line in lines:
        if line == "":
            mapping_number += 1
            continue

        regex = re.compile(r"(\d+)")
        numbers = re.findall(regex, line)
        numbers = [int(num) for num in numbers]
        if len(numbers) == 0:
            continue

        dest_range = (numbers[0], numbers[0] + numbers[2] - 1)
        source_range = (numbers[1], numbers[1] + numbers[2] - 1)
        mappings[mapping_number]["source"].append(source_range)
        mappings[mapping_number]["dest"].append(dest_range)

    return mappings


def get_location_for_seed(seed: int, mappings: dict[int, list[tuple[int, int]]]) -> int:
    value: int = seed

    for mapping_number in range(len(mappings)):
        for idx, source_range in enumerate(mappings[mapping_number]["source"]):
            if source_range[0] <= value <= source_range[1]:
                value = mappings[mapping_number]["dest"][idx][0] + (
                    value - source_range[0]
                )
                break

    return value


def process_almanac(lines: list[str]) -> int:
    regex = re.compile(r"(\d+)")
    seeds = re.findall(regex, lines[0])
    seeds = [int(seed) for seed in seeds]

    mappings = get_mappings(lines[2:])
    lowest = 0
    for seed in seeds:
        if lowest == 0:
            lowest = get_location_for_seed(seed, mappings)
        else:
            lowest = min(lowest, get_location_for_seed(seed, mappings))

    return lowest


# save file as input.txt in same directory as this file
def main():
    with open(INPUT_FILE_PATH) as f:
        lines = f.read().splitlines()
        print(process_almanac(lines))


if __name__ == "__main__":
    main()
