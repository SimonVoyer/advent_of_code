import os, copy

ONE = '1'
ZERO = '0'
NB_BITS = 12

def submarine_power(input_path:str) -> int:
    gamma_bits = ['0' for _ in range(NB_BITS)]
    epsilon_bits = ['0' for _ in range(NB_BITS)]
    bit_0_count = [0 for _ in range(NB_BITS)]
    nb_of_packets = 0
    
    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file:
            nb_of_packets += 1
            bits = list(line)
            for i in range(len(bits)):
                if bits[i]==ZERO:
                    bit_0_count[i] += 1
    
    for i in range(len(bit_0_count)):
        if bit_0_count[i] < nb_of_packets / 2:
            gamma_bits[i] = ONE
        else:
            epsilon_bits[i] = ONE
    gamma_value = int("".join([x for x in gamma_bits]), 2)
    epsilon_value = int("".join([x for x in epsilon_bits]), 2)
    return gamma_value * epsilon_value


def split_by_bit(initial_bits:list, bit_position:int, is_oxygen:bool) -> list :
    bit_split = [[],[]]
    for bits in initial_bits:
        if bits[bit_position] == ZERO:
            bit_split[0].append(bits)
        else:
            bit_split[1].append(bits)
    
    nb_0s = len(bit_split[0])
    nb_1s = len(bit_split[1])

    if is_oxygen :
        remainder = bit_split[1] if nb_1s >= nb_0s else bit_split[0]
    else:
        remainder = bit_split[0] if nb_0s <= nb_1s else bit_split[1]
    return remainder
    

def submarine_life_support(input_path:str) -> int:

    oxygen_bits = []
    co2_bits = []
    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file:
            bits = list(line)
            if bits[-1] == '\n':
                del bits[-1]
            oxygen_bits.append([x for x in bits])
            co2_bits.append([x for x in bits])

    bit_position = 0
    while len(oxygen_bits) > 1:
        oxygen_bits = split_by_bit(oxygen_bits, bit_position, True)
        bit_position +=1
    
    bit_position = 0
    while len(co2_bits) > 1:
        co2_bits = split_by_bit(co2_bits, bit_position, False)
        bit_position +=1

    oxygen_value = int("".join([x for x in oxygen_bits[0]]), 2)
    co2_value = int("".join([x for x in co2_bits[0]]), 2)
            
    return oxygen_value * co2_value
    

if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day3.txt")
    print(f"The submarine's power consumption is {submarine_power(path)}.")
    print(f"The submarine's life support rating is {submarine_life_support(path)}.")