from decouple import config

# pip install pyowm
from langchain.utilities import OpenWeatherMapAPIWrapper

weather_util = OpenWeatherMapAPIWrapper(
    openweathermap_api_key=config("OPENWEATHERMAP_API_KEY"))

weather_data = weather_util.run("Nairobi, Kenya")
print(weather_data)
