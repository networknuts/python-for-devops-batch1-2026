import requests
import sys

api_key = "abcd"
country_code = input("Enter your country code: ")
zip_code = input("Enter your zip code: ")

weather_url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key}"

response = requests.get(weather_url)

if response.status_code == 200:
    print(response.json())
else:
    print("Error: Something went wrong.\nPlease try again.")
    sys.exit(1)
