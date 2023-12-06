import os
import re

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, "input.txt")

def calculate_num_of_winning_combos(race_duration: int, distance_to_beat: int) -> int:
    winning_combos = 0
    for time in range(race_duration):
        speed = time
        time_left = race_duration - time
        distance = speed * time_left
        if distance > distance_to_beat:
            winning_combos += 1
    
    return winning_combos

def get_number_of_winning_combinations(lines):
    regex = re.compile(r"(\d+)")
    times = regex.findall(lines[0])
    times = [int(i) for i in times]
    distances = regex.findall(lines[1])
    distances = [int(i) for i in distances]

    winning_combos = 1
    for race_number in range(len(times)):
        winning_combos *= calculate_num_of_winning_combos(times[race_number], distances[race_number])
    
    return winning_combos

def get_number_of_winning_combos_part_2(lines):
    time = lines[0].replace(" ", "")
    time = int(time.split(":")[1])
    distance = lines[1].replace(" ", "")
    distance = int(distance.split(":")[1])
    return calculate_num_of_winning_combos(time, distance)

# save file as input.txt in same directory as this file
def main():
    with open(INPUT_FILE_PATH) as f:
        lines = f.read().splitlines()
        print(get_number_of_winning_combinations(lines))
    
    with open(INPUT_FILE_PATH) as f:
        lines = f.read().splitlines()
        print(get_number_of_winning_combos_part_2(lines))


if __name__ == "__main__":
    main()
