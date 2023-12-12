import os
import copy

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, "input.txt")

def get_combinations(
    records: str, contiguous: list[int], current_count: int = 0
) -> list[str]:
    combinations = []
    contiguous = copy.deepcopy(contiguous)

    # base case
    if len(records) == 0:
        # pop a match
        if len(contiguous) > 0 and current_count == contiguous[-1]:
            contiguous.pop()
        if len(contiguous) == 0:
            return [""]
        return []

    if records[0] == ".":
        # pop a match
        if len(contiguous) > 0 and current_count == contiguous[-1]:
            contiguous.pop()
        elif len(contiguous) > 0 and current_count > 0 and current_count != contiguous[-1]:
            return []
        
        current_count = 0
        for x in get_combinations(
            records[1:], contiguous, current_count
        ):
            combinations.append(f".{x}")

    elif records[0] == "#":
        current_count += 1
        if len(contiguous) == 0:
            return []
        elif current_count > contiguous[-1]:
            return []
        for x in get_combinations(
            records[1:], contiguous, current_count
        ):
            combinations.append(f"#{x}")

    elif records[0] == "?":
        # try with .
        if len(records) == 1:
            new_with_dot = "."
        else:
            new_with_dot = f".{records[1:]}"  
        combinations.extend(get_combinations(
            new_with_dot, contiguous, current_count
        ))

        # try with #
        if len(records) == 1:
            new_with_pound = "#"
        else:
            new_with_pound = f"#{records[1:]}"
        
        combinations.extend(get_combinations(
            new_with_pound, contiguous, current_count
        ))
        
    return combinations


def part_1(lines):
    total = 0
    for line in lines:
        split = line.split(" ")
        records = split[0]

        # this will be a stack to maintain the matching of contiguous records
        # needs to be in reverse order
        contiguous = [int(x) for x in split[1].split(",")[::-1]]
        total += len(get_combinations(records, contiguous))
    
    return total





# save file as input.txt in same directory as this file
def main():
    with open(INPUT_FILE_PATH) as f:
        lines = f.read().splitlines()
        print(part_1(lines))


if __name__ == "__main__":
    main()
