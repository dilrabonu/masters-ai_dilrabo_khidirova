import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    if not api_key:
        return "OpenWeatherMap API key not found"
    
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad responses
        data = response.json()
        if data.get("weather"):
            return f"The weather in {city} is {data['weather'][0]['description']} with a temperature of {data['main']['temp']}°C."
        else:
            return "Unable to fetch weather information."
    except requests.RequestException as e:
        return f"Error fetching weather: {e}"