import pandas as pd
import numpy as np
import matplotlib.pyplot as m
import pylab as p
import csv
import glob as glob
import operator
import re, os

def get_file_list():

	file_list = []

	for a_csv_file in glob.glob('*.csv'):
		if 'crime' in a_csv_file:
			file_list.append(a_csv_file)
	return file_list

def import_crime_from_csv(csv_file):
	
	year_stats_csv = pd.read_csv(csv_file,sep=',')
	year_stats     = np.array(year_stats_csv)
	return year_stats

def count_crime(year_stats):
	
	crime_count = {}
	
	for entry in year_stats[:,3]:
		if entry not in crime_count:
			crime_count[entry] = 1
		elif entry in crime_count:
			crime_count[entry] += 1
	total_crime = 0
	
	for crime in crime_count:
		total_crime += crime_count[crime]	

	return crime_count, total_crime

def top_5_crimes(crime_count, file_name):
	year = re.findall(r'\d+',file_name)
	top_5_crimes_untrimmed = sorted(crime_count.items(), reverse = False, key = operator.itemgetter(1))
	
	print('The 5 Least Popular Crimes for ', year, ' were: ', top_5_crimes_untrimmed[0:4])
	
	print('The most popular crime this year was', top_5_crimes_untrimmed[-1], '\n')


os.system('clear')

files = get_file_list()

crime_total_count_by_file = {}

for i in range(len(files)):

	year_stats = import_crime_from_csv(files[i])

	crime_count, total_crime = count_crime(year_stats)
	
	top_5_crimes(crime_count,files[i])
	
	crime_total_count_by_file[files[i]] = total_crime
	
	crime_ranked = sorted(crime_total_count_by_file.items(), key = operator.itemgetter(1))	



print("Total crime by year starting form least to most:")
for pair in crime_ranked: print(re.findall(r'\d+', pair[0]), pair[1])
