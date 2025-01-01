def rotate(nums,k):
	if k == 0:
		return nums
	else:
		for i in range(k):
			nums.insert(0,nums.pop())
		return nums

print(rotate([1,2,3,4,5,6,7], 3))