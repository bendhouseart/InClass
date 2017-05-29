import csv
import pandas
from numpy import genfromtxt
import sys

file_name = sys.argv[1]

'''Here we're going to create a dictionary within a dictionary using the last name
of someone as'''


def create_dictionary(file_name):
	phone_book_file = (open(file_name,'r'))
	phone_book_list = []
	for line in phone_book_file:
		phone_book_list.append(tuple(line.strip().split(',')))

	phone_book_dictionary = {}

	for entry in phone_book_list:
		phone_book_dictionary[entry[1]] = {'first_name': entry[0], 'last_name': entry[1], 'number': entry[2]}

	return phone_book_dictionary

def name_search(name,phone_book):
	name = name.title()
	try:
		print(phone_book[name])
	except KeyError:
		print("Entry was not found.")
			
def add_contact(dictionary):
	last_name = input('Enter the contact\'s last name: < ')
	first_name = input('Enter the contact\'s first name: < ')
	number = input('Enter the contact\'s number: < ')

	dictionary[last_name.title()] = {'first_name': first_name.title(), 'last_name': last_name.title(), 'number': number}				
	return last_name.title()

def delete_contact(dictionary):
	
	name = input('Enter the name of the contact you wish to delete: < ')	

	try:
		contact = dictionary[name.title()]
		confirm = input('Do you wish to delete: ' + str(contact) + ' ? enter yes or no.')

		if 'y' in confirm.lower():
			del dictionary[name.title()]
		elif 'n' in confirm.lower():
			print(name + '\'s contact info will remain.')
		else:
			print('Error: invalid input')
	except KeyError:
		print('Entry was not found')

	return dictionary
	
def menu(dictionary):
	try:
		print('*'*80 + '\n' + ' Enter 1 to search for a person\'s number \n Enter 2 to add a new contact \n Enter 3 to delete a contact \n Enter 4 to edit a contact \n enter 5 to exit')
		selection = input(' < ')
	except:
		print('Please enter a valid selection.')		
	if selection =='1':
		name = input(' Enter a last name: ')
		name_search(name,dictionary)	
	elif selection =='2':
		dictionary = add_contact(dictionary)
	elif selection =='3':
		dictionary = delete_contact(dictionary)
	elif selection =='4':
		name = input('Enter a last name to edit: ')
		name_search(name,dictionary)
		confirm = input('Do you wish to edit this entry? Enter yes or no: ')
		if 'y' in confirm:
			temp_entry = dictionary[name.title()]
			del dictionary[name.title()]
			new_entry = add_contact(dictionary)
			print('Successfully updated contact info.')
			
		else:
			print('Print improper entry')

	elif selection =='5':
		print('Exiting the dictionary.')
	else:
		print('Error.')

	return selection

selection = ''

dictionary = create_dictionary(file_name)


while True:
#	dictionary = create_dictionary(file_name)
	selection = menu(dictionary)
	if selection == '5':
		break
