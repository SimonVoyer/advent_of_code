import os, re

GREEN = "green"
BLUE = "blue"
RED = "red"

RED_INDEX = 0
GREEN_INDEX = 1
BLUE_INDEX = 2

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

def possible_game_ids(path):
    id_sum = 0
    with open(path, 'r', encoding="utf-8") as file:
        for line in file:
            is_game_possible = True
            id = int(line.split(" ")[1].split(":")[0])
            sets = [set.strip() for set in re.split('[;]', line.split(": ")[1])]
            for set in sets:
                colors = [color.strip() for color in set.split(",")]
                color_count = count_colors(colors)
                if (color_count[RED_INDEX] > RED_MAX 
                    or color_count[BLUE_INDEX] > BLUE_MAX 
                    or color_count[GREEN_INDEX] > GREEN_MAX):
                    is_game_possible = False
            if is_game_possible:
                id_sum += id
    return id_sum

def fewest_cubes(path):
    sum_of_powers = 0
    with open(path, 'r', encoding="utf-8") as file:
        for line in file:
            sets = [set.strip() for set in re.split('[;]', line.split(": ")[1])]
            minimum_needed = [-1, -1, -1]
            for set in sets:
                colors = [color.strip() for color in set.split(",")]
                color_count = count_colors(colors)
                for i in range(len(minimum_needed)):
                    if color_count[i] > minimum_needed[i]:
                        minimum_needed[i] = color_count[i]
            sum_of_powers += minimum_needed[0] * minimum_needed[1] * minimum_needed[2]
    return sum_of_powers
                


def count_colors(colors):
    color_count = [0, 0, 0]
    for color in colors:
        count = int(color.split(" ")[0])
        if RED in color:
            color_count[RED_INDEX] += count
        elif BLUE in color:
            color_count[BLUE_INDEX] += count
        elif GREEN in color:
            color_count[GREEN_INDEX] += count
    return color_count


if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "input2.txt")
    print(f"Sum of possible game ids: {possible_game_ids(path)}")
    print(f"Sum of the power of the minimum set of cubes: {fewest_cubes(path)}")