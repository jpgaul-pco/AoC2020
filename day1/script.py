import timeit

def read_file():
	file = open("input.txt", "r")
	lines = [line for line in file]
	file.close()
	return lines

def slow_soln1(nums):
	for i in nums:
		for j in nums:
			if i + j == 2020:
				return i * j
	return 1

def slow_soln2(nums):
	for i in nums:
		for j in nums:
			for k in nums:
				if i + j + k == 2020:
					return i * j * k
	return 1


def fast_soln1(nums):
	pairs = set()
	for num in nums:
		compliment = 2020-num
		if num in pairs:
			return num * compliment
		else:
			pairs.add(2020-num)
	return 1


def fast_soln2(nums):
	nums.sort()
	prev = None
	for i in range(len(nums)):
		curr = nums[i]
		if i == prev:
			continue
		target = -curr
		start = i + 1
		end = len(nums) - 1
		while start < end:
			curr_sum = curr + nums[start] + nums[end]
			if curr_sum == 2020:
				return curr * nums[start] * nums[end]
			elif curr_sum > 2020:
				end -= 1
			else:
				start += 1

		prev = curr

	return 1

def main(): 
	lines = read_file()
	nums = [int(x) for x in lines]

	slow1_start = timeit.default_timer()
	slow1 = slow_soln1(nums)
	slow1_time = timeit.default_timer() - slow1_start

	slow2_start = timeit.default_timer()
	slow2 = slow_soln2(nums)
	slow2_time = timeit.default_timer() - slow2_start

	print("Part 1 Brute Force:")
	print(f"Result: {slow1}, time: {(slow1_time * 1000):.3f} ms")
	print("Part 2 Brute Force:")
	print(f"Result: {slow2}, time: {(slow2_time * 1000):.1f} ms")

	fast1_start = timeit.default_timer()
	fast1 = fast_soln1(nums)
	fast1_time = timeit.default_timer() - fast1_start

	fast2_start = timeit.default_timer()
	fast2 = fast_soln2(nums)
	fast2_time = timeit.default_timer() - fast2_start

	print("Part 1 Fast:")
	print(f"Result: {fast1}, time: {(fast1_time * 1000):.3f} ms, speedup: {(slow1_time / fast1_time):.0f}x")
	print("Part 2 Fast:")
	print(f"Result {fast2}, time: {(fast2_time * 1000):.1f} ms, speedup: {(slow2_time / fast2_time):.0f}x")


if __name__=="__main__": 
	main()