import sys
from pathlib import Path
from pprint import pprint

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.analysis import *
from src.fetch_fx import fetch_and_convert_data

# Загружаем данные
data = fetch_and_convert_data(base='USD', symbols=['BYN', 'EUR'])

# 1. Добавляем доходности
print("\nAdd daily returns to the DataFrame.")
df_data = add_returns(data)
print(df_data.head())

# Доступные валюты
print("\nAvailable columns:", list(df_data.columns))

# 2. Статистика доходностей по EUR и BYN
print("\nCalculate statistics for USDEUR and USDBYN returns.")
eur_stats = returns_stats(df_data, "USDEUR")
byn_stats = returns_stats(df_data, "USDBYN")
pprint({"USDEUR": eur_stats, "USDBYN": byn_stats}, indent=4, sort_dicts=False)

# 3. Добавляем SMA
print("\nAdd Simple Moving Averages (SMA) to the DataFrame.")
df_sma = add_sma(df_data)
print(df_sma.head())

# 4. Волатильность
print("\nReturn STD between Returns")
print(f"USDEUR volatility: {volatility(df_data, 'USDEUR')}")
print(f"USDBYN volatility: {volatility(df_data, 'USDBYN')}")

# 5. Корреляция доходностей
print("\nCalculate Return correlation between USDEUR and USDBYN")
print(correlation(df_data, "USDEUR", "USDBYN"))

# 6. Кумулятивная доходность
print("\nCumulative returns")
print(cumulative_returns(df_data, "USDEUR").head())
print(cumulative_returns(df_data, "USDBYN").head())

# 7. Годовая волатильность
print("\nAnnualized volatility")
print(f"USDEUR: {annualized_volatility(df_data, 'USDEUR')}")
print(f"USDBYN: {annualized_volatility(df_data, 'USDBYN')}")

# 8. Sharpe Ratio
print("\nSharpe ratio")
print(f"USDEUR: {sharpe_ratio(df_data, 'USDEUR')}")
print(f"USDBYN: {sharpe_ratio(df_data, 'USDBYN')}")

# 9. Максимальная просадка
print("\nMax drawdown")
print(f"USDEUR: {max_drawdown(df_data, 'USDEUR')}")
print(f"USDBYN: {max_drawdown(df_data, 'USDBYN')}")