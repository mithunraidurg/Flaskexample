from dotenv import load_dotenv
#from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Mumbai"):
    #https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=96a5190272ffacc381872c116f7a3cb2
    request_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={os.getenv("API_KEYS")}'
    print("API_KEYS: "+os.getenv("API_KEYS"))
    print(f"request_Url: {request_url}")

    weather_data = requests.get(request_url).json()
    print(f"weather_data: {weather_data}")

    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    # Check for empty strings or string with only spaces
    # This step is not required here
    # if not bool(city.strip()):
    #     city = "Kansas City"

    weather_data = get_current_weather(city)

    print("\n")
    print(weather_data)
