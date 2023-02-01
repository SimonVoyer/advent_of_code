import os, heapq


def elf_snacks_caloric_content(input_path:str, n=3) -> int:
    """
    Sums the total calories carried by each elf, and then returns the sum of the n highest values.
    """
    calories = []
    calory_counter = 0
    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file:
            if line.rstrip().lstrip().isnumeric():
                calory_counter += int(line)
            else:
                #the heap keeps the calories sorted and we can return the n highest calory counts
                heapq.heappush(calories, calory_counter)
                calory_counter = 0
    return sum(heapq.nlargest(n, calories))


if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day1.txt")
    print(f"Total calories found within the snacks of the elf carrying the most calories : {elf_snacks_caloric_content(path,1)}.")
    print(f"Total calories found within the snacks of the three elves carrying the most calories : {elf_snacks_caloric_content(path)}.")