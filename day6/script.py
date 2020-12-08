def read_file():
	file = open("input.txt", "r")
	lines = [line.strip() for line in file]
	file.close()
	return lines


def get_answer_sets(lines):
	answer_sets = []
	group = set()
	for line in lines:
		if line:
			group.update(list(line))
		else:
			answer_sets.append(group)
			group = set()

	return answer_sets


def get_answer_sets2(lines):
	answer_sets = []
	group = set(list(lines[0]))
	i = 1
	while i < len(lines):
		line = lines[i]
		if line:
			group = group.intersection(set(list(line)))
		else:
			answer_sets.append(group)
			group = set(list(lines[i + 1])) if i + 1 < len(lines) else None
			i += 1
		i += 1

	return answer_sets


def main(): 
	lines = read_file()

	answer_sets = get_answer_sets(lines)
	answer_sets2 = get_answer_sets2(lines)

	print(f"The first sum is: {sum([len(x) for x in answer_sets])}.")
	print(f"The second sum is: {sum([len(x) for x in answer_sets2])}.")


if __name__=="__main__": 
	main()

