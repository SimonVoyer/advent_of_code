import os

spelled_digits = {
    "one":"o1ne",
    "two":"tw2o",
    "three":"thr3ee",
    "four":"fo4ur",
    "five":"fiv5e",
    "six":"six6",
    "seven":"se7en",
    "eight":"eig8ht",
    "nine":"ni9ne",
}

def get_calibration_value(line):
    digits = ''.join(char for char in line if char.isdigit())
    return int(digits[0]+digits[-1])

def insert_digits(line):
    digit_line = line
    for key in spelled_digits.keys():
        digit_line = digit_line.replace(key, spelled_digits[key])
    return digit_line

def sum_calibration_values1(path):
    sum = 0
    with open(path, 'r', encoding="utf-8") as file:
        for line in file:
            sum += get_calibration_value(line)
    return sum

def sum_calibration_values2(path):
    sum = 0
    with open(path, 'r', encoding="utf-8") as file:
        for line in file:
            sum += get_calibration_value(insert_digits(line))
    return sum

if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "input1.txt") 
    print(f"Sum of calibration values: {sum_calibration_values1(path)}")
    print(f"Sum of calibration values: {sum_calibration_values2(path)}")