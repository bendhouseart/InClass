import os

try:
	os.system('clear')
except:
	pass


def greeting_to_person(yournamehere,yournumber):
	return 'Hello {}, your number is {}.'.format(yournamehere,yournumber)


name = input('What is your name buddy? ')
phone_number = input('What is your phone number? ')

x = greeting_to_person(name,phone_number)

print(x)
