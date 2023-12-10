import os
from enum import Enum
from collections import defaultdict

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, "input.txt")


class Direction(Enum):
    NORTH = (-1, 0)
    EAST = (0, 1)
    SOUTH = (1, 0)
    WEST = (0, -1)


def find_next_point_from_start(lines: list[str], start_point: (int, int)) -> (int, int):
    if lines[start_point[0]][start_point[1]] == "S":
        if lines[start_point[0] + 1][start_point[1]] in "|JL":
            return (start_point[0] + 1, start_point[1])
        elif lines[start_point[0] - 1][start_point[1]] in "|7F":
            return (start_point[0] - 1, start_point[1])
        elif lines[start_point[0]][start_point[1] + 1] in "-J7":
            return (start_point[0], start_point[1] + 1)
        elif lines[start_point[0]][start_point[1] - 1] in "-LF":
            return (start_point[0], start_point[1] - 1)
        else:
            raise Exception("No next point found")


def traverse(
    lines: list[str], start_point: (int, int), return_vertices: bool = False
) -> list[str]:
    """
    Traverse the loop and return the points in the loop
    If return_vertices is True, return the vertices of the loop instead
    """
    points = []
    vertices = []
    current_point = start_point
    next_point = find_next_point_from_start(lines, current_point)
    while True:
        points.append(current_point)
        next_point_value = lines[next_point[0]][next_point[1]]
        come_from = (current_point[0] - next_point[0], current_point[1] - next_point[1])

        if next_point_value == "S":
            vertices.append(next_point)
            break

        if next_point_value == "|":
            if come_from == Direction.NORTH.value:
                next_direction = Direction.SOUTH.value
            elif come_from == Direction.SOUTH.value:
                next_direction = Direction.NORTH.value
        if next_point_value == "-":
            if come_from == Direction.EAST.value:
                next_direction = Direction.WEST.value
            elif come_from == Direction.WEST.value:
                next_direction = Direction.EAST.value
        if next_point_value == "J":
            if come_from == Direction.NORTH.value:
                next_direction = Direction.WEST.value
            elif come_from == Direction.WEST.value:
                next_direction = Direction.NORTH.value
            vertices.append(next_point)
        if next_point_value == "L":
            if come_from == Direction.NORTH.value:
                next_direction = Direction.EAST.value
            elif come_from == Direction.EAST.value:
                next_direction = Direction.NORTH.value
            vertices.append(next_point)
        if next_point_value == "7":
            if come_from == Direction.SOUTH.value:
                next_direction = Direction.WEST.value
            elif come_from == Direction.WEST.value:
                next_direction = Direction.SOUTH.value
            vertices.append(next_point)
        if next_point_value == "F":
            if come_from == Direction.SOUTH.value:
                next_direction = Direction.EAST.value
            elif come_from == Direction.EAST.value:
                next_direction = Direction.SOUTH.value
            vertices.append(next_point)

        current_point = next_point
        next_point = (
            current_point[0] + next_direction[0],
            current_point[1] + next_direction[1],
        )

    return points if not return_vertices else vertices


def find_s(lines) -> (int, int):
    for line in lines:
        if "S" in line:
            return (lines.index(line), line.index("S"))


def part_1(lines):
    # find s
    s = find_s(lines)

    # find loop that connects to s
    loop = traverse(lines, s)

    # get the number of steps to the fartherst point in the loop
    return len(loop) // 2


def shoelace(points: list[(int, int)]) -> int:
    area = 0

    X = [point[0] for point in points] + [points[0][0]]
    Y = [point[1] for point in points] + [points[0][1]]

    for i in range(len(points)):
        area += X[i] * Y[i + 1] - Y[i] * X[i + 1]

    return abs(area) // 2


def part_2(lines):
    # find s
    s = find_s(lines)

    # find the loop that connects to s
    loop = traverse(lines, s)

    # find vertices that connects to s
    vertices = traverse(lines, s, return_vertices=True)

    # shoelace calculates the area inside a polygon
    area = shoelace(vertices)
    return area + 1 - len(loop) // 2


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
