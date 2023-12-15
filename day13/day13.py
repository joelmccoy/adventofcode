import os

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, "input.txt")


def match_off_by_one(s1, s2):
    ok = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if ok:
                return False
            else:
                ok = True

    return ok


def get_reflected_row_number_smudge(pattern: list[str]) -> int:
    for idx in range(len(pattern) - 1):
        bad = 0
        if pattern[idx] == pattern[idx + 1] or match_off_by_one(
            pattern[idx], pattern[idx + 1]
        ):
            delta = 0

            while True:
                if idx - delta < 0 or idx + delta + 1 >= len(pattern):
                    break
                if match_off_by_one(pattern[idx - delta], pattern[idx + delta + 1]):
                    bad += 1
                if pattern[idx - delta] != pattern[
                    idx + delta + 1
                ] and not match_off_by_one(
                    pattern[idx - delta], pattern[idx + delta + 1]
                ):
                    break
                if idx - delta <= 0 or idx + delta + 1 >= len(pattern) - 1:
                    if bad == 1:
                        return idx
                    break
                if pattern[idx - delta] != pattern[
                    idx + delta + 1
                ] and not match_off_by_one(
                    pattern[idx - delta], pattern[idx + delta + 1]
                ):
                    break
                delta += 1

    return -1


def get_reflected_row_number(pattern: list[str]) -> int:
    for idx in range(len(pattern) - 1):
        if pattern[idx] == pattern[idx + 1]:
            delta = 0
            while True:
                if idx - delta < 0 or idx + delta + 1 >= len(pattern):
                    return idx
                if pattern[idx - delta] != pattern[idx + delta + 1]:
                    break
                delta += 1

    return -1


def get_reflected_col_number(pattern: list[str]) -> int:
    flipped = [[] for i in range(len(pattern[0]))]
    for idx in range(len(pattern)):
        for idy in range(len(pattern[idx])):
            flipped[idy].append(pattern[idx][idy])

    return get_reflected_row_number(flipped)


def get_reflected_col_number_smudge(pattern: list[str]) -> int:
    flipped = [[] for i in range(len(pattern[0]))]
    for idx in range(len(pattern)):
        for idy in range(len(pattern[idx])):
            flipped[idy].append(pattern[idx][idy])

    return get_reflected_row_number_smudge(flipped)


def part_1(lines: list[str]) -> int:
    patterns = [[]]
    idx = 0
    for line in lines:
        if line == "\n":
            idx += 1
            patterns.append([])
            continue
        patterns[idx].append(line.strip())

    sum = 0
    for pattern in patterns:
        if (x := get_reflected_row_number(pattern)) >= 0:
            sum += (x + 1) * 100
        if (y := get_reflected_col_number(pattern)) >= 0:
            sum += y + 1

    return sum


def part_2(lines: list[str]) -> int:
    patterns = [[]]
    idx = 0
    for line in lines:
        if line == "\n" or line == "":
            idx += 1
            patterns.append([])
            continue
        patterns[idx].append(line.strip())
    sum = 0
    for pattern in patterns:
        if (x := get_reflected_row_number_smudge(pattern)) >= 0:
            sum += (x + 1) * 100
        if (y := get_reflected_col_number_smudge(pattern)) >= 0:
            sum += y + 1
    return sum


# save file as input.txt in same directory as this file
def main():
    with open(INPUT_FILE_PATH) as f:
        lines = f.readlines()
        print(part_1(lines))

    with open(INPUT_FILE_PATH) as f:
        lines = f.read().splitlines()
        print(part_2(lines))


if __name__ == "__main__":
    main()
