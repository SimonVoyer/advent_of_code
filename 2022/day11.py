import os, copy, numpy as np


class Monkey:
    """
    Represents a monkey capable of doing some monkey business.
    """

    OLD = "old"
    ADD = "+"
    MULTIPLY = "*"
    DTYPE = np.uint64

    def __init__(self, items, ops, divisible_test, true_target, false_target) -> None:
        self.items = items
        self.ops = ops
        self.divisor = divisible_test
        self.true_target = true_target
        self.false_target = false_target
        self.inspection_count = 0


    def operation(self) -> int:
        """
        Applies the monkey's favorite operation to the item's worry level.
        """
        if self.ops[0] == Monkey.OLD:
            op1 = np.array([self.items], dtype=Monkey.DTYPE)
        else:
            op1 = np.full(len(self.items), int(self.ops[0]), dtype=Monkey.DTYPE)

        if self.ops[2] == Monkey.OLD:
            op3 = np.array([self.items], dtype=Monkey.DTYPE)
        else:
            op3 = np.full(len(self.items), int(self.ops[2]), dtype=Monkey.DTYPE)
        
        if self.ops[1] == Monkey.ADD:
            result = np.add(op1, op3, dtype=Monkey.DTYPE)
        else:
            result = np.multiply(op1,op3,dtype=Monkey.DTYPE)

        return result


    def target(self, value:int) -> int:
        """
        Determines the next target based on the monkey's favorite prime divisor.
        """
        if value % self.divisor == 0:
            target = self.true_target
        else :
            target = self.false_target
            
        return target


def generate_monkeys(input_path:str) -> list:
    """
    Generates the monkeys based on the input file.
    """
    monkeys = []
    with open(input_path, 'r', encoding="utf-8") as file:
        
        line1 = next(file, None)
        line2 = next(file, None)
        line3 = next(file, None)
        line4 = next(file, None)
        line5 = next(file, None)
        line6 = next(file, None)
        next(file, None)

        while (line1):
            starting_items = [int(x) for x in line2.replace(',', '').split()[2::]]
            ops = line3.split()[3::]
            divisible_test = int(line4.split()[3])
            true_target  = int(line5.split()[5])
            false_target  = int(line6.split()[5])
            monkeys.append(Monkey(starting_items, ops, divisible_test, true_target, false_target))

            line1 = next(file, None)
            line2 = next(file, None)
            line3 = next(file, None)
            line4 = next(file, None)
            line5 = next(file, None)
            line6 = next(file, None)
            next(file, None)
    return monkeys


def monkey_business(monkeys:list, rounds:int, is_very_worried:bool) -> int:
    """
    Process of monkeys doing some monkey business. Returns the multiple of the 
    2 highest numbers of total operations performed by the monkeys.
    """
    if is_very_worried:
        lcm = np.lcm.reduce([monkey.divisor for monkey in monkeys])
    for _ in range(1,rounds+1):
        for i in range(len(monkeys)):
            items = monkeys[i].operation()
            if not is_very_worried:
                divisor = np.full(len(items), 3.0, dtype=Monkey.DTYPE)
                items = np.floor_divide(items, divisor, dtype=Monkey.DTYPE)
            else:
                #based on https://aoc.just2good.co.uk/2022/11
                divisor = np.full(len(items), lcm, dtype=Monkey.DTYPE)
                items = np.remainder(items, divisor, dtype=Monkey.DTYPE)
            monkeys[i].inspection_count += len(monkeys[i].items)
            monkeys[i].items.clear()
            
            for j in range( len(items[0])):
                item = items[0][j]
                target = monkeys[i].target(item)
                monkeys[target].items.append(item)
                
    inspection_counts = [x.inspection_count for x in monkeys]
    inspection_counts.sort(reverse=True) 
    return inspection_counts[0] * inspection_counts[1]


if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day11.txt")
    monkeys = generate_monkeys(path)
    print(f"Monkey business level while worrying is under control = {monkey_business(copy.deepcopy(monkeys), 20, False)}")
    print(f"Monkey business level while worrying is not under control = {monkey_business(copy.deepcopy(monkeys), 10000, True)}")
