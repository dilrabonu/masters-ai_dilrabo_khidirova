import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_exchange_rate(base_currency, target_currency):
    api_key = os.getenv('EXCHANGERATE_API_KEY')
    if not api_key:
        return "Exchange Rate API key not found"
    
    api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        
        if data['result'] == 'success' and target_currency in data['conversion_rates']:
            rate = data['conversion_rates'][target_currency]
            return f"1 {base_currency} = {rate} {target_currency}"
        else:
            return f"Exchange rate for {base_currency} to {target_currency} not found"
    except requests.RequestException as e:
        return f"Error fetching exchange rate: {e}"