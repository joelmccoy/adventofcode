import os

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, "input.txt")


def extrapolate_history(numbers: list[int]) -> (int, int):
    numbers_matrix = []
    numbers_matrix.append(numbers)

    idx = 0
    while numbers_matrix[idx].count(0) != len(numbers_matrix[idx]):
        numbers_matrix.append([])
        for i in range(len(numbers_matrix[idx]) - 1):
            numbers_matrix[idx + 1].append(
                numbers_matrix[idx][i + 1] - numbers_matrix[idx][i]
            )
        idx += 1

    sum1 = 0
    for i in range(len(numbers_matrix) - 1, -1, -1):
        sum1 = sum1 + numbers_matrix[i][-1]

    previous = 0
    for i in range(len(numbers_matrix) - 2, -1, -1):
        previous = numbers_matrix[i][0] - previous

    return (sum1, previous)


def part_1(lines):
    sum = 0
    for line in lines:
        values = line.split(" ")
        values = [int(v) for v in values]
        sum += extrapolate_history(values)[0]

    return sum


def part_2(lines):
    sum = 0
    for line in lines:
        values = line.split(" ")
        values = [int(v) for v in values]
        sum += extrapolate_history(values)[1]

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
