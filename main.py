# This is a Python CLI program that will provide weather data for a user-inputted city

# TODO. Get input from the user: "Enter city name: "
# TODO. Build the API URL using the city and your key
# TODO. Make the request: response = requests.get(url)
# TODO. Convert response to JSON: data = response.json()
# TODO. Extract specific fields like data['main']['temp']
# TODO. Print the result: "The temp in Pittsburgh is 45°F"

import os
import requests
from dotenv import load_dotenv
load_dotenv()

#import API key from .env
WEATHER_KEY = os.getenv('WEATHER_API_KEY')

get_city = input("Enter city name: ")

#convert city into coordinates
geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={get_city},&limit=1&appid={WEATHER_KEY}"
geo_response = requests.get(geo_url)
geo_data = geo_response.json()
# print(geo_data)

#safety check
if geo_data:
    lat = geo_data[0]['lat']
    lon = geo_data[0]['lon']
else:
    print("City not found")
    exit()
# weather url
current_weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_KEY}"

#get API data
response = requests.get(current_weather_url)