"""Модуль для получения курсов валют"""
import sys
from pathlib import Path
import requests
import pandas as pd
from datetime import datetime

# добавил корень проекта в sys.path (меньше ошибок)
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from config import EXCHANGE_API_URL, CURRENCY_BASE, CURRENCY_SYMBOLS

def fetch_rates(base: str = CURRENCY_BASE, symbols: list | None = None, timeout: int = 10) -> pd.DataFrame:
    """Запрашивает курсы и возвращает DataFrame с одной строкой."""

    symbols = symbols or CURRENCY_SYMBOLS
    
    # делаю запрос
    params = {
        'base': base,
        'symbols': ",".join(symbols)
    }
    
    resp = requests.get(url=EXCHANGE_API_URL, params=params, timeout=timeout)
    resp.raise_for_status() # если статус не 200 то кидаем ошибку
    data = resp.json()
    
    # итоговый словарь
    row = {
        'Дата': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'base': base
    }
    
    
    rates = data.get("rates", {})  # берем словарь с цифрами
    for s in symbols:
        row[f"{base}->{s}"] = rates.get(s)
        
    df = pd.DataFrame([row])
    return df