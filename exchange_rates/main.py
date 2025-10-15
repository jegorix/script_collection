import sys
from pathlib import Path
from pprint import pprint

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.analysis import *
from src.visualizer import *
from src.fetch_fx import fetch_and_convert_data


def run_analyze():
    data = fetch_and_convert_data(base='USD',
                                  start_date='2024-01-01',
                                  end_date='2025-01-01',
                                  symbols=['BYN', 'EUR']
                                  )
    print("\nRaw exchange rates:")
    print(data.head())
    
    # 2. Добавляем доходности
    df_returns = add_returns(data)
    print("\nData with daily returns:")
    print(df_returns.head())
    
    # 3. Добавляем SMA
    df_sma = add_sma(df_returns, windows=[7, 30])
    print("\nData with SMA:")
    print(df_sma.head())
    
    # 4. Статистика доходностей
    print("\nReturns statistics:")
    byn_stats = returns_stats(df_returns, 'USDBYN')
    eur_stats = returns_stats(df_returns, 'USDEUR')
    pprint({"USDBYN": byn_stats, "USDEUR": eur_stats}, indent=4, sort_dicts=False)

    # 5. Волатильность
    print("\nVolatility:")
    print(f"USDBYN: {volatility(df_returns, 'USDBYN')}")
    print(f"USDEUR: {volatility(df_returns, 'USDEUR')}")
    
    # 6. Корреляция доходностей
    print("\nCorrelation between USDBYN and USDEUR:")
    print(correlation(df_returns, 'USDBYN', 'USDEUR'))
    
    # 7. Кумулятивная доходность
    print("\nCumulative returns:")
    print("USDBYN:")
    print(cumulative_returns(df_returns, 'USDBYN').head())
    print("USDEUR:")
    print(cumulative_returns(df_returns, 'USDEUR').head())
    
    # 8. Годовая волатильность
    print("\nAnnualized volatility:")
    print(f"USDBYN: {annualized_volatility(df_returns, 'USDBYN')}")
    print(f"USDEUR: {annualized_volatility(df_returns, 'USDEUR')}")
    
    # 9. Sharpe Ratio
    print("\nSharpe Ratio:")
    print(f"USDBYN: {sharpe_ratio(df_returns, 'USDBYN')}")
    print(f"USDEUR: {sharpe_ratio(df_returns, 'USDEUR')}")
    
    # 10. Max Drawdown
    print("\nMax Drawdown:")
    print(f"USDBYN: {max_drawdown(df_returns, 'USDBYN')}")
    print(f"USDEUR: {max_drawdown(df_returns, 'USDEUR')}")
    
    
    # 11. Построение графиков
    plot_prices(data, ['USDBYN', 'USDEUR'])
    plot_returns(df_returns, ['USDBYN', 'USDEUR'])
    plot_cumulative_returns(df_returns, ['USDBYN', 'USDEUR'])
    plot_volatility(df_returns, ['USDBYN', 'USDEUR'], window=30)
    plot_sma(df_sma, 'USDBYN', windows=[7,30])
    plot_sma(df_sma, 'USDEUR', windows=[7,30])
    plot_correlation_heatmap(df_returns, ['USDBYN', 'USDEUR'])


if __name__ == '__main__':
    run_analyze()