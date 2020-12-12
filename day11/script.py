lines = []


class BackingStruct:
    def __init__(self, in_grid):
        self.height = len(in_grid) + 2
        self.width = len(in_grid[0]) + 2
        top_wall = [["w" for x in range(self.width - 2)]]
        self.grid = top_wall + in_grid + top_wall
        self.grid = [["w"] + row + ["w"] for row in self.grid]
        self.updated_grid = [["w" for i in row] for row in self.grid]
        self.adjacency_coords = [[[] for j in range(self.width)] for i in range(self.height)]

    def set_grid(self):
        self.grid = [row[:] for row in self.updated_grid]

    def set_adjacent_seats(self):
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                self.adjacency_coords[i][j] = [(i + x, j + y) for x, y in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]]

    def set_los_seats(self):
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                for x, y in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                    mult = 1
                    while self.grid[i + mult * x][j + mult * y] != "w" and \
                            self.grid[i + mult * x][j + mult * y] != "L":
                        mult += 1
                    self.adjacency_coords[i][j].append([i + mult * x, j + mult * y]) if \
                        self.grid[i + mult * x][j + mult * y] == "L" else None

    def update_grid(self, threshold):
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                adjacenct_members = [self.grid[x][y] for x, y in self.adjacency_coords[i][j]]
                if self.grid[i][j] == "L" and adjacenct_members.count("#") == 0:
                    self.updated_grid[i][j] = "#"
                elif self.grid[i][j] == "#" and adjacenct_members.count("#") >= threshold:
                    self.updated_grid[i][j] = "L"
                else:
                    self.updated_grid[i][j] = self.grid[i][j]


def read_file():
    file = open("input.txt", "r")
    [lines.append(list(line.strip())) for line in file]
    file.close()


def stabilize_state(backing_struct, threshold):
    backing_struct.update_grid(threshold)
    while backing_struct.grid != backing_struct.updated_grid:
        backing_struct.set_grid()
        backing_struct.update_grid(threshold)
    return sum([x.count("#") for x in backing_struct.grid])


def main():
    read_file()
    backing_struct = BackingStruct(lines)
    backing_struct.set_adjacent_seats()
    stabilized_seat_count = stabilize_state(backing_struct, 4)

    backing_struct = BackingStruct(lines)
    backing_struct.set_los_seats()
    stabilized_seat_count_los = stabilize_state(backing_struct, 5)

    print(f"Once stabilized, there will be {stabilized_seat_count} occupied seats.")
    print(f"Once stabilized with line of sight, there will be {stabilized_seat_count_los} occupied seats.")


if __name__ == "__main__":
    main()
