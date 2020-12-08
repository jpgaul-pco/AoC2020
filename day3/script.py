def read_file():
	file = open("input.txt", "r")
	lines = [line for line in file]
	file.close()
	return lines

def count_trees(lines, horiz, vert):
	width = len(lines[0]) - 1
	x_pos = 0
	to_return = 0
	for i in range(0, len(lines), vert):
		to_return += 1 if lines[i][x_pos] == "#" else 0
		x_pos += horiz
		x_pos %= width

	return to_return


def main(): 
	lines = read_file()

	trees_part1 = count_trees(lines, 3, 1)
	options = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
	trees_multiplied = 1
	for horiz, vert in options:
		trees_multiplied *= count_trees(lines, horiz, vert)

	print(f"You encounter {trees_part1} in part 1.")
	print(f"The answer to part 2 is {trees_multiplied}.")


if __name__=="__main__": 
	main()