def part1(nums):
	increases = 0
	for i in range(1, len(nums)):
		if nums[i] > nums[i-1]:
			increases += 1	
	print(f"Part 1: number pairwise increases is {increases}")

def part2(nums):
	increases = 0
	prev_window = []
	for i in range(len(nums)-2):
		window = [nums[i], nums[i+1], nums[i+2]]
		if len(prev_window) > 0:
			if sum(window) > sum(prev_window):
				increases += 1
		prev_window = window		
	print(f"Part 2 : number increase via windows is {increases}")
	
def main():
	nums = [int(x) for x in open("input.txt", "r").readlines()]
	part1(nums)
	part2(nums)	

if __name__ == "__main__":
	main()
