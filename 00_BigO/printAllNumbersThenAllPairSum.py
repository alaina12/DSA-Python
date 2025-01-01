def printAllNumbersThenAllPairSums(numbers):
	print('These are the numbers:')
	for number in numbers:
		print(number)

	print("and these are their sums:")
	for first_number in numbers:
		for second_number in numbers:
			print(first_number + second_number)
			
printAllNumbersThenAllPairSums([1,2,3,4,5])