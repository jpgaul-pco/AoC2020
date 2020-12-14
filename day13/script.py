import re


lines = []


def read_file():
    file = open("input.txt", "r")
    [lines.append(line.strip()) for line in file]
    file.close()


def find_product():
    earliest_time = int(lines[0])
    bus_list = [int(bus) for bus in re.findall("\d+", lines[1])]
    next_bus_list = [bus - (earliest_time % bus) for bus in bus_list]
    min_index = next_bus_list.index(min(next_bus_list))
    return bus_list[min_index] * next_bus_list[min_index]


def find_sequence():
    bus_list = [int(bus) if bus else "" for bus in re.split(",x*", lines[1])]
    running_tally = 0
    increment = bus_list[0]
    for i, bus_num in enumerate(bus_list[1:], 1):
        if bus_num:
            while (running_tally + i) % bus_num != 0:
                running_tally += increment
            increment *= bus_num

    return running_tally


def main():
    read_file()
    part1_product = find_product()
    seq_start = find_sequence()

    print(f"The part 1 product is {part1_product}")
    print(f"The part 2 sequence starts at {seq_start}")


if __name__ == "__main__":
    main()
