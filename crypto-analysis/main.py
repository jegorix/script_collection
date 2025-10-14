from __future__ import annotations
import pandas as pd

from src.fetch_data import fetch_and_save_coin
from src.analysis import add_returns, add_sma, volatility
from src.visualize import(
    plot_price,
    plot_returns,
    plot_correlation_heatmap,
    plot_return_distribution
)


def run_analysis() -> None:
    # Load data
    btc_df = fetch_and_save_coin("bitcoin", days=365)
    eth_df = fetch_and_save_coin("ethereum", days=365)
    
    # add Return and SMA
    btc_df = add_returns(add_sma(btc_df))
    eth_df = add_returns(add_sma(eth_df))
    
    # calculate volitility
    btc_vol = volatility(btc_df)
    eth_vol = volatility(eth_df)
    
    print(f"Волатильность BTC: {btc_vol:.2%}")
    print(f"Волатильность ETH: {eth_vol:.2%}")
    
    # Create plots
    plot_price(btc_df)
    plot_returns(btc_df)
    plot_return_distribution(btc_df)
    
    # Correlations
    dfs: dict[str, pd.DataFrame] = {"BTC": btc_df, "ETH": eth_df}
    plot_correlation_heatmap(dfs)
    
    # Save eventual data to csv
    btc_df.to_csv("data/btc_analysis.csv", index=False)
    eth_df.to_csv("data/eth_analysis.csv", index=False)
    print("✅ Данные сохранены в data/btc_analysis.csv и data/eth_analysis.csv")
    
    
if __name__ == '__main__':
    run_analysis()