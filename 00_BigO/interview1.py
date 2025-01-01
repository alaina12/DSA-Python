#Given two input arrays return True if it contains common items and False else where
#sample input1
#array1=['a'.'b','c','x']
#array2 = ['z','y','i'] return False
#sample input2
#array1 = ['a','b','c','x']
#array2 = ['z','y','x'] return True

def common_elem(arr1, arr2):
	for i in range(len(arr1)):
		for j in range(len(arr2)):
			if arr1[i] == arr2[j]:
				return True
	return False

print(common_elem(['a','b','i','x'],['z','y','i']))
#O(n^2)

