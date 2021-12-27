def part1(commands):
	horz = 0
	depth = 0
	for cmd in commands:
		parsed = cmd.split(" ")
		action = parsed[0]
		val = int(parsed[1])	
		if action == "forward":
			horz += val
		elif action == "up":
			depth -= val
		else:
			depth += val	
	print(f"Part 1: final horizontal position and depth: {horz}, {depth}. Multiplied: {horz*depth}")

def part2(commands):
	aim = 0
	horz = 0
	depth = 0
	for cmd in commands:
		parsed = cmd.split(" ")
		action = parsed[0]
		val = int(parsed[1])
		if action == "forward":
			horz += val
			depth += aim*val
		elif action == "up":
			aim -= val
		else:
			aim += val	
	print(f"Part 2: final horizontal position and depth: {horz}, {depth}. Multiplied: {horz*depth}") 
	
def main():
	commands = open("input.txt", "r").readlines()
	part1(commands)
	part2(commands)
	
if __name__ == "__main__":
	main()
