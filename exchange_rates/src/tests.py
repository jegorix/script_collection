from __future__ import annotations
from typing import Any
import requests
import json
import os 
from dotenv import load_dotenv

load_dotenv()

class FetchError(Exception):
    pass

    
def get_response(api_key: str) -> dict[str, Any]:
    url = "https://api.exchangerate.host/live"
    params = {
        'access_key': api_key
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise FetchError(f"Error fetching data: {e}")
    
    data = response.json()
    
    if not data.get("success", False):
        raise FetchError(f"API error: {data.get('error', 'Unknown error')}")
    
    return data


if __name__ == '__main__':
    api_key = os.getenv("EXCHANGE_RATE_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set the EXCHANGE_RATE_API_KEY environment variable.")
    response = get_response(api_key)
    print(response)