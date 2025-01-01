#maximum subarray in the given array

def maxSubArray(nums):
	N = len(nums)
	max_sum = nums[0]
	curr_sum = nums[0]
	for i in range(1,N):
		curr_sum = max(nums[i],curr_sum+nums[i])
		max_sum = max(max_sum,curr_sum)
	return max_sum

print(maxSubArray([-2,1]))