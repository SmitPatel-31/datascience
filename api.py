# use urllib
from urllib import urlopen
# weather api
whether_api = "http://api.openweathermap.org/data/2.5/weather?q=London&appid=e3175df7e5869596f69b5c848a2e499d"
# url open
weather_data=urlopen(whether_api)
# 
print(type(weather_data))
# to read the data 
weathe_print=weather_data.read()

import json
# print json data
json_data=json.loads(weathe_print)
# if we want only one parameter result
print(json_data['name'])
# conver in string
json_string=json.dumps(json_data)

print(json_string)
