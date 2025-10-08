"""Модуль для получения курсов валют"""
import sys
from pathlib import Path
import requests
import pandas as pd
from datetime import datetime

# Добавляем корень проекта в sys.path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from config import EXCHANGE_API_URL, EXCHANGE_API_KEY, CURRENCY_BASE, CURRENCY_SYMBOLS

def fetch_rates(base: str = CURRENCY_BASE, symbols: list | None = None, timeout: int = 10) -> pd.DataFrame:
    """Запрашивает курсы и возвращает DataFrame с одной строкой."""
    symbols = symbols or CURRENCY_SYMBOLS

    url = f"{EXCHANGE_API_URL}{EXCHANGE_API_KEY}/latest/{base}"

    resp = requests.get(url=url, timeout=timeout)
    resp.raise_for_status() 
    data = resp.json()

    if data.get("result") != "success":
        raise ValueError(f"Ошибка API: {data.get('error-type', 'Неизвестная ошибка')}")

    rates = data.get("conversion_rates", {})
    if not rates:
        raise ValueError("Курсы валют не найдены в ответе API")

    row = {
        'Дата': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'base': base
    }
    for s in symbols:
        if s in rates:
            row[f"{base}->{s}"] = rates[s]
        else:
            row[f"{base}->{s}"] = None  # мб валюта не поддерживается
            print(f"Валюта {s} не найдена в ответе API")

    df = pd.DataFrame([row])
    return df

if __name__ == "__main__":
    df = fetch_rates()
    print(df)