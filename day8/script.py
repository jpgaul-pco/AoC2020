import re


lines = []


def read_file():
	file = open("input.txt", "r")
	[lines.append(line.strip()) for line in file]
	file.close()


def run_until_term_or_loop(ptr=0, acc=0, visited=set()):
	while ptr not in visited and ptr < len(lines):
		visited.add(ptr)
		instr, value = lines[ptr].split()
		if instr == "acc":
			acc += int(value)
			ptr += 1
		elif instr == "jmp":
			ptr += int(value) if int(value) != 0 else len(lines) # terminate if jmp 0
		else: # nop
			ptr += 1
	return ptr >= len(lines), acc

def toggle_instructions(ptr=0, acc=0, visited=set()):
	terminated = False
	while ptr not in visited and ptr < len(lines):
		visited.add(ptr)
		instr, value = lines[ptr].split()
		if instr == "acc":
			acc += int(value)
			ptr += 1
		elif instr == "jmp":
			ptr += 1
			terminated, acc_forecast = run_until_term_or_loop(ptr, acc, visited.copy())
			if terminated:
				return terminated, acc_forecast
			else:
				ptr -= 1
			
			ptr += int(value) if int(value) != 0 else len(lines) # terminate if jmp 0
		else: # nop
			ptr += int(value) if int(value) != 0 else len(lines)
			terminated, acc_forecast = run_until_term_or_loop(ptr, acc, visited.copy())
			if terminated:
				return terminated, acc_forecast
			else:
				ptr -= int(value) if int(value) != 0 else len(lines)

			ptr += 1
	return terminated, acc

def main(): 
	read_file()

	terminated1, loop_acc = run_until_term_or_loop()
	terminated2, term_acc = toggle_instructions()
	print(terminated2, term_acc)

	print(f"One loop accumulates {loop_acc}.")


if __name__=="__main__": 
	main()
