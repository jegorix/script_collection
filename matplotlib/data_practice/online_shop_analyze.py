import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(51)

# Receive data
df_data = pd.read_csv('content/online_shop_orders.csv')
df_data['revenue'] = df_data['price'] * df_data['quantity']
print(df_data)

# get general user's revenue
general_user_revenue = df_data.groupby('customer').sum(numeric_only=True)['revenue']
print(general_user_revenue)
# pivot_user_revenue = df_data.pivot_table(
#     values='revenue',
#     columns='customer',
#     aggfunc='sum',
#     fill_value=0
# )
# print(pivot_user_revenue)

# average purchase by category
average_order_category = df_data.groupby('category')['revenue'].mean()
print("\nAverage purchase by category")
print(average_order_category)

# plot 

# bar chart with customer's revenue
pivot_customer_revenue = df_data.pivot_table(
    values='revenue',
    columns='customer',
    aggfunc='sum',
    fill_value=0
)

ax1 = pivot_customer_revenue.plot(
    kind='bar',
    figsize=(10, 6),
    colormap='tab20'
)

ax1.set_title("Customer's Revenue")
ax1.set_xlabel('Customer')
ax1.set_ylabel('Revenue')
ax1.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=True, ticks=(0, 0))
plt.tight_layout()
plt.show()

# PIE PLOT % of category in revenue
category_revenue = df_data.groupby('category').sum(numeric_only=True)['revenue']
fig, ax = plt.subplots(figsize=(10, 6))
ax.pie(category_revenue.values, labels=category_revenue.index.astype(str), autopct='%1.1f%%', startangle=90)
ax.set_title('Share of category in whole revenue', fontsize=14)
plt.tight_layout()
plt.show()

# Numpy метрики

# Общая медиана всех заказов
median_price = np.median(df_data['revenue'])
print(f"Медиана суммы заказов: {median_price}")

# Стандартное отклонение заказов
std_price = np.std(df_data['revenue'])
print(f"Стандартное отклонение заказов: {std_price:.2f}")
