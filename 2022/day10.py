import os, queue


ADD = "addx"
NOOP = "noop"

CRT_LENGTH = 40
CRT_HEIGHT = 6

LIT = '#'
DARK = '.'

KEY_CYCLES =  [20,60,100,140,180,220]


def emulate_video_system(input_path:str) -> None:
    """
    Analyses the signal (and its strenght) sent to the cpu by the clock circuit and draw pixels
    according to the signal.
    """
    instruction_queue = queue.Queue()
    
    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file:
            #noop is treated as a 0 adding instruction
            instruction_queue.put(0) # since adding takes letter cycle, we simulate it by adding a noop before
            instructions = line.split()
            if instructions[0] == ADD:
                instruction_queue.put(int(instructions[1]))

    register_X = 1
    signal_strenght = 0
    CRT = []

    for _ in range(CRT_HEIGHT):
        CRT.append([DARK for _ in range(CRT_LENGTH)])

    for i in range(1, instruction_queue.qsize()+1):
        if i in KEY_CYCLES:
            signal_strenght += i * register_X
        
        #draw a lit pixel if register x equals the col position or +-1 of col position
        position = (i-1)
        row_position = position // CRT_LENGTH
        col_position = position % CRT_LENGTH
        if col_position - 1 <= register_X <= col_position + 1:
            CRT[row_position][col_position] = LIT

        register_X += instruction_queue.get()

    print(f"Signal strenght is {signal_strenght}.\n\nCRT display :")
    for row in CRT:
        for pixel in row:
            print(pixel, end='')
        print('\n')


if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day10.txt")
    emulate_video_system(path)
