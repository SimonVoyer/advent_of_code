import os

COMMAND = '$'
CHANGE_DIRECTORY = "cd"
ROOT = '/'
PARENT_DIRECTORY = '..'
DIRECTORY = "dir"

TOTAL_SPACE = 70000000
SPACE_NEEDED = 30000000


class Directory:
    """
    Represents a simplified directory subtree.
    """

    def __init__(self, parent_directory, name):
        self.parent_directory = parent_directory 
        self.name = name
        self.subdirectories = {}
        self.files = {}
        self.size = 0


    def calculate_size(self, sizes:list) -> int:
        """
        Recursively sums the size of the directory subtree.
        The sizes parameter is filled and can be used for other calculations.
        """
        for file in self.files:
            self.size += self.files[file]
        
        if len(self.subdirectories) > 0 :
            for subdirectory in self.subdirectories:
                self.size += self.subdirectories[subdirectory].calculate_size(sizes)
        
        sizes.append(self.size)
        
        return self.size
          

def generate_dir_structure(input_path:str) -> Directory :
    """
    Generates the file structure from the input and returns the root.
    """
    root = Directory(None, ROOT)
    current_directory = None
    with open(input_path, 'r', encoding="utf-8") as file:

        for line in file:
            split_line = line.split()

            # branch according to the type of entry : command, listed directory or listed file

            if split_line[0] == COMMAND:
                if split_line[1] == CHANGE_DIRECTORY:
                    if split_line[2] == ROOT:
                        current_directory = root
                    elif split_line[2] == PARENT_DIRECTORY:
                        current_directory = current_directory.parent_directory
                    else:
                        current_directory = current_directory.subdirectories[split_line[2]]
            elif split_line[0] == DIRECTORY:
                new_directory = split_line[1]   
                if new_directory not in current_directory.subdirectories:
                    current_directory.subdirectories[new_directory] = Directory(current_directory, new_directory)
            else:
                file_size = split_line[0]
                file_name = split_line[1]
                if file_name not in current_directory.files:
                    current_directory.files[file_name] = int(file_size)

    return root


def sum_below_threshold(sizes:list, threshold:int) -> int :
    """
    Sums the values in the sizes parameter that are below the threshold parameter.
    """
    sizes_below_threshold = [x for x in sizes if x < threshold]
    return sum(sizes_below_threshold)


def delete_optimal_dir(sizes:list, root:Directory) -> int :
    """
    Returns the size of the optimal directory to delete.
    """
    available_space = TOTAL_SPACE - root.size
    space_to_free =  SPACE_NEEDED - available_space
    candidate_sizes = [x for x in sizes if x >= space_to_free]
    candidate_sizes.sort()
    return candidate_sizes[0]


if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day7.txt")

    root = generate_dir_structure(path)
    sizes = []
    root.calculate_size(sizes)

    print(f"Sum of directory sizes of at most 100000 : {sum_below_threshold(sizes, 100000)}.")
    print(f"Size of the directory to be deleted : {delete_optimal_dir(sizes, root)}.")
