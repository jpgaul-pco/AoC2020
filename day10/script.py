lines = []


def read_file():
	file = open("input.txt", "r")
	[lines.append(int(line.strip())) for line in file]
	file.close()


def chain_adapters():
	sorted_lines = sorted(lines)
	one_ct = 0
	three_ct = 0
	curr = 0
	for line in sorted_lines:
		if line - curr == 1:
			one_ct += 1
		elif line - curr == 3:
			three_ct += 1
		curr = line

	return one_ct * (1 + three_ct)


def count_arrangements():
	sorted_lines = sorted(lines)
	arrangement_array = [0 for i in range(max(sorted_lines) + 1)]
	arrangement_array[0] = 1
	for i in sorted_lines:
		arrangement_array[i] = arrangement_array[i - 1] + arrangement_array[i - 2] + arrangement_array[i - 3]
	return arrangement_array[-1]


def main(): 
	read_file()

	part1_prod = chain_adapters()
	arrangements = count_arrangements()
	print(f"The product for part one is {part1_prod}.")
	print(f"The number of possible arrangements is {arrangements}.")


if __name__=="__main__": 
	main()
