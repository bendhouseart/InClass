import os

os.system('clear')

current_time = int(input('Please enter the current hour: '))
am_pm = input('enter am or pm: ').lower()

if am_pm == 'pm':
	current_time = current_time + 12

if    7 <= current_time <= 9:
	print('Breakfast is now being served.')
elif 12 <= current_time <= 14:
	print('Lunch is now being served.')
elif 19 <= current_time <= 21:
	print('Dinner is now being served.')
elif current_time >= 22 or current_time <= 4:
	print('Stop: Hammer Time.')
else:
	print('Tough luck chump.')
