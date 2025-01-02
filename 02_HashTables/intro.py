user = {
	'name' : "Brent",
	'age' : 56,
	'magic' : True,
	'scream' : lambda:print('aaaaaaaaaah!')
}

#Lookup O(1)
print(user["name"])

#insert O(1)
user["spell"] = 'abra kadabra'

#print the updates dictionary
print(user)