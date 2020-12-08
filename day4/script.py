def read_file():
	file = open("input.txt", "r")
	lines = [line for line in file]
	file.close()
	return lines


def get_full_passport_dict(lines):
	required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
	passports = []
	person = {}
	for line in lines:
		pairs = line.split()
		if pairs:
			for pair in pairs:
				key, val = pair.split(":")
				person[key] = val
		else:
			if required.issubset(set(person.keys())):
				passports.append(person)
			person = {}

	return passports


def validate_fields(passports):
	valid_ecls = set('amb blu brn gry grn hzl oth'.split())
	validated_passports = []
	for passport in passports:
		try:
			valid_byr = int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002
			valid_iyr = int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020
			valid_eyr = int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030
			if passport['hgt'][-2:] == 'cm':
				valid_hgt = int(passport['hgt'][:-2]) >= 150 and int(passport['hgt'][:-2]) <= 193
			elif passport['hgt'][-2:] == 'in':
				valid_hgt = int(passport['hgt'][:-2]) >= 59 and int(passport['hgt'][:-2]) <= 76
			else:
				valid_hgt = False
			valid_hcl = passport['hcl'][0] == '#' and len(passport['hcl'][1:]) == 6 and int(passport['hcl'][1:], 16)
			valid_ecl = passport['ecl'] in valid_ecls
			valid_pid = len(passport['pid']) == 9 and int(passport['pid'])

			if valid_byr and valid_iyr and valid_eyr and valid_hgt and valid_hcl and valid_ecl and valid_pid:
				validated_passports.append(passport)
		except:
			pass

	return validated_passports


def main(): 
	lines = read_file()

	full_passports = get_full_passport_dict(lines)
	validated_passports = validate_fields(full_passports)

	print(f"There are {len(full_passports)} passports with all required fields.")
	print(f"There are {len(validated_passports)} passports with valid fields.")


if __name__=="__main__": 
	main()
