lines = []
preamble_len = 25
preamble = []


def read_file():
	file = open("input.txt", "r")
	[lines.append(int(line.strip())) for line in file]
	file.close()


def check_pattern_bf():
	for i in range(preamble_len, len(lines)):
		preamble = lines[i-preamble_len:i]
		preamble_set = set([i + j for i in preamble for j in preamble])
		if not lines[i] in preamble_set:
			return lines[i]
	return 0


def find_target_range_bf(target_number):
	for i in range(len(lines)):
		for j in range(len(lines)):
			if sum(lines[i:j]) == target_number:
				return lines[i:j]
	return 0


def main(): 
	read_file()

	broken_pattern = check_pattern_bf()
	target_range = find_target_range_bf(broken_pattern)

	print(f"The first number to break the pattern is {broken_pattern}.")
	print(f"The added min and max is {min(target_range) + max(target_range)}.")


if __name__=="__main__": 
	main()
