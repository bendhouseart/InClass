import csv
import pandas
import sys

file_name = sys.argv[1]

try:
	phone_book_file = open(file_name, 'r')
	phone_book = pandas.read_csv(phone_book_file)

except:
	print("Sorry please try again.")

print(phone_book)

for i in range(len(phone_book)):
	print(row(phone_book))
