import os
import openai
import requests
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")  # Add your OpenWeatherMap API key here

# Weather function
def get_weather(city):
    """Fetch the current weather for a city using OpenWeatherMap API."""
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            city_name = data["name"]
            return f"The current weather in {city_name} is {weather} with a temperature of {temp}°C."
        else:
            return f"Unable to fetch weather data for {city}. Please check the city name."
    except Exception as e:
        logging.error(f"Error fetching weather data: {e}")
        return "Error: Unable to fetch weather data."

# Main function for OpenAI with weather functionality
def chat_with_function_calling(user_message):
    """Handle user requests with OpenAI function calling."""
    functions = [
        {
            "name": "get_weather",
            "description": "Get the current weather for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The name of the city to fetch weather for.",
                    }
                },
                "required": ["city"],
            },
        }
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            functions=functions
        )

        if response.choices[0]["finish_reason"] == "function_call":
            function_call = response.choices[0]["message"]["function_call"]
            if function_call["name"] == "get_weather":
                arguments = eval(function_call["arguments"])
                return get_weather(arguments["city"])
        else:
            return response.choices[0]["message"]["content"]
    except Exception as e:
        logging.error(f"Error in OpenAI API call: {e}")
        return "An error occurred while processing your request."

# Test the weather agent
if __name__ == "__main__":
    print("Type your query:")
    user_query = input()
    result = chat_with_function_calling(user_query)
    print("Results:")
    print(result)
