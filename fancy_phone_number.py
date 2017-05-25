while True:

	phone_number = input('Enter a 10 digit phone number: ')

	if len(phone_number) != 10:
		print('Enter a valid phone number.')
	else:
		break

print('(' + phone_number[:3] + ')' + '-' + phone_number[3:6] + '-' + phone_number[6:10])
