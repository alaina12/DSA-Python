#to understand the space complexity

def booo(n):
	for i in range(n):
		print('booooooo')


def arrayOfHiNTimes(n):
	hiArray = []
	for i in range(n):
		hiArray.append('hi')

	return hiArray
booo(6)
print(arrayOfHiNTimes(6))