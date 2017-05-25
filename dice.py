from random import *

while True:
	no_die = int(input("Enter the number of die you wish to roll. "))

	sides  = int(input("Enter the number of sides to your die. "))




	for no_die in range(no_die):
		print('\n' + 'You have rolled a: ',randrange(1,sides,1))


	rollagain = input("do you wish to roll again?").lower()

	if 'n' in rollagain:
		break
