def ie_check(word):

	c_location = word.find('c')

	ie_location = word.find('ie')

	if c_location == -1 or ie_location == -1:
		print("You didn't enter a valid number.")
	elif c_location < ie_location:
		print("This word does not follow the rule: I before E except after C.")
	else:
		print("This word follows the rule: I before E except after C.")


word = input("Please enter a word containing an 'ie' and the letter c. ")

ie_check(word)
