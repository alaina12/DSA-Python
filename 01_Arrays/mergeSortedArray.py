def merge_sorted_array(array1, array2):
	merged_array = []
	i, j = 0,0

	# merging logic
	while i < len(array1) and j < len(array2):
		if array1[i] < array2[j]:
			merged_array.append(array1[i])
			i += 1
		else:
			merged_array.append(array2[j])
			j += 1
	# Add remainind elements from array1 (if any)
	while i < len(array1):
		merged_array.append(array1[i])
		i += 1
	# Add remaining elements from array2 (if any)
	while j < len(array2):
		merged_array.append(array2[j])
		j += 1

	return merged_array

print(merge_sorted_array([0,3,2,31], [4,6,30]))