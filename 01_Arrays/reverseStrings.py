#by using for loop
def reverse(str):
	mylist = []
	for i in range(len(str)-1,-1,-1):
		mylist.append(str[i])
	return ''.join(mylist)

x = reverse('I am Alaina')
print(x)


# By using string indexing
def reverse1(str1):
	return str1[::-1]

print(reverse1('I am Alaina'))