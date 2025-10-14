from __future__ import annotations
import pandas as pd
import numpy as np
from typing import Any

def add_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Добавляет колонку 'return' = дневная доходность.
    """
    df = df.copy()
    df['return'] = df['price'].pct_change()
    return df

def add_sma(df: pd.DataFrame, windows: list[int] = [7, 30]) -> pd.DataFrame:
    """
    Добавляет скользящие средние SMA по указанным окнам.
    """
    df = df.copy()
    for w in windows:
        df[f"SMA_{w}"] = df["price"].rolling(window=w).mean()
    return df
    
def volatility(df: pd.DataFrame) -> pd.DataFrame:
    """
    Возвращает стандартное отклонение доходностей (волатильность).
    """
    return float(df['return'].std(skipna=True))

def correlation(df1: pd.DataFrame, df2: pd.DataFrame) -> float:
    """
    Считает корреляцию доходностей между двумя активами.
    """
    merged = pd.merge(df1['data', 'return'], df2['data', 'return'], on='date', suffixes=("_1", "_2"))
    return float(merged['return_1'].corr(merged['return_2']))

