from __future__ import annotations
from typing import Any, Dict
import json
from pathlib import Path
import pandas as pd
import requests
import time

DATA_DIR = Path("data")
DATA_DIR.mkdir(parents=True, exist_ok=True)

class FetchError(Exception):
    pass

def fetch_coin_market_chart(
    coin_id: str,
    days: int = 90,
    vs_currency: str = "usd",
    interval: str = "daily",
    timeout: int = 10
) -> Dict[str, Any]:
    
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {'vs_currency': vs_currency, 'days': days, 'interval': interval}
    
    try:
        resp = requests.get(url, params=params, timeout=timeout)
        resp.raise_for_status()
        
    except requests.RequestException as exc:
        raise FetchError(f"Request failed: {exc}") from exc
    
    data = resp.json()
    if "prices" not in data:
        raise FetchError("API response doesn't contain 'prices' field")
    
    # Save raw json
    p = DATA_DIR / f"{coin_id}.json"
    
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    return data
        
def prices_json_to_df(data: Dict[str, Any]) -> pd.DataFrame:
    prices = data.get("prices", [])
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df = df.drop(columns=["timestamp"]).sort_values("date").reset_index(drop=True)
    return df

def fetch_and_save_coin(
    coin_id: str, 
    days: int = 90,
    vs_currency: str = 'usd',
    interval: str = 'daily',
    save_csv: bool = True,
    pause_seconds: float = 1.0
) -> pd.DataFrame:
    
    raw = fetch_coin_market_chart(coin_id, days=days, vs_currency=vs_currency, interval=interval)
    df_data = prices_json_to_df(raw)
    if save_csv:
        csv_path = DATA_DIR / f"{coin_id}"
        df_data.to_csv(csv_path, index=False)
    return df_data