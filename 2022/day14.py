import os, copy


LINE_SEP = "->"
ROCK_VALUE = 1
SAND_VALUE = 2

PATH_ROW = 1
PATH_COL = 0

FLOOR_DELTA = 2


def generate_cave(input_path:str, cave:dict) -> int:
    """
    Generates a cave from the input file.
    """
    #place the rocks
    highest_point = 0
    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file:
            paths = line.replace(' ', '').replace('\n', '').split(LINE_SEP)
            paths = [x.split(',') for x in paths]
            for path in paths:
                for i in range(len(path)):
                    path[i] = int(path[i])
            
            for i in range(len(paths)-1):
                from_point = paths[i]
                from_row = from_point[PATH_ROW]
                from_col = from_point[PATH_COL]

                to_point = paths[i+1]
                to_row = to_point[PATH_ROW]
                to_col = to_point[PATH_COL]

                if to_row > highest_point:
                    highest_point = to_row
                if from_row > highest_point:
                    highest_point = from_row

                if to_row > from_row:
                    for i in range(to_row-from_row+1):
                        cave[(from_row+i,from_col)] = ROCK_VALUE
                elif from_row > to_row:
                    for i in range(from_row-to_row+1):
                        cave[(to_row+i,from_col)] = ROCK_VALUE
                elif to_col > from_col:
                    for i in range(to_col-from_col+1):
                        cave[(from_row, from_col+i)] = ROCK_VALUE
                elif from_col > to_col:
                    for i in range(from_col-to_col+1):
                        cave[(from_row, to_col+i)] = ROCK_VALUE
    return highest_point


def sandfall(cave:dict, floor_height:int, sand_row:int, sand_col:int, has_floor:bool) -> int:
    """
    Simulates falling sand within the cave. If has_floor is false, we ignore the floor.
    """
    sand_count = 0
    sand_fell_through = False
    sand_blocked = False
    while not sand_fell_through and not sand_blocked:
        row = sand_row
        col = sand_col

        for _ in range(floor_height):
            row_below = row+1
            if row_below >= floor_height and not has_floor:
                sand_fell_through = True
                break

            col_left = col-1
            col_right = col+1

            reached_floor = has_floor and row_below >= floor_height
            below_blocked = (row_below,col) in cave
            left_blocked = (row_below,col_left) in cave 
            right_blocked = (row_below,col_right) in cave

            if not below_blocked and not reached_floor:
                #fall straight down
                row += 1
            elif not left_blocked and not reached_floor:
                #below is blocked but down-left isn't, go down that way
                row += 1
                col -= 1
            elif not right_blocked and not reached_floor:
                #below and left are blocked but down-right isn't, go down that way
                row +=1
                col +=1
            else:
                #all three paths are blocked, sand rests there
                sand_count += 1
                cave[(row,col)] = SAND_VALUE
                if row == sand_row and col == sand_col:
                    sand_blocked = True
                break
    return sand_count


if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day14.txt")
    cave = {}
    floor_height = generate_cave(path, cave) + FLOOR_DELTA
    sand_count = sandfall(cave, floor_height, 0, 500, False)
    print(f"Sand count without accounting for the floor : {sand_count}")
    sand_count += sandfall(cave, floor_height, 0, 500, True)
    print(f"Sand count after accounting for the floor : {sand_count}")