# This is a Python CLI program that will provide temperature data for a user-input city

# Get input from the user: "Enter city name: "
# Build the API URL using the city and your key
# Make the request: response = requests.get(url)
# Convert response to JSON: data = response.json()
# Extract specific fields like temp, conditions, rain, etc

import os
import requests
from dotenv import load_dotenv
load_dotenv()
# import API key from .env (.env part of gitignore for API key security)
WEATHER_KEY = os.getenv('WEATHER_API_KEY')

# main loop
while True:

    get_city = input("Enter city name or type 'exit' to quit: ")
    if get_city.lower() == 'exit':
        exit()
    else:
        #convert city into coordinates
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={get_city},&limit=1&appid={WEATHER_KEY}"
        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()
        # print(geo_data)

        #safety check
        if geo_data:
            lat = geo_data[0]['lat']
            lon = geo_data[0]['lon']
            print(f"Coordinates found for {get_city.title()}: Latitude: {lat}, Longitude: {lon}")
        else:
            print("City not found. Please try again")
            continue
        # weather url
        current_weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={WEATHER_KEY}"

        #get API data
        weather_response = requests.get(current_weather_url)
        weather_data = weather_response.json()

        temp = weather_data['main']['temp'] # main is a json dictionary
        feels_like = weather_data['main']['feels_like']
        conditions = weather_data['weather'][0]['main'] # weather is a list so must index it with 0

        print(f"Weather conditions for {get_city}:\nCurrent temperature: {temp}°F\nFeels like: {feels_like}°F\nConditions: {conditions}")
        continue

