import re

def longestWord(sen):
	# split the sentence into words based on spaces
	arr_words = sen.split(' ')

	# Regular expression to match valid characters (ketters, digits, snd some special characters)
	regular_expression = re.compile(r"^[a-zA-Z0-9ñáéíóúÁÉÍÓÚÑ ,.'-]+$")

	# Initialize the variable to stire the longest word
	str_longer = ""

	# iterate through each word in the array
	for word in arr_words:
		# check if the word matches the regular expression and is longerthan the current longest word
		if regular_expression.match(word) and len(word) > len(str_longer):
			str_longer = word


	# Return the longest valid word
	return str_longer

print(longestWord(input("Enter a sentence: ")))
