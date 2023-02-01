import os, copy


DIRECTION = 0
NUMBER_OF_STEPS = 1

HEAD = 0
VISITED_FLAG = 1

UP = 'U'
DOWN = 'D'
RIGHT = 'R'
LEFT = 'L'

GRID_HEIGHT = 1000
GRID_LENGTH = 1000
STARTING_POSITION = (GRID_HEIGHT//2,GRID_LENGTH//2)

X = 0
Y = 1


def clamp(x):
    """
    Clamps x between -1 and 1.
    """
    if x < -1:
        x = -1
    elif x > 1:
        x = 1
    return x


def rope_motion(input_path:str, nb_of_knots:int) -> int:
    """
    Simulates the movement of a rope's knots and sums the number of positions
    visited by the tail.
    """
    knots = []

    for _ in range(nb_of_knots):
        knots.append([STARTING_POSITION[X], STARTING_POSITION[Y]])

    rope_grid = []

    for _ in range(GRID_HEIGHT):
        rope_grid.append([0 for x in range(GRID_LENGTH)])
    
    rope_grid[STARTING_POSITION[X]][STARTING_POSITION[Y]] = VISITED_FLAG

    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file:
            line_contents = line.split()
            direction = line_contents[DIRECTION]
            nb_of_steps = int(line_contents[NUMBER_OF_STEPS])

            for _ in range(nb_of_steps):
                # head movement
                if direction == UP:
                    knots[HEAD][X] -= 1
                elif direction == DOWN:
                    knots[HEAD][X] += 1
                elif direction == LEFT:
                    knots[HEAD][Y] -= 1
                else: #direction == RIGHT
                    knots[HEAD][Y] += 1
                
                #knots following movement
                for i in range(1,nb_of_knots):
                    x_diff = knots[i-1][X] - knots[i][X]
                    y_diff = knots[i-1][Y] - knots[i][Y]

                    if x_diff == -2: 
                        knots[i][X] -= 1
                        knots[i][Y] += clamp(y_diff)
                    elif x_diff == 2: 
                        knots[i][X] += 1
                        knots[i][Y] += clamp(y_diff)
                    elif y_diff == -2: 
                        knots[i][X] += clamp(x_diff)
                        knots[i][Y] -= 1
                    elif y_diff == 2: 
                        knots[i][X] += clamp(x_diff)
                        knots[i][Y] += 1
                    
                rope_grid[knots[nb_of_knots-1][X]][knots[nb_of_knots-1][Y]] = VISITED_FLAG
                
    sum_grid = 0
    for row in rope_grid:
        sum_grid += sum(row)
    return sum_grid
            

if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day9.txt")
    print(f"Number of positions visited by the 2 knots rope's tail : {rope_motion(path, 2)}")
    print(f"Number of positions visited by the 10 knots rope's tail : {rope_motion(path, 10)}")