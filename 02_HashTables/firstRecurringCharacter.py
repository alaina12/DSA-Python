# O(n^2)

def first_recurring_character(input_list):
	for i in range(len(input_list)):
		for j in range(i+1, len(input_list)):
			if input_list[i] == input_list[j]:
				return input_list[i]
	return None

print(first_recurring_character([2,5,1,2,3,5,1,2,4])) 


# O(n) 

def first_recurring_character2(input_list):
	seen = {}
	for i, value in enumerate(input_list):
		if value in seen:
			return value
		else:
			seen[value] = i
	return None

print(first_recurring_character([2,5,1,2,3,1,2,4]))