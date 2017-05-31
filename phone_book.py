import os
run_bool = True
def clear_screen():
    os.system('clear')


class phone_book_entry(object):
    def __init__(self,name, number):
        self.name = name
        self.number = number

def create_entry(name, number, book):
    book[name] = number

def delete_entry(name, book):
    del book[name]

def edit_entry(name,book):
    to_be_edited = name, book[name]




while run_bool:
    print('Commands: (S) search, (C) create, (D) Delete, (E) Edit, (Q) Quit/Exit')
    try:
        selection = input('Enter your command below: \n < ').lower()
    except ValueError:
        print('whoops')
        continue
    if selection == 's':
        query = input('Enter the name you\'d like to search for: ').lower()
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
    #clear_screen()