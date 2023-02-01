import os, collections

#analyzing the input reveals a few interesting constants we can save and a function to calculate the box ids' positions

STACK_DESCRIPTION_END = 8 #drawing of stacks go from lines 1 to 8
NB_OF_STACKS = 9
NB_TO_MOVE_INDEX = 1
SOURCE_BOX_INDEX = 3
DESTINATION_BOX_INDEX = 5


def box_id_position(stack_nb:int):
    """
    Position of box id : 1=2, 2=6, 3=10 => 2+(n-1)*4, then remove 1 to get the actual index => 1+(n-1)*4
    """
    return 1+(stack_nb-1)*4


def crane_stacking_process(input_path:str, is_mark_9000=True)-> str:
    """
    Stacks crates according to the process used by the crane and returns the joined character ids of the top boxes.
    M9000 stacks boxes 1 by 1 and M9001 stacks them by group, thus the end order varies.
    """
    stacks = [collections.deque() for _ in range(NB_OF_STACKS)]
    stacks.insert(0,None) #so we can deal directly with indexes 1 to 9
    
    with open(input_path, 'r', encoding="utf-8") as file:
        stacks_content = collections.deque()

        #get the contents of the stacks in line format
        for _ in range(STACK_DESCRIPTION_END):
            stacks_content.append(file.readline())

        #get the ids from boxes into corresponding stacks
        for _ in range(len(stacks_content)):
            content = stacks_content.pop()
            for i in range(1,NB_OF_STACKS+1):
                id_position = box_id_position(i)
                id = content[id_position]
                if id != ' ':
                    stacks[i].append(id)

        #analyzing the input reveals that the next 2 lines don't have any valuable information other than the stacks are ordered 1-9
        file.readline()
        file.readline()

        #the following lines detail how to move the boxes

        if not is_mark_9000:
            temp = collections.deque()

        for line in file:
            line_content = line.split()
            nb_to_move = int(line_content[NB_TO_MOVE_INDEX])
            source_stack = int(line_content[SOURCE_BOX_INDEX])
            destination_stack = int(line_content[DESTINATION_BOX_INDEX])

            if is_mark_9000: #CrateMover9000 puts them 1 by 1 so it behaves exactly like pushing on a stack
                for _ in range(nb_to_move):
                    stacks[destination_stack].append(stacks[source_stack].pop())
            else : #CrateMover9001 puts them by groups so we can reuse the same logic by simply reversing an intermediary stack
                for _ in range(nb_to_move):
                    temp.append(stacks[source_stack].pop())
                for _ in range(nb_to_move):
                    stacks[destination_stack].append(temp.pop())
    return "".join([x.pop() for x in stacks if x is not None])


if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day5.txt")
    print(f"Ids of the boxes on top of the stacks using CraneMover9000 : {crane_stacking_process(path)}.")
    print(f"Ids of the boxes on top of the stacks using CraneMover9001 : {crane_stacking_process(path, False)}.")
    
   
    