import os


def detect_marker(input_path:str, unique_count:int) -> int:
    """
    Returns the position of the marker which is placed after the first 
    sequence of n unique characters where parameter unique_count corresponds to n.
    """
    with open(input_path, 'r', encoding="utf-8") as file:
        signal = file.readline()
    
    start_pointer = 0
    marker_found = False
    while start_pointer+unique_count < len(signal) and not marker_found:
        subsignal = signal[start_pointer:start_pointer+unique_count]
        if len(set(subsignal)) != unique_count:
            start_pointer += 1
        else :
            marker_found = True
    return start_pointer+unique_count


def detect_marker_v2(input_path:str, unique_count:int) -> int:
    """
    Returns the position of the marker which is placed after the first 
    sequence of n unique characters where parameter unique_count corresponds to n.
    """
    with open(input_path, 'r', encoding="utf-8") as file:
        signal = file.readline()

    start_pointer = 0
    character_indices = {}
    marker_found = False

    while start_pointer+unique_count < len(signal) and not marker_found:
        for current_pointer in range(start_pointer, start_pointer+unique_count):
            character = signal[current_pointer]
            if character not in character_indices:
                character_indices[character] = current_pointer
                if len(character_indices) == unique_count:
                    marker_found = True
            else :
                start_pointer = character_indices[character] + 1
                character_indices.clear()
                break
    return start_pointer+unique_count


if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day6.txt")
    print(f"Start-of-packet marker is at position : {detect_marker(path, 4)}.")
    print(f"Start-of-message marker is at position : {detect_marker(path, 14)}.")
    