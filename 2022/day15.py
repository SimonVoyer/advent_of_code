import os


SENSOR_X = 2
SENSOR_Y = 3
BEACON_X = 8
BEACON_Y = 9

X = 0
Y = 1

SENSOR = 0
BEACON = 1
VOID = 2

UPPER_BOUND = 4000000


def parse_beacon_sensor_pairs(input_path:str) -> dict:
    """
    Returns the beacon-sensor pairs as parsed from the input file.
    """
    beacon_sensor_pairs = {}
    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file:
            tokens = line.split()
            sensor_x = int(tokens[SENSOR_X].replace("x=",'').replace(',',''))
            sensor_y = int(tokens[SENSOR_Y].replace("y=", '').replace(':',''))
            beacon_x = int(tokens[BEACON_X].replace("x=",'').replace(',',''))
            beacon_y = int(tokens[BEACON_Y].replace("y=", ''))
            beacon_sensor_pairs[(sensor_x,sensor_y)] = (beacon_x,beacon_y)
    return beacon_sensor_pairs


def detect_void(sensor:tuple, beacon:tuple, scan:set, y_target:int) -> None:
    """
    Detects positions where a beacon cannot be for a specific row in the scan.
    """
    x = sensor[X]
    y = sensor[Y]
    
    distance = abs(x-beacon[X]) + abs(y-beacon[Y])
    starting_row = y-distance
    ending_row = y+distance
    if starting_row <= y_target <= ending_row:
        y_distance = abs(y - y_target)
        col_distance = abs(distance - y_distance)
        left_col = x-col_distance
        right_col = x+col_distance

        for i in range(left_col,right_col+1):
            scan.add(i)


def count_nb_beacon_positions(beacon_sensor_pairs:dict, y_target:int) -> None:
    """
    Counts the nb of positions where a beacon cannot be.
    """
    scan = set()
    beacon_counter = 0
    for sensor in beacon_sensor_pairs:
        beacon = beacon_sensor_pairs[sensor]
        if beacon[Y] == y_target and beacon[X] not in scan:
            beacon_counter +=1
            scan.add(beacon[X])
    
    for sensor in beacon_sensor_pairs:
        detect_void(sensor, beacon_sensor_pairs[sensor], scan, y_target)

    print(f"Number of positions where a beacon cannot be present for y={y_target} : {len(scan) - beacon_counter}.")


class Block:
    """
    Represents a block within a certain Manhattan distance from the center.
    """

    def __init__(self, center_x:int, center_y:int, distance:int) -> None:
        self.center_x = center_x
        self.center_y = center_y
        self.distance = distance
    
    def jump(self, x:int, y:int) -> tuple:
        """
        Jumps to the next position outside of the block.
        """
        distance_x = abs(self.center_x-x)
        distance_y = abs(self.center_y-y)
        if  distance_x+distance_y <= self.distance:
            new_x = self.center_x + self.distance - distance_y + 1
            jump = (new_x, y) if new_x < UPPER_BOUND else (0,y+1)
        else:
            jump = (x,y)
        return jump


def find_distress_beacon(beacon_sensor_pairs:dict) -> None:
    """
    Finds the distress beacon. This solution is poorly optimized and takes roughly 30 seconds to complete.
    Jumping through the blocks allows to quickly pass through the x axis but there's no optimization
    for the y axis. 
    """
    blocks = []
    for sensor in beacon_sensor_pairs:
        x = sensor[X]
        y = sensor[Y]

        beacon = beacon_sensor_pairs[sensor]
        distance = abs(x-beacon[X]) + abs(y-beacon[Y])
        blocks.append(Block(x,y,distance))

    blocks.sort(key=lambda x: x.center_x)

    x = 0
    y = 0
    while x < UPPER_BOUND and y < UPPER_BOUND:
        old_x = x
        old_y = y
        for k in range(len(blocks)):
            block = blocks[k]
            jumped_to = block.jump(x,y)
            x = jumped_to[X]
            y = jumped_to[Y]
        
        if x == old_x and y == old_y:
            break
    print(f"Distress beacon tuning frequency : {x*UPPER_BOUND+y}.")


if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day15.txt")
    beacon_sensor_pairs = parse_beacon_sensor_pairs(path)
    count_nb_beacon_positions(beacon_sensor_pairs, y_target=2000000)
    find_distress_beacon(beacon_sensor_pairs)
    