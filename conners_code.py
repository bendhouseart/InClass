import csv

phonebook = {'Kieran' : {'name': 'Kieran','number' : 8456331959, 'phrase': 'Good code is not written, it\s re-written.'}
            ,'Lambda': {'name': 'Lambda', 'number':8454185633,'phrase':'I am a robut.'}}

running = True

while running:
    search_or_quit = True
    while search_or_quit:
        try:
            query = int(input('E000000nter 1 to search phonebook, or 2 to quit'))

        except ValueError:
            print("Input must be a number")
            continue

        if query == 1:
            search_or_quit = False
        elif query == 2:
            quit()
        else:
            print("I did not understand that.")

    searching = True
    while searching:
        with open('MOCK_DATA.csv','r') as userFile:
            userFileReader = csv.reader(userFile)
            search = input('enter a name, phone number (with correct punctuation), or phrase')
            for line in userFileReader:
                for index in line:
                    if search in index:
                        with open('mostRecentSearch.csv', 'w') as newFile:
                            newFileWriter = csv.writer(newFile)
                            newFileWriter.writerow(line)

                            print('You might be looking for' + str(line))
    for line in userFileReader:
        print(line)