word = input('Please enter a word: ')

def case_check(some_word):
	capital_characters = [C for C in some_word if C.isupper()]
	if '_' in some_word:
		print('snek_case')
	elif len(capital_characters) != 0:
		print('CamelCase')
	else:
		print('Bad Input')

case_check(word)

