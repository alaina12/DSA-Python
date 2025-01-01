#two Sum

def twoSum(nums, target):
	N = len(nums)
	for i in range(N):
		for j in range(i+1, N):
			if nums[i] + nums[j] == target:
				return [i,j]
print(twoSum([3,2,4], 6))

#o(n^2)