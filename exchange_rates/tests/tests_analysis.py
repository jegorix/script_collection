import sys
from pathlib import Path
from pprint import pprint

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.analysis import *
from src.fetch_fx import fetch_and_convert_data

data = fetch_and_convert_data()

print("""\nAdd daily returns to the DataFrame.""")
df_data = add_returns(data)
print(df_data)

print("""\nCalculate statistics for a series of returns.""")
pprint(returns_stats(df_data), indent=4, sort_dicts=False)

print("""\nAdd Simple Moving Averages (SMA) to the DataFrame.""")
pprint(add_sma(df_data))

print("""\nReturn STD between Returns""")
pprint(float(volatility(df_data)))

# print("""\nCalculate Return correlation between 2 currencies""")
# print(float(correlation(df_data, df_data)))

print("""\nКумулятивная доходность: (1 + r).cumprod() - 1""")
pprint(cumulative_returns(df_data))

print("""\nГодовая волатильность""")
pprint(float(annualized_volatility(df_data)))


print("""\nКоэффициент Шарпа""")
pprint(float(sharp_ratio(df_data)))

print("""\nМаксимальная просадка""")
pprint(max_drawdown(df_data))