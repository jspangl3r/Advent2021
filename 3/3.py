def part1(nums):
	length = len(nums[0])
	most_commons = [0]*length
	least_commons = [0]*length
	for i in range(length):
		num_0 = 0
		num_1 = 0
		for num in nums:
			if num[i] == '0':
				num_0 += 1
			else:
				num_1 += 1
		most_commons[i] = '0' if num_0 > num_1 else '1'	
		least_commons[i] = '1' if num_0 > num_1 else '0'
	gamma = int("".join(most_commons), 2) 
	epsilon = int("".join(least_commons), 2)
	print(f"Gamma: {gamma}, Epsilon: {epsilon}, Multiplied = {gamma*epsilon}")
	
def main():
	nums = [x.replace("\n", "") for x in open("input.txt", "r").readlines()]
	part1(nums)	

if __name__ == "__main__":
	main()
