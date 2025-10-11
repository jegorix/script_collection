import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range(start='2023-10-01', periods=30)

store_a = pd.DataFrame(data={
    'store': 'Store-A',
    'date': dates,
    'laptops': np.random.randint(0, 21, size=30),
    'tablets': np.random.randint(0, 16, size=30),
    'phones': np.random.randint(10, 51, size=30),
})

store_b = pd.DataFrame(data={
    'store': 'Store-B',
    'date': dates,
    'laptops': np.random.randint(0, 21, size=30),
    'tablets': np.random.randint(0, 16, size=30),
    'phones': np.random.randint(10, 51, size=30),
})

df_stores = pd.concat([store_a, store_b], ignore_index=True)

df_stores['revenue'] = df_stores['laptops'] * 1000 + df_stores['tablets'] * 700 + df_stores['phones'] * 500
print(df_stores)


# day with highest revenue
highest_revenue_day = df_stores.loc[df_stores.groupby('store')['revenue'].idxmax()]
print('Cамый прибыльный день для каждого магазина')
print(highest_revenue_day[['store', 'date', 'revenue']])

# plot
df_store_a = df_stores[df_stores['store'] == 'Store-A']
df_store_b = df_stores[df_stores['store'] == 'Store-B']

fig, ax1 = plt.subplots(figsize=(10,6))

# axis for revenue
ax1.plot(df_store_a['date'], df_store_a['revenue'], color='red', marker='o', label='Store-A revenue')
ax1.plot(df_store_b['date'], df_store_b['revenue'], color='blue', marker='s', label='Store-B revenue')
ax1.set_xlabel('Date')
ax1.set_ylabel('Revenue')
ax1.tick_params(axis='y', labelcolor='red')

# axis for phone bars
ax2 = ax1.twinx()
ax2.bar(df_store_a['date'], df_store_a['phones'] * 700, color='red', alpha=0.3, label='Store-A phones')
ax2.bar(df_store_b['date'], df_store_b['phones'] * 700, color='blue', alpha=0.3, label='Store-B phones')
ax2.set_ylabel('phones revenue')
ax2.tick_params(axis='y', labelcolor='blue')

# plot title and legend
plt.title('Compare sales of Store-A and Store-B')
fig.tight_layout()
fig.legend(loc="upper right", bbox_to_anchor=(0.9, 0.9))
plt.show()