from collections import defaultdict
import re


lines = []


def read_file():
    file = open("input.txt", "r")
    [lines.append(line.strip()) for line in file]
    file.close()


def populate_addresses():
    address_space = defaultdict(lambda: 0)
    mask, mask_set_ones, mask_set_zeroes = 0, 0, 0
    for line in lines:
        if line[:7] == "mask = ":
            mask = line[7:]
            mask_set_ones = int("".join(['1' if x == '1' else '0' for x in mask]), 2)
            mask_set_zeroes = int("".join(['0' if x == '0' else '1' for x in mask]), 2)
        else:
            address, value = [int(num) for num in re.findall("\d+", line)]
            address_space[address] = (value | mask_set_ones) & mask_set_zeroes

    return sum(address_space.values())


def floaty_populate_addresses():
    address_space = defaultdict(lambda: 0)
    mask, mask_set_ones, mask_set_zeroes, modifier_power_set = 0, 0, 0, []
    for line in lines:
        if line[:7] == "mask = ":
            mask = line[7:]
            mask_set_ones = int("".join(['1' if x == '1' else '0' for x in mask]), 2)
            mask_set_zeroes = int("".join(['0' if x == 'X' else '1' for x in mask]), 2)
            modifiers = [1 << (len(mask) - i - 1) for i in range(len(mask)) if mask[i] == 'X']
            modifier_power_set = []
            for i in range(1 << len(modifiers)):
                modifier_power_set.append(sum(modifiers[j] for j in range(len(modifiers)) if (i & (1 << j))))
        else:
            address, value = [int(num) for num in re.findall("\d+", line)]
            base_address = (address | mask_set_ones) & mask_set_zeroes
            for modifier in modifier_power_set:
                address_space[base_address + modifier] = value

    return sum(address_space.values())


def main():
    read_file()
    part1_sum = populate_addresses()
    part2_sum = floaty_populate_addresses()

    print(f"The part 1 sum is {part1_sum}")
    print(f"The part 2 sum is {part2_sum}")


if __name__ == "__main__":
    main()
