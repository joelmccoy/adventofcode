import os
import copy

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, "input.txt")

def get_number_of_combinations(
    records: str, contiguous: list[int], current_count: int = 0
) -> int:
    number_of_combinations = 0
    contiguous = copy.deepcopy(contiguous)

    # base case
    if len(records) == 0:
        # pop a match
        if len(contiguous) > 0 and current_count == contiguous[-1]:
            contiguous.pop()
        if len(contiguous) == 0:
            return 1
        return 0

    if records[0] == ".":
        # pop a match
        if len(contiguous) > 0 and current_count == contiguous[-1]:
            contiguous.pop()
        
        current_count = 0
        number_of_combinations += get_number_of_combinations(
            records[1:], contiguous, current_count
        )

    elif records[0] == "#":
        current_count += 1
        if len(contiguous) == 0:
            return 0
        elif current_count > contiguous[-1]:
            return 0
        number_of_combinations += get_number_of_combinations(
            records[1:], contiguous, current_count
        )

    elif records[0] == "?":
        # try with .
        if len(records) == 1:
            new_with_dot = "."
        else:
            new_with_dot = f".{records[1:]}"  
        number_of_combinations += get_number_of_combinations(
            new_with_dot, contiguous, current_count
        )

        # try with #
        if len(records) == 1:
            new_with_pound = "#"
        else:
            new_with_pound = f"#{records[1:]}"
        
        number_of_combinations += get_number_of_combinations(
            new_with_pound, contiguous, current_count
        )

    return number_of_combinations


def part_1(lines):
    total = 0
    for line in lines:
        split = line.split(" ")
        records = split[0]

        # this will be a stack to maintain the matching of contiguous records
        # needs to be in reverse order
        contiguous = [int(x) for x in split[1].split(",")[::-1]]

        total += get_number_of_combinations(records, contiguous)
    
    return total





# save file as input.txt in same directory as this file
def main():
    with open(INPUT_FILE_PATH) as f:
        lines = f.read().splitlines()
        part_1(lines)


if __name__ == "__main__":
    main()
