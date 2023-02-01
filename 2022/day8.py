import os

def count_visible_trees(input_path:str) -> int :
    """
    Counts the number of trees that are not hidden by a higher tree from at least one of
    the four cardinal points.
    """
    visible_trees_count = 0
    forest = []
    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file :
            tree_row = list(line)
            tree_row.remove('\n')
            tree_row = [int(x) for x in tree_row]
            forest.append(tree_row)
    
    #initialize a grid that will flag visible trees
    is_visible = []
    size = len(forest) #forest is a square grid
    for i in range(size):
        is_visible.append([0 for x in range(size)])

    for i in range(size):
        max_west_height = -1
        max_east_height = -1
        max_north_height = -1
        max_south_height = -1

        for j in range(size):
            west_tree = forest[i][j]
            east_col_index = size-(j+1)
            east_tree = forest[i][east_col_index]
            north_tree = forest[j][i]
            south_row_index = size-(j+1)
            south_tree = forest[south_row_index][i]

            if west_tree > max_west_height:
                max_west_height = west_tree
                is_visible[i][j] = 1
            
            if east_tree > max_east_height:
                max_east_height = east_tree
                is_visible[i][east_col_index] = 1

            if north_tree > max_north_height:
                max_north_height = north_tree
                is_visible[j][i] = 1
            
            if south_tree > max_south_height:
                max_south_height = south_tree
                is_visible[south_row_index][i] = 1

    for row in is_visible:
        visible_trees_count += sum(row)
    return visible_trees_count


def most_scenic_view(input_path:str) -> int :
    """
    Finds the most scenic view which is defined as the tree from which the most trees 
    can be seen from 
    """
    forest = []
    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file :
            tree_row = list(line)
            tree_row.remove('\n')
            tree_row = [int(x) for x in tree_row]
            forest.append(tree_row)

    size = len(forest) #forest is a square grid
    max_scenic_view = 0
    
    for i in range(size):
        for j in range(size):
            tree = forest[i][j]

            west_scenic_value = 0
            west_blocked = False
            east_scenic_value = 0
            east_blocked = False
            north_scenic_value = 0
            north_blocked = False
            south_scenic_value = 0
            south_blocked = False

            for k in range(1,size):
                west_col_index = j-k
                east_col_index = j+k
                north_row_index = i-k
                south_row_index = i+k
                
                if not west_blocked :
                    if  0 <= west_col_index <= size-1:
                        west_scenic_value = k
                        if forest[i][west_col_index] >= tree:
                            west_blocked = True
                    else :
                        west_blocked = True

                if not east_blocked :
                    if  0 <= east_col_index <= size-1:
                        east_scenic_value = k
                        if forest[i][east_col_index] >= tree:
                            east_blocked = True
                    else :
                        east_blocked = True

                if not north_blocked :
                    if  0 <= north_row_index <= size-1:
                        north_scenic_value = k
                        if forest[north_row_index][j] >= tree:
                            north_blocked = True
                    else :
                        north_blocked = True
                
                if not south_blocked :
                    if  0 <= south_row_index <= size-1:
                        south_scenic_value = k
                        if forest[south_row_index][j] >= tree:
                            south_blocked = True
                    else :
                        south_blocked = True

                scenic_value = west_scenic_value * east_scenic_value * north_scenic_value * south_scenic_value
                if scenic_value > max_scenic_view:
                    max_scenic_view = scenic_value
    return max_scenic_view


def forest_aerial_mapping(input_path:str) -> int :
    """
    Combines both previous functions to avoid iterating twice over the same trees
    but this makes it less readable.
    """
    visible_trees_count = 0
    max_scenic_view = 0
    forest = []
    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file :
            tree_row = list(line)
            tree_row.remove('\n')
            tree_row = [int(x) for x in tree_row]
            forest.append(tree_row)
    
    #initialize a grid that will flag visible trees
    is_visible = []
    size = len(forest) #forest is a square grid
    for i in range(size):
        is_visible.append([0 for x in range(size)])

    for i in range(size):
        max_west_height = -1
        max_east_height = -1
        max_north_height = -1
        max_south_height = -1

        for j in range(size):
            west_tree = forest[i][j]
            east_col_index = size-(j+1)
            east_tree = forest[i][east_col_index]
            north_tree = forest[j][i]
            south_row_index = size-(j+1)
            south_tree = forest[south_row_index][i]

            if west_tree > max_west_height:
                max_west_height = west_tree
                is_visible[i][j] = 1
            
            if east_tree > max_east_height:
                max_east_height = east_tree
                is_visible[i][east_col_index] = 1

            if north_tree > max_north_height:
                max_north_height = north_tree
                is_visible[j][i] = 1
            
            if south_tree > max_south_height:
                max_south_height = south_tree
                is_visible[south_row_index][i] = 1

            tree = forest[i][j]
            west_scenic_value = 0
            west_blocked = False
            east_scenic_value = 0
            east_blocked = False
            north_scenic_value = 0
            north_blocked = False
            south_scenic_value = 0
            south_blocked = False

            #traverse all 4 directions and find the scenic values
            for k in range(1,size):
                west_col_index = j-k
                east_col_index = j+k
                north_row_index = i-k
                south_row_index = i+k
                
                if not west_blocked :
                    if  0 <= west_col_index <= size-1:
                        west_scenic_value = k
                        if forest[i][west_col_index] >= tree:
                            west_blocked = True
                    else :
                        west_blocked = True

                if not east_blocked :
                    if  0 <= east_col_index <= size-1:
                        east_scenic_value = k
                        if forest[i][east_col_index] >= tree:
                            east_blocked = True
                    else :
                        east_blocked = True

                if not north_blocked :
                    if  0 <= north_row_index <= size-1:
                        north_scenic_value = k
                        if forest[north_row_index][j] >= tree:
                            north_blocked = True
                    else :
                        north_blocked = True
                
                if not south_blocked :
                    if  0 <= south_row_index <= size-1:
                        south_scenic_value = k
                        if forest[south_row_index][j] >= tree:
                            south_blocked = True
                    else :
                        south_blocked = True
                scenic_value = west_scenic_value * east_scenic_value * north_scenic_value * south_scenic_value
                if scenic_value > max_scenic_view:
                    max_scenic_view = scenic_value

    for row in is_visible:
        visible_trees_count += sum(row)
    return (visible_trees_count, max_scenic_view)
    

if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day8.txt")
    aerial_mapping = forest_aerial_mapping(path)
    print(f"Number of visible trees : {aerial_mapping[0]} and most scenic view value : {aerial_mapping[1]}.")