def read_file():
	file = open("input.txt", "r")
	lines = [line.strip() for line in file]
	file.close()
	return lines


def convert_partition(code):
	bin_stirng = "".join(['0' if x == 'F' or x == 'L' else '1' for x in code])
	row = int(bin_stirng[:7], 2)
	col = int(bin_stirng[7:], 2)
	seat_id = row * 8 + col
	return code, row, col, seat_id


def get_id_max_and_set(lines):
	max_id = -1
	first_full_row = 127
	last_full_row = 0
	id_set = set()
	for line in lines:
		code, row, col, seat_id = convert_partition(line)
		max_id = max(max_id, seat_id)
		first_full_row = row if row < first_full_row and col == 0 else first_full_row
		last_full_row = row if row > last_full_row and col == 7 else last_full_row
		id_set.add(seat_id)
	return max_id, first_full_row, last_full_row, id_set


def missing_seat_id(first_full_row, last_full_row, id_set):
	full_set = set([x for x in range(first_full_row * 8, last_full_row * 8 + 8)])
	return full_set.difference(id_set).pop()


def main(): 
	lines = read_file()

	max_id, first_full_row, last_full_row, id_set = get_id_max_and_set(lines)
	missing_id = missing_seat_id(first_full_row, last_full_row, id_set)

	print(f"The max ID is {max_id}.")
	print(f"The missing seat id is {missing_id}.")


if __name__=="__main__": 
	main()
