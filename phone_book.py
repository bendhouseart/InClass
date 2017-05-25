import os

run_bool = True
import csv

with open('MOCK_DATA.csv', 'r') as datafile:
    book = csv.DictReader(datafile)
    for row in book:
        print('first name {}, last name {}, number {}'.format(row['first_name'], row['last_name'], row['phone']))


# def search():
#     name = input('enter a first name:  ')
#     for n in book:
#         for x in n:
#             if name in n['first_name']:
#                 print('first {}, last{}'.format(n['first_name'], n['last_name']))
#             else:
#                 print('name not found')


print(book['Vilma'])


def __init__(self, name, number):
    self.name = name
    self.number = number


def create_entry(name, number, book):
    book[name] = number


def delete_entry(name, book):
    del book[name]


def edit_entry(name, book):
    to_be_edited = name, book[name]


while run_bool:
    print('Commands: (S) search, (C) create, (D) Delete, (E) Edit, (Q) Quit/Exit')
    try:
        selection = input('Enter your command below: \n < ').lower()
    except ValueError:
        print('whoops')
        continue
    if selection == 's':
        # query = input('Enter the name you\'d like to search for: ').lower()
        search()
    elif selection == 'c':
        name = input('Enter the first name of the contact you\'d like to create: ')
    elif selection == 'e':
        name = input('Enter the name of the contact you\'d like to edit: ')
    elif selection == 'd':
        name = input('Enter the name of the contact you\'d like to delete: ')
    elif selection == 'q':
        quit()
    else:
        print('Please enter a selection from the menu given above.')
        # clear_screen()
