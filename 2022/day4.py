import os


def camp_cleanup_complete_overlap(input_path:str) -> int :
    """
    Counts the number of times one cleanup duty roster fully contains the other in a pair.
    The roster pair takes the form of W-X,Y-Z, where W, X, Y, and Z are natural numbers
    """
    overlaps = 0
    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file:
            assignment1, assignment2 = line.split(',')
            lower_bound1, upper_bound1 = assignment1.split('-')
            lower_bound2, upper_bound2 = assignment2.split('-')

            lower_bound1 = int(lower_bound1)
            lower_bound2 = int(lower_bound2)
            upper_bound1 = int(upper_bound1)
            upper_bound2 = int(upper_bound2)

            is_1_contains_2 = lower_bound2 >= lower_bound1 and upper_bound2 <= upper_bound1
            is_2_contains_1 = lower_bound1 >= lower_bound2 and upper_bound1 <= upper_bound2
            if is_1_contains_2 or is_2_contains_1 :
                overlaps += 1

    return overlaps


def camp_cleanup_partial_overlap(input_path:str) -> int :
    """
    Counts the number of times one cleanup duty roster overlaps the other in a pair.
    The roster pair takes the form of W-X,Y-Z, where W, X, Y, and Z are natural numbers
    """
    overlaps = 0
    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file:
            assignment1, assignment2 = line.split(',')
            lower_bound1, upper_bound1 = assignment1.split('-')
            lower_bound2, upper_bound2 = assignment2.split('-')

            lower_bound1 = int(lower_bound1)
            lower_bound2 = int(lower_bound2)
            upper_bound1 = int(upper_bound1)
            upper_bound2 = int(upper_bound2)

            is_1_overlaps_2 = lower_bound1 <=lower_bound2 <= upper_bound1 or lower_bound1 <=upper_bound2 <= upper_bound1
            is_2_overlaps_1 = lower_bound2 <=lower_bound1 <= upper_bound2 or lower_bound2 <=upper_bound1 <= upper_bound2
            if is_1_overlaps_2 or is_2_overlaps_1:
                overlaps+=1

    return overlaps


if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day4.txt")
    print(f"Number of complete cleanup duty pair overlaps : {camp_cleanup_complete_overlap(path)}.")
    print(f"Number of partial cleanup duty pair overlaps : {camp_cleanup_partial_overlap(path)}.")
    