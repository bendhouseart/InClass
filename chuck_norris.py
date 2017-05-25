# In this program we will provide the user with temperature in
# either celsius or farenheit (per their request) and provide
# them with the current conditions outside of the location they
# provide via either zip code or city, state etc...

import requests
from json import *

package = {
	'APPID': '0de4ba8217e33c57978bb8286eeef89e',
	'q': 'Portland'
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

# here we are stripping the [] from weather, or converting the string into it's
# dictionary form.
cloud_cover = weather[0]

# now that we've converted weather from a string into a dict we can use a key
# to request information as such.
conditions = cloud_cover['main']

print(conditions)

#temp = weather['main'['temp']]

#print(json_data)

print(weather)
