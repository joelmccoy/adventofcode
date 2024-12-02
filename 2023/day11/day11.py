import os
from collections import defaultdict

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, "input.txt")


def expand_galaxy(galaxy: list[str]) -> list[str]:
    expand_row = {}
    expand_col = {}

    for x in range(len(galaxy)):
        for y in range(len(galaxy[x])):
            if galaxy[x][y] == "#":
                expand_row[x] = False
                expand_col[y] = False

    x = 0
    expanded_rows = 0
    while x < len(galaxy):
        if expand_row.get(x - expanded_rows, True):
            galaxy.insert(x + 1, "." * len(galaxy[x]))
            x += 1
            expanded_rows += 1

        x += 1

    expanded_columns = 0
    for y in range(len(galaxy[0])):
        if expand_col.get(y, True):
            for x in range(len(galaxy)):
                galaxy[x] = (
                    galaxy[x][: y + expanded_columns]
                    + "."
                    + galaxy[x][y + expanded_columns :]
                )
            expanded_columns += 1

    return galaxy


def find_all_galaxy_coordinates(galaxy: list[str]) -> list[(int, int)]:
    coordinates = []
    for x in range(len(galaxy)):
        for y in range(len(galaxy[x])):
            if galaxy[x][y] == "#":
                coordinates.append((x, y))
    return coordinates


def part_1(lines):
    # expand galaxy
    expanded_galaxy = expand_galaxy(lines)

    # find all galaxy coordinates
    galaxy_coordinates = find_all_galaxy_coordinates(expanded_galaxy)

    # for each galaxy, add up the shortest distances
    sum = 0
    for x in range(len(galaxy_coordinates)):
        for y in range(len(galaxy_coordinates)):
            if x >= y:
                continue
            distance = abs(galaxy_coordinates[x][0] - galaxy_coordinates[y][0]) + abs(
                galaxy_coordinates[x][1] - galaxy_coordinates[y][1]
            )
            sum += distance
    return sum


def part_2(lines, expansion_factor=1000000):
    # get list of rows to expand
    rows_to_expand = defaultdict(lambda: True)
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if lines[x][y] == "#":
                rows_to_expand[x] = False
                break

    # get list of columns to expand
    cols_to_expand = defaultdict(lambda: True)
    for y in range(len(lines[0])):
        for x in range(len(lines)):
            if lines[x][y] == "#":
                cols_to_expand[y] = False
                break

    # get galaxy coordinates
    galaxy_coordinates = []
    row_expansion = 0
    for x in range(len(lines)):
        col_expansion = 0
        for y in range(len(lines[x])):
            if lines[x][y] == "#":
                galaxy_coordinates.append((x + row_expansion, y + col_expansion))
                continue
            if rows_to_expand[x]:
                row_expansion += expansion_factor - 1
                rows_to_expand[x] = False
            if cols_to_expand[y]:
                col_expansion += expansion_factor - 1

    # for each galaxy, add up the shortest distances
    sum = 0
    for x in range(len(galaxy_coordinates)):
        for y in range(len(galaxy_coordinates)):
            if x >= y:
                continue
            distance = abs(galaxy_coordinates[x][0] - galaxy_coordinates[y][0]) + abs(
                galaxy_coordinates[x][1] - galaxy_coordinates[y][1]
            )
            sum += distance
    return sum


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
