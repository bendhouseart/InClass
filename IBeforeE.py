word = input("Please enter a correctly spelled word: ").lower()

if 'ie' in word:
	print("This word contains an ie.")
else:
	print("This word doesnt contain ie.")


index = 0

for letter in word:
	if letter == 'c':
		c = index
	if letter == 'i' and word[index + 1] == 'e':
		ie = index
	print(letter)

if c < ie:
	print("this does not follow the rule.")
else:
	print("this does follow the rule.")
