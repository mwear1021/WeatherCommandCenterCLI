# Weather Command Center CLI

## Description

A simple command-line interface (CLI) program that fetches and displays current weather information for a user-specified city using the OpenWeatherMap API.

## Features

- Get current temperature, feels-like temperature, and weather conditions
- Interactive CLI with loop for multiple queries
- Type 'exit' to quit

## Prerequisites

- Python 3.x
- OpenWeatherMap API key (free tier available)

## Installation

1. Clone or download this repository.
2. Install required packages:
   ```
   pip install requests python-dotenv
   ```

## Setup

1. Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api).
2. Create a `.env` file in the project root.
3. Add your API key to the `.env` file:
   ```
   WEATHER_API_KEY=your_api_key_here
   ```
4. Ensure `.env` is in your `.gitignore` to keep your key secure!!!

## Usage

Run the program:
```
python main.py
```

Enter a city name when prompted. The program will display the weather information.

Example:
```
Enter city name or type 'exit' to quit: New York
Coordinates found for New York: Latitude: 40.7128, Longitude: -74.0060
Weather conditions for New York:
Current temperature: 72°F
Feels like: 75°F
Conditions: Clear
```

## License

This project is open source. Feel free to use and modify.