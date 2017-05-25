def join2strings():
	string1 = input('Enter a string: ')
	string2 = input('Enter a string: ')
	print(string1.join(string2))
	print(str.join(string1,string2))
	return 0

join2strings()
