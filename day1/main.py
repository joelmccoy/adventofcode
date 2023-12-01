from enum import Enum
import os


SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, "input.txt")


def get_digits(input_str: str, replace_words: bool = False) -> int:
    """Returns the first and last digits of a string as the int representation"""
    first = 0
    last = 0

    if replace_words is True:
        input_str = replace_words_in_string(input_str)
    for idx in range(len(input_str)):
        if input_str[idx].isdigit():
            first = input_str[idx]
            break
    for idx in range(len(input_str) - 1, -1, -1):
        if input_str[idx].isdigit():
            last = input_str[idx]
            break

    return int(first + last)


def replace_words_in_string(input_str: str) -> str:
    """Replaces all words in a string with their digit representation"""
    return (
        input_str.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )


def get_sum(f, replace_words: bool = False) -> int:
    """Returns the sum of all calibration values"""
    sum = 0
    for line in f:
        value = get_digits(line, replace_words=replace_words)
        sum += value
    return sum


# Save file as input.txt in same directory as this file
def main():
    with open(INPUT_FILE_PATH) as f:
        print(f"Part 1 Answer: {get_sum(f)}")

    with open(INPUT_FILE_PATH) as f:
        print(f"Part 2 Answer: {get_sum(f, replace_words=True)}")


if __name__ == "__main__":
    main()
