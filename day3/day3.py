import os
import itertools
import math
from collections import defaultdict

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, "input.txt")


def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != "."


def check_char_near_symbol(lines: list[str], idx: int, idy: int) -> bool:
    square = list(itertools.product((-1, 0, 1), (-1, 0, 1)))
    for dx, dy in square:
        if dx == 0 and dy == 0:
            continue
        if 0 <= idx + dx < len(lines) and 0 <= idy + dy < len(lines[idx]):
            if is_symbol(lines[idx + dx][idy + dy]):
                return True


def get_nearby_gear(lines: list[str], idx: int, idy: int) -> tuple[int, int]:
    square = list(itertools.product((-1, 0, 1), (-1, 0, 1)))
    for dx, dy in square:
        if dx == 0 and dy == 0:
            continue
        if 0 <= idx + dx < len(lines) and 0 <= idy + dy < len(lines[idx]):
            if lines[idx + dx][idy + dy] == "*":
                return (idx + dx, idy + dy)
    return None


def process_schematic(lines: list[str]) -> tuple[int, int]:
    """
    Returns a tuple with the following:
    - The sum of all the parts in the schematic near a symbol
    - The gear ratio of all the values connected to a gear
    """
    parts_near_symbol = []
    gears_map = defaultdict(list)

    for idx in range(len(lines)):
        idy = 0
        while idy < len(lines[idx]):
            char = lines[idx][idy]
            if not char.isdigit():
                idy += 1
                continue

            number_str = ""
            is_near_symbol = False
            nearby_gear = None
            while char.isdigit() and idy < len(lines[idx]):
                if lines[idx][idy].isdigit():
                    if check_char_near_symbol(lines, idx, idy):
                        is_near_symbol = True
                    if get_nearby_gear(lines, idx, idy):
                        nearby_gear = get_nearby_gear(lines, idx, idy)

                    number_str += lines[idx][idy]
                    if idy == len(lines[idx]) - 1:
                        if is_near_symbol:
                            parts_near_symbol.append(number_str)
                        if nearby_gear:
                            gears_map[nearby_gear].append(int(number_str))
                        break

                if not lines[idx][idy].isdigit():
                    if is_near_symbol:
                        parts_near_symbol.append(number_str)
                    if nearby_gear:
                        gears_map[nearby_gear].append(int(number_str))
                    break

                idy += 1
            idy += 1
    return sum([int(part) for part in parts_near_symbol]), sum(
        math.prod(v) for v in gears_map.values() if len(v) == 2
    )


# Save file as input.txt in same directory as this file
def main():
    with open(INPUT_FILE_PATH) as f:
        lines = f.read().splitlines()
        sum_of_parts_near_symbol, sum_of_gear_ratio = process_schematic(lines)
        print(sum_of_parts_near_symbol)
        print(sum_of_gear_ratio)


if __name__ == "__main__":
    main()
