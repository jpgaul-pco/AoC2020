import bisect
import timeit


lines = []
preamble_len = 25


def read_file():
	file = open("input.txt", "r")
	[lines.append(int(line.strip())) for line in file]
	file.close()


# O(n * p^2)
def check_pattern_bf():
	for i in range(preamble_len, len(lines)):
		preamble = lines[i-preamble_len:i]
		preamble_set = set([i + j for i in preamble for j in preamble])
		if not lines[i] in preamble_set:
			return lines[i]
	return 0


# O(n^3)
def find_target_range_bf(target_number):
	for i in range(len(lines)):
		for j in range(len(lines)):
			if sum(lines[i:j]) == target_number:
				return lines[i:j]
	return 0


# O(n * p)
def check_pattern():
	preamble = sorted(lines[:preamble_len])

	for i in range(preamble_len, len(lines)): # O(n)
		start = 0
		end = len(preamble) - 1
		while start < end and preamble[start] + preamble[end] != lines[i]: # O(p)
			if preamble[start] + preamble[end] > lines[i]:
				end -= 1
			else:
				start += 1
		if start == end:
			return lines[i]
		
		bisect.insort(preamble, lines[i]) # O(log(p))
		del preamble[bisect.bisect_left(preamble, lines[i - preamble_len])] # O(p)

	return 0


def find_target_range(target_number):
	for i in range(len(lines)):
		for j in range(len(lines)):
			if sum(lines[i:j]) == target_number:
				return lines[i:j]
	return 0


def main(): 
	read_file()

	start_p1bf = timeit.default_timer()
	broken_pattern_bf = check_pattern_bf()
	time_p1bf = timeit.default_timer() - start_p1bf
	start_p2bf = timeit.default_timer()
	target_range_bf = find_target_range_bf(broken_pattern_bf)
	time_p2bf = timeit.default_timer() - start_p2bf

	start_p1 = timeit.default_timer()
	broken_pattern = check_pattern()
	time_p1 = timeit.default_timer() - start_p1
	start_p2 = timeit.default_timer()
	target_range = find_target_range(broken_pattern)
	time_p2 = timeit.default_timer() - start_p2

	print(f"The first number to break the pattern is {broken_pattern}, speedup: {(time_p1bf / time_p1):.0f}x.")
	print(f"The added min and max is {min(target_range) + max(target_range)}, speedup: {(time_p2bf / time_p2):.0f}x.")


if __name__=="__main__": 
	main()
