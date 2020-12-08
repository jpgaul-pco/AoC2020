import re


def read_file():
	file = open("input.txt", "r")
	lines = [line for line in file]
	file.close()
	return lines


def valid_passwords_part1(lines):
	passwords = []
	for line in lines:
		min_amt, max_amt, character, password = re.split("-| |: ", line)
		amt = password.count(character)
		if amt >= int(min_amt) and amt <= int(max_amt):
			passwords.append(password)
	return passwords


def valid_passwords_part2(lines):
	passwords = []
	for line in lines:
		pos_one, pos_two, character, password = re.split("-| |: ", line)
		char_at_one = character == password[int(pos_one) - 1]
		char_at_two = character == password[int(pos_two) - 1]
		if char_at_one ^ char_at_two:
			passwords.append(password)
	return passwords


def main(): 
	lines = read_file()

	passwords_part1 = valid_passwords_part1(lines)
	passwords_part2 = valid_passwords_part2(lines)

	print(f"There are {len(passwords_part1)} valid passwords in part 1.")
	print(f"There are {len(passwords_part2)} valid passwords in part 2.")


if __name__=="__main__": 
	main()