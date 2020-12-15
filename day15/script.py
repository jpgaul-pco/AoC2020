import timeit


starting_nums = []


def read_file():
    file = open("input.txt", "r")
    [starting_nums.extend(int(i) for i in line.split(",")) for line in file]
    file.close()


def play_game(final_turn):
    record = {}
    for i, num in enumerate(starting_nums):
        record[num] = [i, i]

    diff = starting_nums[-1]
    for i in range(len(starting_nums), final_turn):
        diff = record[diff][0] - record[diff][1]
        record[diff] = [i, i if record.get(diff) is None else record[diff][0]]

    return diff


def main():
    read_file()
    last_num_short = play_game(2020)
    start = timeit.default_timer()
    last_num = play_game(30000000)
    time = timeit.default_timer() - start

    print(f"The 2020th number is {last_num_short}")
    print(f"The 30000000th number is {last_num} (in {time:.1f} seconds!)")


if __name__ == "__main__":
    main()
