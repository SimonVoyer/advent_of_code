import os, heapq

START_MARKER = 'S'
START_VALUE = 'a'
START_INDEX = 0

END_MARKER = 'E'
END_VALUE = 'z'
END_INDEX = 1

A_INDEX = 2



def generate_grid(input_path:str) -> list:
    """
    Generates a grid from the input file.
    """
    grid = []
    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file:
            row = list(line)
            if row[-1] == '\n':
                del row[-1]
            grid.append(row)
    return grid


def find_and_transform(grid:list) -> list:
    """
    Replaces the starting and ending points with their
    equivalent values and returns the positions of S, E and a.
    """
    positions = [None, None]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            value = grid[i][j]
            if value == START_MARKER:
                positions[START_INDEX] = (i,j)
                grid[i][j] = START_VALUE
            elif value == END_MARKER:
                positions[END_INDEX] = (i,j)
                grid[i][j] = END_VALUE
            elif value == START_VALUE:
                positions.append((i,j))
    return positions
            

def generate_graph(grid:list) -> dict:
    """
    Generate a graph where vertices are every position and edges are
    the valid path, where a path is valid if the character is at most 1
    value higher. For example, valid paths for c would be {a,b,c,d}.
    """
    graph = {}
    height = len(grid)
    width = len(grid[0])
    for i in range(height):
        for j in range(width):
            neighbors = []
            key = (i,j)
            value = ord(grid[i][j])

            up_i = i-1
            if up_i >= 0 and ord(grid[up_i][j]) - 1 <= value:
                neighbors.append((up_i, j))
            
            down_i = i+1
            if down_i < height and ord(grid[down_i][j]) - 1 <= value:
                neighbors.append((down_i, j))
            
            left_j = j-1
            if left_j >= 0 and ord(grid[i][left_j]) - 1 <= value:
                neighbors.append((i, left_j))
            
            right_j = j+1
            if right_j < width and ord(grid[i][right_j]) - 1 <= value:
                neighbors.append((i, right_j))

            graph[key] = neighbors
            
    return graph


def find_shortest_path(graph:dict, start_position:tuple, end_position:tuple) -> float:
    """
    Taken and adapted from https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
    Finds the shortest path between the starting position and the end position.
    """
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start_position] = 0.

    priority_queue = [(0., start_position)]
    while len(priority_queue) > 0:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        #this is necessary because the same vertex can be added more than
        #once to the priority queue
        if current_distance > distances[current_vertex]:
            continue
        
        #every neighbor is at a distance of 1 by definition
        for neighbor in graph[current_vertex]:
            distance = current_distance + 1.
        
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances[end_position]


def find_quickest_start(graph:dict, positions:list, shortest_distance=float("infinity")) -> float:
    """
    Iterates through the possible starting points and finds the one that would give
    the shortest path.
    """
    for i in range(A_INDEX, len(positions)):
        distance = find_shortest_path(graph, positions[i], positions[END_INDEX])
        if distance < shortest_distance:
            shortest_distance = distance
    return shortest_distance
        

if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day12.txt")
    grid = generate_grid(path)
    positions = find_and_transform(grid)
    graph= generate_graph(grid)
    distance_S = find_shortest_path(graph, positions[START_INDEX], positions[END_INDEX])
    print(f"Shortest distance from starting point S : {distance_S}.")
    print(f"Shortest distance from any starting point {find_quickest_start(graph, positions, distance_S)}")
