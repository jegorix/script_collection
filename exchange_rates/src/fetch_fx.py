from __future__ import annotations
from typing import Dict, Any, Sequence
import requests
import json
import pathlib as Path

import os 


DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True, parents=True)

class FetchError(Exception):
    pass

# def fetch_fx_data(
#     base: str,
#     symbols: Sequence[str],
#     start_date: str,
#     end_date: str,
#     save_json: bool = True,
#     timeout: int = 10,  
# ) -> Dict[str, Any]:
    
def get_response(api_key) -> dict[str, Any]:
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
    api_key = None