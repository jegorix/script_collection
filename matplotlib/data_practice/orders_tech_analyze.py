import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df_orders = pd.read_csv('content/orders.csv')
df_orders['total_price'] = df_orders['quantity'] * df_orders['price']
df_orders['date'] = pd.to_datetime(df_orders['date'])

# day of week prepare
df_orders['day_of_week'] = df_orders['date'].dt.day_name()



print(df_orders.head(5))

# Statistics
print("\nTotal revenue:")
print(df_orders['total_price'].sum())

print("\nCount of unique customers:")
print(df_orders['customer_id'].nunique())

print("\nAverage price of order")
print(df_orders['total_price'].mean())

print("\nMedian order price")
print(df_orders['total_price'].median())

print('\nStandart deviation')
print(f"{df_orders['total_price'].std():.6}")

# Analytics by category

# total_price by category
category_revenue = df_orders.groupby('category').sum(numeric_only=True)['total_price']
print('\nTotal price by category')
print(category_revenue)

# average order by category
category_average_order = df_orders.groupby('category')['total_price'].mean()
print('\nAverage order by category')
print(category_average_order)


# General plot field
fig, ax = plt.subplots(3, 3, figsize=(14, 10))


# bar chart with categories revenue
ax[0, 0].bar(category_revenue.index, category_revenue.values)
ax[0, 0].set_title('Выручка по категориям', fontsize=14)
ax[0, 0].set_xlabel('Category')
ax[0, 0].set_ylabel('Revenue')
ax[0, 0].grid(True, linestyle='--', alpha=0.6)


# Time analytics
# Динамика выручки по месяцам + график
monthly_revenue = df_orders.groupby(df_orders['date'].dt.to_period('M')).sum(numeric_only=True)['total_price']
# revenue dynamic plot
ax[1, 0].plot(monthly_revenue.index.astype(str), monthly_revenue.values, marker='o', color='green')
ax[1, 0].set_title('Динамика выручки по месяцам')
ax[1, 0].set_xlabel('Месяц')
ax[1, 0].set_ylabel('Выручка')
ax[1, 0].grid(True, linestyle='--', alpha=0.6)

print("\nМесяц с наибольшими продажами:")
print(monthly_revenue.loc[monthly_revenue == monthly_revenue.max()])



# Top products and customers
products_revenue = df_orders.groupby('product').sum(numeric_only=True)['total_price'].sort_values(ascending=False).head(5)
print("\nТоп-5 товаров по общей выручке:")
print(products_revenue)

customers_revenue = df_orders.groupby('customer_id').sum(numeric_only=True)['total_price'].sort_values(ascending=False).head(5)
print("\nТоп-5 клиентов по общей сумме покупок:")
print(customers_revenue)


# barH for products and users
ax[0, 1].barh(products_revenue.index, products_revenue.values)
ax[0, 1].set_title('Топ-5 товаров по общей выручке.')
ax[0, 1].set_xlabel('Товар')
ax[0, 1].set_ylabel('Выручка')
ax[0, 1].grid(True, linestyle='--', alpha=0.6)


ax[1, 1].barh(customers_revenue.index, customers_revenue.values)
ax[1, 1].set_title('Топ-5 товаров по общей выручке.')
ax[1, 1].set_xlabel('Клиент')
ax[1, 1].set_ylabel('Сумма покупок')
ax[1, 1].grid(True, linestyle='--', alpha=0.6)

# box plot for total_price
df_orders.boxplot(column='total_price', by='category', ax=ax[2, 0], 
                  patch_artist=True, boxprops=dict(facecolor='lightyellow', color='orange'),
                  medianprops=dict(color='red', linewidth=2 )
                  )
ax[2, 0].set_title('Boxplot для итоговой цены')
ax[2, 0].set_ylabel('Цена')
ax[2, 0].grid(True, linestyle='--', alpha=0.6)
ax[2, 0].showfliers = True

# pie chart for categories
ax[2, 1].pie(category_revenue.values, labels=category_revenue.index.astype(str), 
             autopct="%1.1f%%", startangle=90, explode=(0, 0, 0, 0, 0))
ax[2, 1].set_title("Распределение выручки по категориям")


# heatmap
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
pivot_day_order = df_orders.pivot_table(
    index='day_of_week',
    values='quantity',
    aggfunc='sum',
    fill_value=0
)

sns.heatmap(pivot_day_order.values,
            annot=True,
            fmt='d',
            cmap='YlOrRd',
            xticklabels=['Заказы'],
            yticklabels=days_order,
            ax=ax[2,2]
)
ax[2, 2].set_title('Количество заказов по дням недели')


plt.xticks(rotation=True)
plt.tight_layout()
plt.show()

# Correlation between quantity and price
cor_quantity_price = np.corrcoef(df_orders['quantity'], df_orders['price'])
print('\nКорреляция между количеством товара и его ценой')
print(cor_quantity_price)

