import os, functools, copy


START = '['
END = ']'
TEN = '10'
STAR = '*'

DIVIDER_PACKET1 = [[2]]
DIVIDER_PACKET2 = [[6]]


def compare_lists(list1:list, list2:list) -> int :
    """
    Signum function that recursively compares two lists according to the elven distress protocol.
    """
    list1 = copy.deepcopy(list1)
    list2 = copy.deepcopy(list2)
    comparison = 0
    size1 = len(list1)
    size2 = len(list2)
    if size1 == 0 and size2 > 0:
        comparison = -1
    elif size1 > 0 and size2 == 0:
        comparison = 1
    elif list1 != list2: #comparison stays 0 if both lists are equal
        while list1 and list2 and comparison == 0:
            val1 = list1.pop(0)
            is_list1 = type(val1) is list
            val2 = list2.pop(0)
            is_list2 = type(val2) is list
            if not is_list1 and not is_list2:
                if val1 < val2:
                    comparison = -1
                elif val1 > val2:
                    comparison = 1
            elif is_list1 and is_list2:
                comparison = compare_lists(val1, val2)
            elif is_list1:
                comparison = compare_lists(val1, [val2])
            else:
                comparison = compare_lists([val1], val2)
        #once we've gone through the lists, we need to do one last comparison
        #in case both were almost the same but one of them had one fewer character
        if comparison == 0:
            size1 = len(list1)
            size2 = len(list2)
            if size1 < size2:
                comparison = -1
            elif size1 > size2:
                comparison = 1
    return comparison


def decode_distress_signal(input_path:str) -> None:
    """
    Decodes the distress signal according to the elven distress protocol. 
    """
    sum_indexes = 0
    index = 1
    packets = [DIVIDER_PACKET1, DIVIDER_PACKET2]
    with open(input_path, 'r', encoding="utf-8") as file:
        line1 = next(file, None)
        line2 = next(file, None)
        while line1:
            packet1 = to_packet(line1)
            packet2 = to_packet(line2)
            packets.append(packet1)
            packets.append(packet2)
            
            comparison = compare_lists(packet1, packet2)
            if comparison == -1:
                sum_indexes += index
            
            index +=1
            next(file, None)
            line1 = next(file, None)
            line2 = next(file, None)
    print(f"Sum of indexes where packets are in the right order : {sum_indexes}.")
    packets.sort(key=functools.cmp_to_key(compare_lists))
    decoder = (packets.index(DIVIDER_PACKET1) + 1) * (packets.index(DIVIDER_PACKET2) + 1)
    print(f"Decoder key for the distress signal : {decoder}.")


def to_packet(line:str) -> list :
    """
    Turns a line of text into the corresponding packet.
    """
    packet = []
    #since 10 is the only two digit number, we can replace it in the raw input
    #to make the parsing easier, then it will be reconverted to 10
    raw_packet = list(line.replace(',' , '').replace('\n', '').replace(TEN,STAR))[1:-1]
    lists = []
    current_list = None
    for i in range(len(raw_packet)):
        char = raw_packet[i]

        if char == START:
            if current_list is None:
                current_list = []
            else:
                lists.append(current_list) 
                current_list = []
        elif char == END:
            if len(lists) > 0:
                lists[-1].append(current_list)
                current_list = lists.pop()
            else:
                packet.append(current_list)
                current_list = None
        else:
            if char == STAR:
                char = TEN
            if current_list is not None:
                current_list.append(int(char))
            else :
                packet.append(int(char))
    return packet
            

if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day13.txt")
    decode_distress_signal(path)