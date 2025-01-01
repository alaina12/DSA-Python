# return True if the array contains duplicate and false else where
 
def containsDuplicate(nums):
 	N = len(nums)
 	#create a dictionary to store unique elements
 	unique_elements = {}
 	#loop through the array
 	for i in range(N):
 		#if elements is in arrray return True
 		if nums[i] in unique_elements:
 			return True
 		#if the element is not in array, add it to the dict
 		else:
 			unique_elements[nums[i]] = True
 		#else return False
 	return False

print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))