import os


NB_OF_FLAGS = 52 


def item_to_priority(x):
    """
    Priorities for each item : a-z == 1-26, A-Z == 27-52.
    """
    return x - 96 if x >= 97 else x-38


def find_misplaced_items(input_path) -> int:
    """
    Sums the priority value of misplaced items, which corresponds to an item that appears in both compartments of an elf's rucksack.
    """
    with open(input_path, 'r', encoding="utf-8") as file:
        priority_sum = 0
        for line in file:
            rucksack_length = int(len(line)/2)
            compartment1 = line[0:rucksack_length]
            compartment2 = line[rucksack_length::]
            
            priority = -1
            flags = [None]
            for _ in range(NB_OF_FLAGS):
                flags.append(0)
        
            #we set the flag to 1 for each character
            for char in compartment1:
                ascii_value = ord(char)
                flags[item_to_priority(ascii_value)] = 1

            #a char that is found and was flagged means it's in both compartments of the rucksack
            for char in compartment2:
                ascii_value = ord(char)
                priority = item_to_priority(ascii_value)
                if flags[priority]:
                    break
            
            priority_sum += priority
        return priority_sum


def find_elf_trio_badge(input_path:str) -> int:
    """
    Sums the priority value of the item shared by each trio of elf (badge), where the first trio would be 1 to 3 and nth trio would be (n*3-2) to (n*3) .
    """
    with open(input_path, 'r', encoding="utf-8") as file:
        priority_sum = 0
        next_line = next(file)

        #this assumes the number of lines is a multiple of 3, which would make the problem nonsensical otherwise
        while (next_line):
            line1 = next_line
            line2 = next(file)
            line3 = next(file)

            priority = -1
            flags = [None]
            for _ in range(NB_OF_FLAGS):
                flags.append(0)

            #we set the flag to 1 for each character
            for char in line1:
                ascii_value = ord(char)
                flags[item_to_priority(ascii_value)] = 1

            #if the char was already flagged, we flag it with 2
            for char in line2:
                ascii_value = ord(char)
                priority = item_to_priority(ascii_value)
                if flags[priority]:
                    flags[priority] = 2

            #a character that is found and was flagged with 2 means it's shared by the three elves
            for char in line3:
                ascii_value = ord(char)
                priority = item_to_priority(ascii_value)
                if flags[priority] == 2:
                    break

            priority_sum += priority
            next_line = next(file, None)
        return priority_sum


if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day3.txt")
    print(f"Sum of the priority value of the misplaced items in the rucksacks : {find_misplaced_items(path)}.")
    print(f"Sum of the priority value of each elf trio's badge : {find_elf_trio_badge(path)}.")