import os
import re
from collections import defaultdict
import math

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, "input.txt")


def part_2(lines) -> int:
    instructions = lines[0]

    mappings = {}
    regex = re.compile(r"([A-Z0-9]{3})")
    for idx in range(1, len(lines)):
        if lines[idx] == "":
            continue
        matches = regex.findall(lines[idx])
        start = matches[0]
        left = matches[1]
        right = matches[2]
        mappings[start] = (left, right)

    steps = 0
    currents = []
    for key in mappings:
        if key.endswith("A"):
            currents.append(key)

    paths = {}
    paths_done = defaultdict(bool)
    while True:
        instruction = instructions[steps % len(instructions)]
        steps += 1
        if instruction == "L":
            for idx in range(len(currents)):
                currents[idx] = mappings[currents[idx]][0]
        else:
            for idx in range(len(currents)):
                currents[idx] = mappings[currents[idx]][1]

        done = True
        for idx in range(len(currents)):
            if currents[idx].endswith("Z") and not paths_done[idx]:
                paths[idx] = steps
                paths_done[idx] = True

            if not paths_done[idx]:
                done = False

        if done:
            break

    steps_for_each = [path for path in paths.values()]
    return math.lcm(*steps_for_each)


def part_1(lines) -> int:
    instructions = lines[0]

    mappings = {}
    regex = re.compile(r"([A-Z]{3})")
    for idx in range(1, len(lines)):
        if lines[idx] == "":
            continue
        matches = regex.findall(lines[idx])
        start = matches[0]
        left = matches[1]
        right = matches[2]
        mappings[start] = (left, right)

    steps = 0
    current = "AAA"
    while True:
        instruction = instructions[steps % len(instructions)]
        steps += 1
        if instruction == "L":
            current = mappings[current][0]
        else:
            current = mappings[current][1]

        if current == "ZZZ":
            break

    return steps


# save file as input.txt in same directory as this file
def main():
    with open(INPUT_FILE_PATH) as f:
        lines = f.read().splitlines()
        print(part_1(lines))

    with open(INPUT_FILE_PATH) as f:
        lines = f.read().splitlines()
        print(part_2(lines))


if __name__ == "__main__":
    main()
