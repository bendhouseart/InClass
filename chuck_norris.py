# In this program we will provide the user with temperature in
# either celsius or farenheit (per their request) and provide
# them with the current conditions outside of the location they
# provide via either zip code or city, state etc...

from scipy.constants import convert_temperature as convert
import requests
from json import *

# this def will get the users location
def GetLoc():
	while True:
		
		loc_string = input("Enter the location you wish to know the current weather for: ")

		try:
			loc_string = int(loc_string)
			zip_or_city_state = 'zip'
			loc_string = str(loc_string)
		except ValueError:
			zip_or_city_state = 'q'		

		temp_string = input("Enter F for Fahrenheit or C for Celsius: ").lower()
	
		if 'f' in temp_string:
			temp = 'Fahrenheit'
			break
		elif 'c' in temp_string:
			temp = 'Celsius'
			break
		else:
			print("enter something that isn't shit.")

	return loc_string, zip_or_city_state, temp

loc_string, zip_or_city_state, temp = GetLoc()



package = {
	'APPID': '0de4ba8217e33c57978bb8286eeef89e',
	zip_or_city_state : loc_string 
}

r = requests.post('http://api.openweathermap.org/data/2.5/weather',params=package)

# pulling information requested into a json object
json_data = r.json()

# pulling weather out of the json object weather contains the following
# descriptors: id, main, description, icon
# main is a one word descriptor of curent conditions
# descripition is a brief description of current conditions
# the previous two are the only ones that your interested in for this
# exercise
weather = json_data['weather']
temperature = float(json_data['main']['temp'])

# here we are stripping the [] from weather, or converting the string into it's
# dictionary form.
conditions = weather[0]['main']

# Temperature conversion takes input float or int and converts
# from second arg's units to third args units
temperature = convert(temperature, 'kelvin',temp)


print('\n' + '*'*80)
print('Current conditions and temperature for: {} are {} and {} degrees {}'.format(str(loc_string), str(conditions),str(temperature),str(temp)))
print('*'*80)
#print(loc_string)
#print(conditions)
#rint(temperature)
#print(temp)
