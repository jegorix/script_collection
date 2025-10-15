from __future__ import annotations
from typing import Dict, Any, Sequence
import requests
import json
from pathlib import Path
import pandas as pd
import os 
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True, parents=True)

class FetchError(Exception):
    pass

def fetch_fx_data(
    base: str,
    symbols: Sequence[str],
    start_date: str,
    end_date: str,
    api_key: str | None = os.getenv("EXCHANGE_RATE_API_KEY"),
    save_json: bool = True,
    timeout: int = 10,  
) -> Dict[str, Any]:
    
    # access_key  [Required] Your API Access Key.
    # start_date  [Required] Specify the start date of your time frame.
    # end_date	  [Required] Specify the end date of your time frame.
    # source      [optional] Specify a Source Currency other than the default USD. Supported on the Basic Plan and higher.
    # currencies  [optional] Specify a comma-separated list of currency codes to limit your API response to specific currencies.
    
    url = "https://api.exchangerate.host/timeframe"
    params = {
        'access_key': api_key,
        'start_date': start_date,
        'end_date': end_date, 
        'source': base,
        'currencies': ",".join(symbols)
    }
    
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        raise FetchError(f"Error fetching data: {e}")
    
    if not data.get("success", True) and "rates" not in data:
         raise FetchError("API не вернул поле 'rates'")
        
    if save_json:
        path = DATA_DIR / f"{base}_{'_'.join(symbols)}_{start_date}_{end_date}.json"
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    return data


def fx_json_to_df(data: Dict[str, Any]) -> pd.DataFrame:
    """
    Преобразует data['rates'] -> DataFrame с индексом Date и колонками валют.
    """
    rates: Dict[str, Dict[str, float]] = data.get("quotes", {})
    df = pd.DataFrame.from_dict(rates, orient='index')
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    # df = df.reset_index().rename(columns={'index': 'date'})
    return df

def fetch_and_convert_data(
    base: str = 'USD',
    start_date: str = '2025-01-01',
    end_date: str = '2025-01-30',
    symbols: list[str] = ['EUR']
    ) -> pd.DataFrame:
    """
    Point of entering
    """
    json_data: Dict[str, Any] = fetch_fx_data(
        base=base,
        start_date=start_date,
        end_date=end_date,
        symbols=symbols
    )
    # print(json_data)
    
    df_result: pd.DataFrame = fx_json_to_df(json_data)
    
    return df_result
    
    

if __name__ == '__main__':
    df = fetch_and_convert_data()
    print(df)