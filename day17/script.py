import copy


lines = []
rounds = 6
offset = rounds + 1


def read_file():
    file = open("input.txt", "r")
    [lines.append(line.strip()) for line in file]
    file.close()


def simulate_array():
    backing_array = []
    for i in range(len(lines) + 2 * offset):
        backing_array.append([["." for k in range(1 + 2 * offset)] for j in range(len(lines[0]) + 2 * offset)])
    for x, line in enumerate(lines):
        for y, elem in enumerate(line):
            backing_array[offset + x][offset + y][offset] = elem

    update_array = copy.deepcopy(backing_array)
    neighbors = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                neighbors.append((i, j, k))
    neighbors.remove((0, 0, 0))

    for round_num in range(rounds):
        for i in range(1, len(backing_array) - 1):
            for j in range(1, len(backing_array[0]) - 1):
                for k in range(1, len(backing_array[0][0]) - 1):
                    neighbor_contents = [backing_array[i + x][j + y][k + z] for x, y, z in neighbors]
                    neighbor_count = neighbor_contents.count("#")
                    if backing_array[i][j][k] == "#" and (2 > neighbor_count or neighbor_count > 3):
                        update_array[i][j][k] = "."
                    elif backing_array[i][j][k] == "." and neighbor_count == 3:
                        update_array[i][j][k] = "#"
        backing_array = copy.deepcopy(update_array)

    return sum([sum([sub_arr.count("#") for sub_arr in arr]) for arr in backing_array])


def simulate_array_4d():
    backing_array = []
    for i in range(len(lines) + 2 * offset):
        backing_array.append([[["." for _ in range(1 + 2 * offset)] for _ in range(1 + 2 * offset)] for _ in range(len(lines[0]) + 2 * offset)])
    for x, line in enumerate(lines):
        for y, elem in enumerate(line):
            backing_array[offset + x][offset + y][offset][offset] = elem

    update_array = copy.deepcopy(backing_array)
    neighbors = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for L in [-1, 0, 1]:
                    neighbors.append((i, j, k, L))
    neighbors.remove((0, 0, 0, 0))

    for round_num in range(rounds):
        for i in range(1, len(backing_array) - 1):
            for j in range(1, len(backing_array[0]) - 1):
                for k in range(1, len(backing_array[0][0]) - 1):
                    for L in range(1, len(backing_array[0][0][0]) - 1):
                        neighbor_contents = [backing_array[i + x][j + y][k + z][L + w] for x, y, z, w in neighbors]
                        neighbor_count = neighbor_contents.count("#")
                        if backing_array[i][j][k][L] == "#" and (2 > neighbor_count or neighbor_count > 3):
                            update_array[i][j][k][L] = "."
                        elif backing_array[i][j][k][L] == "." and neighbor_count == 3:
                            update_array[i][j][k][L] = "#"
        backing_array = copy.deepcopy(update_array)

    return sum([sum([sum([sub_sub_arr.count("#") for sub_sub_arr in sub_arr]) for sub_arr in arr]) for arr in backing_array])


def main():
    read_file()
    cube_count = simulate_array()
    hypercube_count = simulate_array_4d()

    print(f"After {rounds} cycles there are {cube_count} cubes")
    print(f"After {rounds} cycles there are {hypercube_count} hypered-cubes")


if __name__ == "__main__":
    main()
