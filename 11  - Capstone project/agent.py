import os
import pandas as pd
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAI
from weather_tool import get_weather
from currency_tool import get_exchange_rate

# Load environment variables
load_dotenv()

# Read data
data = pd.read_csv("data.csv")

# Initialize LLM with environment variable for API key
llm = ChatOpenAI(
    temperature=0.7, 
    model_name="gpt-4", 
    openai_api_key=os.getenv('OPENAI_API_KEY')
)

def process_query(query):
    query = query.lower()
    try:
        if "shipment" in query:
            # Extract shipment ID, handle potential errors
            parts = query.split()
            shipment_id = parts[-1] if len(parts) > 1 else None
            return get_shipment_status(shipment_id) if shipment_id else "Invalid shipment query"
        
        elif "exchange rate" in query:
            # More robust currency extraction
            parts = query.split()
            if len(parts) >= 4:
                base_currency = parts[-2].upper()
                target_currency = parts[-1].upper()
                return get_exchange_rate(base_currency, target_currency)
            return "Invalid currency exchange query"
        
        elif "weather" in query:
            # Extract city name
            parts = query.split()
            city = parts[-1] if len(parts) > 1 else None
            return get_weather(city) if city else "Please specify a city"
        
        else:
            # Default to LLM response
            return llm(query)
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

def get_shipment_status(shipment_id):
    try:
        row = data[data["ShipmentID"] == shipment_id]
        if not row.empty:
            return f"Shipment {shipment_id} status: {row.iloc[0]['Status']}"
        return "Shipment not found."
    except Exception as e:
        return f"Error retrieving shipment status: {str(e)}"