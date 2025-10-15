from __future__ import annotations
import pandas as pd
import numpy as np

def add_returns(df: pd.DataFrame) -> pd.DataFrame:
    """Add daily returns to the DataFrame."""
    returns = df.pct_change()
    returns = returns.add_suffix("_return")
    df_with_returns = pd.concat([df, returns], axis=1)
    return df_with_returns

def returns_stats(df: pd.DataFrame, currency: str) -> dict[str, float]:
    """Calculate statistics for a series of returns."""
    col = f"{currency}_return"
    stats = {
        'mean': float(df[col].mean()),
        'std': float(df[col].std()),
        'min': float(df[col].min()),
        'max': float(df[col].max()),
        'median': float(df[col].median()),
        'skew': float(df[col].skew()),
        'kurtosis': float(df[col].kurtosis()),
        'sharpe_ratio': float(df[col].mean() / df[col].std() * np.sqrt(252) if df[col].std() != 0 else np.nan),
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



def volatility(df: pd.DataFrame, currency: str, window: int | None = None) -> float:
    """return STD between Returns"""
    col = f"{currency}_return"
    if window:
        return float(df[col].rolling(window=window).std().iloc[-1])
    return df[col].std(skipna=True)
    
    
def correlation(df: pd.DataFrame, currency1: str, currency2: str) -> float:
    """Calculate Return correlation between 2 currencies"""
    col1 = f"{currency1}_return"
    col2 = f"{currency2}_return"
    return float(df[col1].corr(df[col2]))


def cumulative_returns(df: pd.DataFrame, currency: str) -> pd.DataFrame:
    """Кумулятивная доходность: (1 + r).cumprod() - 1"""
    col = f"{currency}_return"
    return (1 + df[col]).cumprod() - 1


def annualized_volatility(df: pd.DataFrame, currency: str, perionds_per_year: int = 252) -> pd.Series:
    """Годовая волатильность"""
    col = f"{currency}_return"
    return df[col].std(skipna=True) * (perionds_per_year ** 0.5 )



def sharpe_ratio(df: pd.DataFrame, currency: str, risk_free_rate: float = 0.0) -> pd.Series:
    """Коэффициент Шарпа"""
    col = f"{currency}_return"
    excess_returns = df[col].mean(skipna=True) - risk_free_rate
    return excess_returns / df[col].std(skipna=True)



def max_drawdown(df: pd.DataFrame, currency: str) -> pd.Series:
    """Максимальная просадка"""
    cum = cumulative_returns(df, currency)
    drawdown = cum / cum.cummax() - 1
    return drawdown.min()


if __name__ == '__main__':
    pass