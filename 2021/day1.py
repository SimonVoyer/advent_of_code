import os

def sonar_depth_increase(input_path:str) -> int:
    increase_count = -1
    previous_depth = 0
    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file:
            depth = int(line)
            if depth > previous_depth:
                increase_count += 1
            previous_depth = depth
    return increase_count

def sonar_window_increase(input_path:str) -> int:
    increase_count = -1
    previous_depth = 0
    depths = [[],[]]
    with open(input_path, 'r', encoding="utf-8") as file:
        depth1 = int(file.readline())
        depth2 = int(file.readline())

        depths[0].append(depth1)
        depths[0].append(depth2)
        depths[1].append(depth2)

        for line in file:
            depths.append([])
            depth = int(line)
            for i in range(len(depths)):
                depths[i].append(depth)
            
            sum_depths = sum(depths[0])
            if sum_depths > previous_depth:
                increase_count += 1
            previous_depth = sum_depths
            del depths[0]
            
    return increase_count
            

if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day1.txt")
    print(f"Sonar depth increased {sonar_depth_increase(path)} times.")
    print(f"Sonar depth window increased {sonar_window_increase(path)} times.")