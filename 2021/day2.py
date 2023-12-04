import os


FORWARD = "forward"
UP = "up"
DOWN = "down"

DIRECTION = 0
AMPLITUDE = 1

def naive_submarine(input_path:str) -> None:
    horizontal_position = 0
    vertical_position = 0
    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file:
            commands = line.split()
            if commands[DIRECTION] == FORWARD:
                horizontal_position += int(commands[AMPLITUDE])
            elif commands[DIRECTION] == UP:
                vertical_position -= int(commands[AMPLITUDE])
            else : #commands[DIRECTION] == DOWN
                vertical_position += int(commands[AMPLITUDE])
    return horizontal_position * vertical_position


def submarine_read_the_docs(input_path:str) -> None:
    horizontal_position = 0
    vertical_position = 0
    aim = 0
    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file:
            commands = line.split()
            if commands[DIRECTION] == FORWARD:
                forward = int(commands[AMPLITUDE])
                horizontal_position += forward
                vertical_position += aim * forward
            elif commands[DIRECTION] == UP:
                aim -= int(commands[AMPLITUDE])
            else : #commands[DIRECTION] == DOWN
                aim += int(commands[AMPLITUDE])
    return horizontal_position * vertical_position


if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day2.txt")
    print(f"The submarine with naive commands has a position product of {naive_submarine(path)}.")
    print(f"The submarine with the actual commands has a position product of {submarine_read_the_docs(path)}.")