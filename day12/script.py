import math

lines = []
cardinal_coords = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}


def read_file():
    file = open("input.txt", "r")
    [lines.append(line.strip()) for line in file]
    file.close()


def projection(degrees_to_rotate):
    return int(math.cos(math.radians(degrees_to_rotate))), int(math.sin(math.radians(degrees_to_rotate)))


def navigate():
    curr_pos = [0, 0]
    curr_dir_deg = 0
    for line in lines:
        action, amt = line[0], int(line[1:])
        if action == "F":
            proj = projection(curr_dir_deg)
            curr_pos = [curr_pos[0] + proj[0] * amt,
                        curr_pos[1] + proj[1] * amt]
        elif action == "L" or action == "R":
            amt *= 1 if action == "L" else -1
            curr_dir_deg = (curr_dir_deg + amt) % 360
        else:
            cardinal_coord = cardinal_coords.get(action)
            curr_pos = [curr_pos[0] + cardinal_coord[0] * amt,
                        curr_pos[1] + cardinal_coord[1] * amt]
    return curr_pos


def navigate_waypoint():
    curr_ship_pos = [0, 0]
    curr_waypoint_pos = [10, 1]
    for line in lines:
        action, amt = line[0], int(line[1:])
        if action == "F":
            curr_ship_pos = [curr_ship_pos[0] + curr_waypoint_pos[0] * amt,
                             curr_ship_pos[1] + curr_waypoint_pos[1] * amt]
        elif action == "L" or action == "R":
            amt *= 1 if action == "L" else -1
            proj = projection(amt)
            curr_waypoint_pos = [curr_waypoint_pos[0] * proj[0] - curr_waypoint_pos[1] * proj[1],
                                 curr_waypoint_pos[0] * proj[1] + curr_waypoint_pos[1] * proj[0]]
        else:
            cardinal_coord = cardinal_coords.get(action)
            curr_waypoint_pos = [curr_waypoint_pos[0] + cardinal_coord[0] * amt,
                                 curr_waypoint_pos[1] + cardinal_coord[1] * amt]
    return curr_ship_pos


def main():
    read_file()
    curr_pos = navigate()
    curr_pos_waypoint = navigate_waypoint()
    print(f"The final distance traveled is {abs(curr_pos[0]) + abs(curr_pos[1])}")
    print(f"The final distance traveled by waypoint is {abs(curr_pos_waypoint[0]) + abs(curr_pos_waypoint[1])}")


if __name__ == "__main__":
    main()
