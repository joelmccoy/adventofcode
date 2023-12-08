import os
from enum import IntEnum

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, "input.txt")


class FaceCards(IntEnum):
    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14


class Hand(IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


def calculate_hand_value(hand: str) -> int:
    hand_counts = [hand.count(card) for card in set(hand)]

    if 5 in hand_counts:
        power = Hand.FIVE_OF_A_KIND
    elif 4 in hand_counts:
        power = Hand.FOUR_OF_A_KIND
    elif 3 in hand_counts:
        if 2 in hand_counts:
            power = Hand.FULL_HOUSE
        else:
            power = Hand.THREE_OF_A_KIND
    elif 2 in hand_counts:
        if hand_counts.count(2) == 2:
            power = Hand.TWO_PAIR
        else:
            power = Hand.ONE_PAIR
    else:
        power = Hand.HIGH_CARD

    return power


def calculate_hand_value_with_jokers(hand: str) -> int:
    hand_counts = [hand.count(card) for card in set(hand)]
    jokers = hand.count("J")

    if 5 in hand_counts:
        power = Hand.FIVE_OF_A_KIND
    elif 4 in hand_counts:
        power = Hand.FOUR_OF_A_KIND
    elif 3 in hand_counts:
        if 2 in hand_counts:
            power = Hand.FULL_HOUSE
        else:
            power = Hand.THREE_OF_A_KIND
    elif 2 in hand_counts:
        if hand_counts.count(2) == 2:
            power = Hand.TWO_PAIR
        else:
            power = Hand.ONE_PAIR
    else:
        power = Hand.HIGH_CARD

    if jokers == 1:
        if power == Hand.HIGH_CARD or power == Hand.FOUR_OF_A_KIND:
            power += 1
        elif (
            power == Hand.ONE_PAIR
            or power == Hand.TWO_PAIR
            or power == Hand.THREE_OF_A_KIND
        ):
            power += 2
    elif jokers == 2:
        if power == Hand.ONE_PAIR or power == Hand.FULL_HOUSE:
            power += 2
        elif power == Hand.TWO_PAIR:
            power = Hand.FOUR_OF_A_KIND
    elif jokers == 3:
        if power == Hand.THREE_OF_A_KIND or power == Hand.FULL_HOUSE:
            power += 2
    elif jokers == 4:
        power = Hand.FIVE_OF_A_KIND

    return power


def replace_hand(hand: str, part_2: bool = False) -> str:
    # replace face cards with characters so they can be sorted by value
    hand = hand.replace("A", "E").replace("K", "D").replace("Q", "C").replace("T", "A")
    if part_2:
        hand = hand.replace("J", "0")

    else:
        hand = hand.replace("J", "B")
    return hand


def part_1(lines: list[str], part_2: bool = False) -> int:
    hand_details = []
    for line in lines:
        split = line.split(" ")
        hand = split[0]
        hand_replaced = replace_hand(hand, part_2)
        bid = split[1]
        hand_details.append(
            (
                hand_replaced,
                int(bid),
                int(
                    calculate_hand_value_with_jokers(hand)
                    if part_2
                    else calculate_hand_value(hand)
                ),
            )
        )

    sorted_hands = sorted(hand_details, key=lambda x: (x[2], x[0]))

    score = 0
    for idx, hand in enumerate(sorted_hands):
        score += (idx + 1) * int(hand[1])

    return score


def part_2(lines: list[str]):
    score = part_1(lines, part_2=True)
    return score


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
