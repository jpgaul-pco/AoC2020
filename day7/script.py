import re


lines = []
backing_dict = {}
reversed_dict = {}


def read_file():
	file = open("input.txt", "r")
	[lines.append(line.strip()) for line in file]
	file.close()


def populate_backing_dict():
	for line in lines:
		color, contents = line.split(" bags contain ")
		attr_list = re.findall("(\d+ \w+ \w+)", contents)
		backing_dict[color] = [tuple(attr.split(" ", 1)) for attr in attr_list]


def populate_reversed_dict():
	for color in backing_dict.keys():
		reversed_dict[color] = []
	for color, vals in backing_dict.items():
		for amt, dest_color in vals:
			reversed_dict[dest_color].append((amt, color))


def populate_parent_colors(target_color, parent_colors_set):
	parent_colors_set.add(target_color)
	for curr_parent_amt, curr_parent_color in reversed_dict[target_color]:
		if curr_parent_color not in parent_colors_set:
			populate_parent_colors(curr_parent_color, parent_colors_set)


def get_child_bag_count(target_color):
	to_return = 1
	for children_amt, children_color in backing_dict[target_color]:
		to_return += int(children_amt) * get_child_bag_count(children_color)
	return to_return


def main(): 
	read_file()

	populate_backing_dict()
	populate_reversed_dict()

	parent_colors_set = set()
	populate_parent_colors('shiny gold', parent_colors_set)
	parent_colors_set.remove('shiny gold') # don't count the bag itself
	child_bags = get_child_bag_count('shiny gold') - 1 # off by one for the parent bag itself
	print(f"There are {len(parent_colors_set)} parent bag colors.")
	print(f"There are {child_bags} child bags required.")


if __name__=="__main__": 
	main()
