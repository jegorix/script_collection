from __future__ import annotations
import pandas as pd
import numpy as np

def add_returns(df: pd.DataFrame) -> pd.DataFrame:
    """Add daily returns to the DataFrame."""
    df = df.copy()
    df['return'] = df.pct_change()
    return df

# def add_returns(df: pd.DataFrame) -> pd.DataFrame:
#     """Add daily returns to the DataFrame."""
#     df = df.copy()
#     for col in df.columns:
#         df[f'return_{col}'] = df[col].pct_change()
#     return df

def returns_stats(df: pd.DataFrame) -> dict[str, float]:
    """Calculate statistics for a series of returns."""
    stats = {
        'mean': float(df['return'].mean()),
        'std': float(df['return'].std()),
        'min': float(df['return'].min()),
        'max': float(df['return'].max()),
        'median': float(df['return'].median()),
        'skew': float(df['return'].skew()),
        'kurtosis': float(df['return'].kurtosis()),
        'sharpe_ratio': float(df['return'].mean() / df['return'].std() * np.sqrt(252) if df['return'].std() != 0 else np.nan),
    }
    return stats


def add_sma(df: pd.DataFrame, windows: list[int] = [7, 30]) -> pd.DataFrame:
    """Add Simple Moving Averages (SMA) to the DataFrame."""
    df = df.copy()
    for window in windows:
        df_sma = df.rolling(window=window).mean()
        df_sma.columns = [f"{col}_SMA_{window}" for col in df.columns]
        df = pd.concat([df, df_sma], axis=1)
    return df



def volatility(df: pd.DataFrame, window: int | None = None) -> float:
    """return STD between Returns"""
    if window:
        return float(df['return'].rolling(window=window).std().iloc[-1])
    return df['return'].std(skipna=True)
    
    
def correlation(df1: pd.DataFrame, df2: pd.DataFrame) -> float:
    """Calculate Return correlation between 2 currencies"""
    merged = pd.merge(df1['date', 'return'], df2['date', 'return'], on='date', suffixes=("_1", "_2"))
    return float(merged['return_1'].corr(merged['return_2']))



def cumulative_returns(df: pd.DataFrame) -> pd.DataFrame:
    """Кумулятивная доходность: (1 + r).cumprod() - 1"""
    return (1 + df['return']).cumprod() - 1



def annualized_volatility(df: pd.DataFrame, perionds_per_year: int = 252) -> pd.Series:
    """Годовая волатильность"""
    return df['return'].std(skipna=True) * (perionds_per_year ** 0.5 )



def sharp_ratio(df: pd.DataFrame, risk_free_rate: float = 0.0) -> pd.Series:
    """Коэффициент Шарпа"""
    excess_returns = df['return'].mean(skipna=True) - risk_free_rate
    return excess_returns / df['return'].std(skipna=True)



def max_drawdown(cumulative: pd.DataFrame) -> pd.Series:
    """Максимальная просадка"""
    drawdown = cumulative / cumulative.cummax() - 1
    return drawdown.min()


if __name__ == '__main__':
    pass