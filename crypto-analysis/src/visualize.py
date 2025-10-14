from __future__ import annotations
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional


def plot_price(df: pd.DataFrame, title: str = "Price with SMA") -> None:
    """
    Строит график цен с наложением скользящих средних.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['price'], label='Price', color='blue')
    
    sma_cols = [col for col in df.columns if col.startswith('SMA_')]
    for col in sma_cols:
        plt.plot(df['date'], df[col], label=col)
        
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(alpha=0.5)
    plt.show()
    

def plot_returns(df: pd.DataFrame, title: str = "Daily Returns") -> None:
    """
    Линейный график доходностей.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['return'], label='Return', color='orange')
    plt.axhline(0, color='black', linestyle='--', alpha=0.7)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Return')
    plt.legend()
    plt.grid(alpha=0.5)
    plt.show()
    
    
def plot_return_distribution(df: pd.DataFrame, title: str = "Distribution of Return"):
    """
    Гистограмма распределения доходностей.
    """
    plt.figure(figsize=(8, 5))
    sns.histplot(df['return'].dropna(), bins=50, kde=True, color='purple')
    plt.title(title)
    plt.xlabel('Return')
    plt.ylabel('Frequency')
    plt.grid(alpha=0.5)
    plt.show()
    

def plot_correlation_heatmap(dfs: dict[str, pd.DataFrame], title: str = 'Correlation Heatmap') -> None:
    """
    Тепловая карта корреляций доходностей нескольких активов.
    dfs — словарь вида {"BTC": df_btc, "ETH": df_eth, ...}
    """
    returns = {}
    for name, df in dfs.items():
        returns[name] = df['return']
        
    corr_df = pd.DataFrame(returns).corr()
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_df, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
    plt.title(title)
    plt.show()
        
   