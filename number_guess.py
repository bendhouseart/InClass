import random

number = int(random.uniform(1,2)*1000000000)

selection = '1'

print(number)

while selection != 'q':
	selection = input('Would you like to guess a number? Enter yes or no: '.lower())

	if 'y' in selection:
		try:
			guess = int(input('Enter a  guess >= 1000,000,000, and <= 2,000,000,00: '))
		except:
			print('Sorry, you did not enter an integer.')
			break
	else:
		prompt = input('Are you sure you\'d like to exit? enter yes to confirm: ')
		if 'y' in prompt.lower():
			selection = 'q'
			continue
		else:
			continue

	if guess == number:
		print('Congratulations, you guessed the number.')
		number = int(random.uniform(1,2)*1000000000)
	elif guess < number:
		print('Too low so slow')
		continue
	elif guess > number:
		print('Too high, get rekt')
		continue
	else:
		print('error')
