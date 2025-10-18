import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

import matplotlib.pyplot as plt
import seaborn as sns
from src.fetch_fx import fetch_and_convert_data
from src.analysis import cumulative_returns, volatility, correlation, add_returns, add_sma
import pandas as pd

def plot_prices(df: pd.DataFrame, currencies: list[str]) -> None:
    """График курсов валют"""
    df[currencies].plot(figsize=(10, 5))
    plt.title("Exchange Rates Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(alpha=0.5)
    plt.legend()
    plt.show()
    
def plot_returns(df: pd.DataFrame, currencies: list[str], title: str = "Daily Returns"):
    """
    Линейный график доходностей.
    """
    plt.figure(figsize=(12, 6))
    for c in currencies:
        df[f"{c}_return"].plot(figsize=(10,4), label=f"{c} return")
        
    plt.xticks(rotation=45)
    plt.locator_params(axis='x', nbins=50)
    plt.locator_params(axis='y', nbins=10)
    plt.grid(alpha=0.5)
        
    plt.title("Daily Returns")
    plt.xlabel("Date")
    plt.ylabel("Return")
    plt.legend()
    plt.show()
    

def plot_cumulative_returns(df: pd.DataFrame, currencies: list[str]):
    """Кумулятивная доходность"""
    for c in currencies:
        cum = cumulative_returns(df, c)
        cum.plot(figsize=(10, 4), label=f"{c} cumulative return")
    plt.title("Cumulative Returns")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.legend()
    plt.show()
    
    

def plot_volatility(df: pd.DataFrame, currencies: list[str], window: int = 30):
    """Скользящая волатильность"""
    for c in currencies:
        vol = df[f"{c}_return"].rolling(window).std()
        vol.plot(figsize=(10, 4), label=f"{c} {window}d volatility")
        
    plt.title(f"Rolling {window}-Day Volatility")
    plt.xlabel("Day")
    plt.ylabel("Volatility")
    plt.legend()
    plt.show()
    
    
    
def plot_sma(df: pd.DataFrame, currency: str, windows: list[int] = [7, 30]):
    """График цены с SMA"""
    df[currency].plot(figsize=(10, 5), label='Price')
    
    for w in windows:
        df[f'{currency}_SMA_{w}'].plot(label=f"SMA {w}")
    
    plt.title(f"{currency} Price with SMA")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()
    
    
    
def plot_correlation_heatmap(df, curriencies: list[str]):
    """Тепловая карта корреляций доходностей"""
    return_cols = [f"{c}_return" for c in curriencies]
    corr = df[return_cols].corr()
    plt.figure(figsize=(6,5))
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title("Correlation of Returns")
    plt.show()



if __name__ == '__main__':
    data = fetch_and_convert_data(symbols=['BYN', 'EUR'])
    data = add_returns(data)
    plot_prices(data, ['USDBYN', 'USDEUR'])
    plot_returns(data, ['USDBYN', 'USDEUR'])
    plot_cumulative_returns(data, ['USDBYN', 'USDEUR'])
    plot_volatility(data, ['USDBYN', 'USDEUR'], window=7)
    
    data = add_sma(data)
    
    plot_sma(data, 'USDBYN')
    plot_correlation_heatmap(data, ['USDBYN', 'USDEUR'])