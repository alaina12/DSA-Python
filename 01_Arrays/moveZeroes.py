# move all the zeroes to the end

def moveZeroes(nums):
	N = len(nums)
	if N == 0:
		return nums
	i = 0
	j = 0
	while j < N:
		if nums[j] != 0:
			nums[i] = nums[j]
			i += 1
		j += 1
	while i < N:
		nums[i] = 0
		i += 1
	return nums
print(moveZeroes([0,1,2,0,3]))
